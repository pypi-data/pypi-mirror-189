import os.path
from json import JSONDecodeError

import json
import re
import shutil
import yaml
from click.testing import CliRunner, Result
from threading import Thread
from typing import Dict, Any, List, Optional

from dnastack.__main__ import dnastack as cli_app
from dnastack.common.environments import env, flag
from dnastack.common.logger import get_logger
from dnastack.configuration.models import Configuration
from dnastack.feature_flags import in_global_debug_mode
from dnastack.json_path import JsonPath
from ..exam_helper import BaseTestCase


class CliTestCase(BaseTestCase):
    _runner = CliRunner(mix_stderr=False)

    def __init__(self, *args, **kwargs):
        super(CliTestCase, self).__init__(*args, **kwargs)
        self._logger = get_logger(f'{type(self).__name__}', self.log_level())

    def setUp(self) -> None:
        super().setUp()
        self._temporarily_remove_existing_config()

    def tearDown(self) -> None:
        super().tearDown()
        self._restore_existing_config()

    def show_output(self) -> bool:
        return in_global_debug_mode

    def _invoke(self,
                *cli_blocks: str,
                envs: Optional[Dict[str, str]] = None,
                timeout: Optional[int] = None,
                stderr=None) -> Result:
        test_envs = {
            k: 'false' if k == 'DNASTACK_DEBUG' else os.environ[k]
            for k in os.environ
            if k[0] != '_' and (k.startswith('DNASTACK_') or k.startswith('E2E_'))
        }

        if envs:
            test_envs.update(envs)

        if not timeout:
            # noinspection PyTypeChecker
            return self._runner.invoke(cli_app, cli_blocks, env=test_envs)
        else:
            shared_memory = dict()

            def runner():
                # noinspection PyTypeChecker
                shared_memory['output'] = self._runner.invoke(cli_app, cli_blocks, env=test_envs)

            invocation = Thread(target=runner)
            invocation.start()
            invocation.join(timeout)

            return shared_memory['output']

    def invoke(self,
               *cli_blocks: str,
               bypass_error: bool = False,
               debug=False,
               envs: Optional[Dict[str, str]] = None,
               timeout: Optional[int] = None,
               stderr=None) -> Result:
        self._logger.debug(f'INVOKE: python3 -m dnastack {" ".join(cli_blocks)}')
        result = self._invoke(*cli_blocks, envs=envs, timeout=timeout, stderr=stderr)
        if self.show_output() or debug:
            print()
            print(f'EXEC: {" ".join(cli_blocks)}')
            if result.stderr:
                print(f'ERROR:')
                print(self._reformat_output(result.stderr))
            if result.stdout:
                print(f'STDOUT:')
                print(self._reformat_output(result.stdout))
            print()
        if result.exception and not bypass_error:
            raise result.exception
        return result

    def expect_error_from(self, cli_blocks: List[str], error_regex: Optional[str] = None,
                          error_message: Optional[str] = None):
        result = self._invoke(*cli_blocks)

        self.assertIsNotNone(result.exception, 'The exception is not raised.')
        self.assertIsInstance(result.exception, SystemExit)

        actual_error_message = result.stdout or result.stderr

        if error_regex:
            self.assertTrue(re.search(error_regex, actual_error_message) is not None,
                            f'Unexpected error message pattern\nPattern: {error_regex}\nActual: {actual_error_message}')

        if error_message:
            self.assertEqual(actual_error_message.strip(),
                             error_message.strip(),
                             f'Unexpected error message\nExpected: {error_message}\nActual: {actual_error_message}')

    def _reformat_output(self, content) -> str:
        return '\n'.join([
            f'  | {line}' for line in content.split('\n')
        ])

    def simple_invoke(self, *cli_blocks: str):
        result = self.invoke(*cli_blocks, bypass_error=False)
        self.assertEqual(0, result.exit_code,
                         'The command "' + (' '.join(cli_blocks)) + f'" returns the exit code {result.exit_code}')
        return self.parse_json_or_yaml(result.output)

    @staticmethod
    def parse_json_or_yaml(content: str):
        try:
            return json.loads(content)
        except JSONDecodeError:
            try:
                return yaml.load(content, Loader=yaml.SafeLoader)
            except:
                raise ValueError(f'Unable to parse this content either as JSON or YAML string:\n\n{content}')

    def _show_config(self):
        self.execute(f'cat {self._config_file_path}')

    def _configure(self, config: Dict[str, str], debug=False):
        self._logger.warning('"dnastack config set" is now deprecated')
        for k, v in config.items():
            self.invoke('config', 'set', k, v)

        if debug:
            self.execute(f'cat {self._config_file_path}')

    def _add_endpoint(self, endpoint_id: str, short_service_type: str, url: str):
        self.invoke('config', 'endpoints', 'add', '-t', short_service_type, endpoint_id)
        self.invoke('config', 'endpoints', 'set', endpoint_id, 'url', url)
        return self

    def _get_endpoint(self, id: str):
        return [
            endpoint
            for endpoint in self.simple_invoke('config', 'endpoints', 'list')
            if endpoint['id'] == id
        ][0]

    def _get_endpoint_property(self, id: str, config_property: str):
        return JsonPath.get(self._get_endpoint(id), config_property)

    def _configure_endpoint(self, id: str, props: Dict[str, Any]):
        for k, v in props.items():
            self.invoke('config', 'endpoints', 'set', id, k, str(v))

        endpoint = self._get_endpoint(id)

        for k, v in props.items():
            self.assertEqual(JsonPath.get(endpoint, k), str(v))

    def _load_configuration(self) -> Configuration:
        with open(self._config_file_path, 'r') as f:
            content = f.read()
        return Configuration(**yaml.load(content, Loader=yaml.SafeLoader))
