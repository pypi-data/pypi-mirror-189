from __future__ import annotations

import logging
import warnings
from datetime import datetime
from typing import Any, cast

from airflow import settings as airflow_settings
from airflow.models.connection import Connection
from airflow.models.dag import DAG
from airflow.models.dagrun import DagRun
from airflow.models.taskinstance import TaskInstance
from airflow.secrets.local_filesystem import LocalFilesystemBackend
from airflow.utils import timezone
from airflow.utils.session import provide_session
from airflow.utils.state import DagRunState, State
from airflow.utils.types import DagRunType
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.session import Session

from astro.sql.operators.cleanup import AstroCleanupException
from sql_cli.constants import LOGGER_NAME
from sql_cli.exceptions import ConnectionFailed
from sql_cli.utils.rich import RichHandler, rprint

log = logging.getLogger(LOGGER_NAME)

# This was added to airflow.utils.session as part of Airflow 2.2.4, we're copying it here for backwwards
# compatibility (currently we support Airflow 2.1 onwards)
# It seems like a hack to avoid MyPy complaining we're assigning None to a variable that should be an Airflow session
NEW_SESSION = airflow_settings.SASession = cast(airflow_settings.SASession, None)


class AstroFilesystemBackend(LocalFilesystemBackend):
    def __init__(
        self,
        connections: dict[str, Connection] | None = None,
        variables_file_path: str | None = None,
        connections_file_path: str | None = None,
    ):
        self._local_conns: dict[str, Connection] = connections or {}
        super().__init__(variables_file_path=variables_file_path, connections_file_path=connections_file_path)

    @property
    def _local_connections(self) -> dict[str, Connection]:
        conns = self._local_conns
        conns.update(super()._local_connections)
        return conns


@provide_session
def run_dag(
    dag: DAG,
    execution_date: datetime | None = None,
    run_conf: dict[str, Any] | None = None,
    conn_file_path: str | None = None,
    variable_file_path: str | None = None,
    connections: dict[str, Connection] | None = None,
    verbose: bool = False,
    session: Session = NEW_SESSION,
) -> DagRun:
    """
    Execute one single DagRun for a given DAG and execution date.

    :param dag: The Airflow DAG we will run
    :param execution_date: execution date for the DAG run
    :param run_conf: configuration to pass to newly created dagrun
    :param conn_file_path: file path to a connection file in either yaml or json
    :param variable_file_path: file path to a variable file in either yaml or json
    :param session: database connection (optional)

    :return: the dag run object
    """
    execution_date = execution_date or timezone.utcnow()
    log.debug("Clearing existing task instances for execution date %s", execution_date)
    dag.clear(
        start_date=execution_date,
        end_date=execution_date,
        dag_run_state=False,  # type: ignore
        session=session,
    )
    log.debug("Getting dagrun for dag %s", dag.dag_id)
    dr: DagRun = _get_or_create_dagrun(
        dag=dag,
        start_date=execution_date,
        execution_date=execution_date,
        run_id=DagRun.generate_run_id(DagRunType.MANUAL, execution_date),
        session=session,
        conf=run_conf,
    )

    if conn_file_path or variable_file_path or connections:
        # To get around the fact that we reload certain modules, we need to import here
        from airflow.configuration import secrets_backend_list

        local_secrets = AstroFilesystemBackend(
            variables_file_path=variable_file_path,
            connections_file_path=conn_file_path,
            connections=connections,
        )
        secrets_backend_list.insert(0, local_secrets)

    tasks = dag.task_dict
    log.debug("starting dagrun")
    # Instead of starting a scheduler, we run the minimal loop possible to check
    # for task readiness and dependency management. This is notably faster
    # than creating a BackfillJob and allows us to surface logs to the user
    while dr.state == State.RUNNING:
        schedulable_tis, _ = dr.update_state(session=session)
        for ti in schedulable_tis:
            add_loghandler(ti, verbose)
            ti.task = tasks[ti.task_id]
            _run_task(ti, session=session)
    if conn_file_path or variable_file_path or connections:
        # Remove the local variables we have added to the secrets_backend_list
        secrets_backend_list.pop(0)  # noqa
    return dr


def add_loghandler(ti: TaskInstance, verbose: bool) -> None:
    """
    Add a formatted logger to the taskinstance so all logs are surfaced to the command line instead
    of into a task file. Since this is a local test run, it is much better for the user to see logs
    in the command line, rather than needing to search for a log file.

    :param ti: The taskinstance that will receive a logger
    :param verbose: Whether to enable debug or critical logs
    """
    log.debug("Adding RichHandler to taskinstance %s", ti.task_id)
    if verbose:
        ti.log.setLevel(logging.INFO)
        ti.log.manager.disable = logging.NOTSET
    else:
        ti.log.setLevel(logging.CRITICAL)
    ti.log.addHandler(RichHandler(markup=True))


def _run_task(ti: TaskInstance, session: Session) -> None:
    """
    Run a single task instance, and push result to Xcom for downstream tasks. Bypasses a lot of
    extra steps used in `task.run` to keep our local running as fast as possible
    This function is only meant for the `dag.test` function as a helper function.

    :param ti: TaskInstance to run
    """
    if hasattr(ti, "map_index") and ti.map_index >= 0:
        rprint(f"Processing [bold yellow]{ti.task_id}[/bold yellow][{ti.map_index}]...", end=" ")
    else:
        rprint(f"Processing [bold yellow]{ti.task_id}[/bold yellow]...", end=" ")

    try:
        warnings.filterwarnings(action="ignore")
        ti._run_raw_task(session=session)  # skipcq: PYL-W0212
        session.flush()
        session.commit()
        rprint("[bold green]SUCCESS[/bold green]")
    except OperationalError as operational_exception:
        rprint("[bold red]FAILED[/bold red]")
        orig_exception = operational_exception.orig
        orig_message = orig_exception.args[0]
        raise ConnectionFailed(orig_message, conn_id=getattr(ti.task, "conn_id", "")) from orig_exception
    except AstroCleanupException:
        rprint("aql.cleanup async, continuing")
    except Exception:
        rprint("[bold red]FAILED[/bold red]")
        raise


def _get_or_create_dagrun(
    dag: DAG,
    conf: dict[Any, Any] | None,
    start_date: datetime,
    execution_date: datetime,
    run_id: str,
    session: Session,
) -> DagRun:
    """
    Create a DAGRun, but only after clearing the previous instance of said dagrun to prevent collisions.
    This function is only meant for the `dag.test` function as a helper function.

    :param dag: Dag to be used to find dagrun
    :param conf: configuration to pass to newly created dagrun
    :param start_date: start date of new dagrun, defaults to execution_date
    :param execution_date: execution_date for finding the dagrun
    :param run_id: run_id to pass to new dagrun
    :param session: sqlalchemy session

    :return: the Dagrun object needed to run tasks.
    """
    log.debug("dagrun id: %s", dag.dag_id)
    dr: DagRun = (
        session.query(DagRun)
        .filter(DagRun.dag_id == dag.dag_id, DagRun.execution_date == execution_date)
        .first()
    )
    if dr:
        session.delete(dr)
        session.commit()
    dr = dag.create_dagrun(
        state=DagRunState.RUNNING,
        execution_date=execution_date,
        run_id=run_id,
        start_date=start_date or execution_date,
        session=session,
        conf=conf,  # type: ignore
    )
    return dr
