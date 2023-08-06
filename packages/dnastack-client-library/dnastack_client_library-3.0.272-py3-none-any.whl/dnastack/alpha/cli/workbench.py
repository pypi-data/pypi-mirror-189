import uuid
from typing import Optional, List

import click
from imagination import container

from dnastack.alpha.client.ewes.client import EWesClient
from dnastack.alpha.client.ewes.models import ExtendedRunListOptions, LogType, Log
from dnastack.cli.helpers.client_factory import ConfigurationBasedClientFactory
from dnastack.cli.helpers.command.decorator import command
from dnastack.cli.helpers.command.spec import ArgumentSpec
from dnastack.cli.helpers.exporter import to_json, normalize
from dnastack.cli.helpers.iterator_printer import show_iterator, OutputFormat


def _get(context_name: Optional[str] = None,
         endpoint_id: Optional[str] = None,
         namespace: Optional[str] = None) -> EWesClient:
    factory: ConfigurationBasedClientFactory = container.get(ConfigurationBasedClientFactory)
    return factory.get(EWesClient, endpoint_id=endpoint_id, context_name=context_name, namespace=namespace)


@click.group('workbench')
def alpha_workbench_command_group():
    """ Interact with Workbench """


@click.group('runs')
def runs_command_group():
    """ EWES Runs API """


@command(runs_command_group,
         'list',
         specs=[
             ArgumentSpec(
                 name='namespace',
                 arg_names=['--namespace', '-n'],
                 help='An optional flag to define the namespace to connect to. By default, the namespace will be '
                      'extracted from the users credentials.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='max_results',
                 arg_names=['--max-results'],
                 help='An optional flag to limit the total number of results.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='page',
                 arg_names=['--page'],
                 help='An optional flag to set the offset page number. '
                      'This allows for jumping into an arbitrary page of results.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='page_size',
                 arg_names=['--page-size'],
                 help='An optional flag to set the page size returned by the server.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='order',
                 arg_names=['--order'],
                 help='An optional flag to define the ordering of the results. '
                      'The value should return to the attribute name to order the results by. '
                      'By default, results are returned in descending order. '
                      'To change the direction of ordering include the "ASC" or "DESC" string after the column. '
                      'e.g.: --O "end_time", --O "end_time ASC"',
                 as_option=True
             ),
             ArgumentSpec(
                 name='states',
                 arg_names=['--state'],
                 help='An optional flag to filter the results by their state. '
                      'This flag can be defined multiple times, with the result being any of the states.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='submitted_since',
                 arg_names=['--submitted-since'],
                 help='An optional flag to filter the results with their start_time '
                      'greater or equal to the since timestamp. '
                      'The timestamp can be in iso date, or datetime format. '
                      'e.g.: -f "2022-11-23", -f "2022-11-23T00:00:00.000Z"',
                 as_option=True
             ),
             ArgumentSpec(
                 name='submitted_until',
                 arg_names=['--submitted-until'],
                 help='An optional flag to filter the results with their start_time '
                      'strictly less than the since timestamp. '
                      'The timestamp can be in iso date, or datetime format. '
                      'e.g.: -t "2022-11-23", -t "2022-11-23T23:59:59.999Z"',
                 as_option=True
             ),
             ArgumentSpec(
                 name='engine',
                 arg_names=['--engine'],
                 help='An optional flag to filter the results to runs with the given engine ID',
                 as_option=True
             ),
             ArgumentSpec(
                 name='search',
                 arg_names=['--search'],
                 help='An optional flag to perform a full text search across various fields using the search value',
                 as_option=True
             ),
         ])
def list_runs(context: Optional[str],
              endpoint_id: Optional[str],
              namespace: Optional[str],
              max_results: Optional[int],
              page: Optional[int],
              page_size: Optional[int],
              order: Optional[str],
              submitted_since: Optional[str],
              submitted_until: Optional[str],
              engine: Optional[str],
              search: Optional[str],
              states: List[str] = None):
    """ List workflow runs """

    def parse_to_datetime_iso_format(date: str, start_of_day: bool = False, end_of_day: bool = False) -> str:
        if (date is not None) and ("T" not in date):
            if start_of_day:
                return f'{date}T00:00:00.000Z'
            if end_of_day:
                return f'{date}T23:59:59.999Z'
        return date

    order_direction = None
    if order:
        order_and_direction = order.split()
        if len(order_and_direction) > 1:
            order = order_and_direction[0]
            order_direction = order_and_direction[1]

    client = _get(context_name=context, endpoint_id=endpoint_id, namespace=namespace)
    list_options: ExtendedRunListOptions = ExtendedRunListOptions(
        page=page,
        page_size=page_size,
        order=order,
        direction=order_direction,
        state=states,
        since=parse_to_datetime_iso_format(date=submitted_since, start_of_day=True),
        until=parse_to_datetime_iso_format(date=submitted_until, end_of_day=True),
        engineId=engine,
        search=search,
    )
    show_iterator(output_format=OutputFormat.JSON, iterator=client.list_runs(list_options, max_results))


@command(runs_command_group,
         'describe',
         specs=[
             ArgumentSpec(
                 name='namespace',
                 arg_names=['--namespace', '-n'],
                 help='An optional flag to define the namespace to connect to. By default, the namespace will be '
                      'extracted from the users credentials.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='status',
                 arg_names=['--status'],
                 help='Output a minimal response, only showing the status id, current state, start and stop times.',
                 as_option=True,
                 default=False
             ),
             ArgumentSpec(
                 name='inputs',
                 arg_names=['--inputs'],
                 help='Display only the run\'s inputs as json.',
                 as_option=True,
                 default=False
             ),
             ArgumentSpec(
                 name='outputs',
                 arg_names=['--outputs'],
                 help='Display only the run\'s outputs as json.',
                 as_option=True,
                 default=False
             ),
             ArgumentSpec(
                 name='include_tasks',
                 arg_names=['--include-tasks'],
                 help='Include the tasks in the output.',
                 as_option=True,
                 default=False
             ),
         ])
def describe_runs(context: Optional[str],
                  endpoint_id: Optional[str],
                  namespace: Optional[str],
                  runs: List[str],
                  status: Optional[bool],
                  inputs: Optional[bool],
                  outputs: Optional[bool],
                  include_tasks: Optional[bool]):
    """ Describe workflow run """
    client = _get(context_name=context, endpoint_id=endpoint_id, namespace=namespace)
    if status:
        described_runs = [client.get_status(run_id=run) for run in runs]
    else:
        described_runs = [client.get_run(run_id=run, include_tasks=include_tasks) for run in runs]

        if inputs:
            described_runs = [
                {
                    'run_id': described_run.run_id,
                    'inputs': described_run.request.workflow_params,
                } for described_run in described_runs
            ]
        elif outputs:
            described_runs = [
                {
                    'run_id': described_run.run_id,
                    'outputs': described_run.outputs
                } for described_run in described_runs
            ]
    click.echo(to_json(normalize(described_runs)))


@command(runs_command_group,
         'cancel',
         specs=[
             ArgumentSpec(
                 name='namespace',
                 arg_names=['--namespace', '-n'],
                 help='An optional flag to define the namespace to connect to. By default, the namespace will be '
                      'extracted from the users credentials.',
                 as_option=True
             ),
         ])
def cancel_runs(context: Optional[str],
                endpoint_id: Optional[str],
                namespace: Optional[str],
                runs: List[str] = None):
    """Cancel one or more workflow runs"""
    client = _get(context_name=context, endpoint_id=endpoint_id, namespace=namespace)
    result = client.cancel_runs(runs)
    click.echo(to_json(normalize(result)))


@command(runs_command_group,
         'delete',
         specs=[
             ArgumentSpec(
                 name='namespace',
                 arg_names=['--namespace', '-n'],
                 help='An optional flag to define the namespace to connect to. By default, the namespace will be '
                      'extracted from the users credentials.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='force',
                 arg_names=['--force'],
                 help='Force the deletion without prompting for confirmation.',
                 as_option=True,
                 default=False
             )
         ])
def delete_runs(context: Optional[str],
                endpoint_id: Optional[str],
                namespace: Optional[str],
                force: Optional[bool] = False,
                runs: List[str] = None):
    """Delete one or more workflow runs"""
    client = _get(context_name=context, endpoint_id=endpoint_id, namespace=namespace)
    if not force and not click.confirm('Do you want to proceed?'):
        return
    result = client.delete_runs(runs)
    click.echo(to_json(normalize(result)))


@command(runs_command_group,
         'logs',
         specs=[
             ArgumentSpec(
                 name='namespace',
                 arg_names=['--namespace', '-n'],
                 help='Namespace',
                 as_option=True,
                 required=True
             ),
             ArgumentSpec(
                 name='log_type',
                 arg_names=['--log-type'],
                 help='Print only stderr or stdout to the current console.',
                 as_option=True,
                 default=LogType.stdout
             ),
             ArgumentSpec(
                 name='task_name',
                 arg_names=['--task-name'],
                 help='Retrieve logs associated with the given task in the run.',
                 as_option=True
             ),
             ArgumentSpec(
                 name='max_bytes',
                 arg_names=['--max-bytes'],
                 help='Limit number of bytes to retrieve from the log stream.',
                 as_option=True,
             ),
         ])
def get_run_logs(context: Optional[str],
                 endpoint_id: Optional[str],
                 namespace: Optional[str],
                 run_id_or_log_url: str,
                 log_type: Optional[LogType] = LogType.stdout,
                 task_name: Optional[str] = None,
                 max_bytes: Optional[int] = None):
    """Get logs of a single workflow run"""

    def is_valid_uuid(val: str):
        try:
            uuid.UUID(val, version=4)
            return True
        except ValueError:
            return False

    def print_logs_by_url(log_url: str):
        for logs_chunk in client.stream_run_logs(log_url=log_url, max_bytes=max_bytes):
            if not logs_chunk:
                click.echo(f"There are no {log_type} logs")
            else:
                click.echo(logs_chunk)

    def print_logs(log: Log):
        if not log:
            return
        print_logs_by_url(log.stderr if log_type == LogType.stderr else log.stdout)

    client = _get(context_name=context, endpoint_id=endpoint_id, namespace=namespace)
    if not is_valid_uuid(run_id_or_log_url):
        print_logs_by_url(log_url=run_id_or_log_url)
        return

    described_run = client.get_run(run_id=run_id_or_log_url, include_tasks=True)
    if not task_name:
        print_logs(log=described_run.run_log)
    else:
        if not described_run.task_logs:
            click.echo("No task with a given name exists for a given run")
            return

        task = next(
            (run_task for run_task in described_run.task_logs if run_task.name.lower() == task_name.strip().lower()),
            None
        )
        if not task:
            click.echo("No task with a given name exists for a given run")
        else:
            print_logs(log=task)


alpha_workbench_command_group.add_command(runs_command_group)
