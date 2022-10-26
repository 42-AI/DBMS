import pytest
import subprocess
from get_project_root import root_path
SQL_SCRIPTS_TEST_DIR = "./tests/resources/SQL_scripts/"

from tests.resources.SQL_scripts.scripts_expectation import script_expectation_array
ROOT_DIR = root_path(ignore_cwd=False)

class TestIntegration:

    @pytest.mark.parametrize("file_name, expected_output", script_expectation_array)
    def test_sql_scripts(self, file_name, expected_output):
        file_path = SQL_SCRIPTS_TEST_DIR + file_name
        with open(file_path, 'rb') as f:
            data = f.read()
        program_output = subprocess.run(["python3", "main.py"],input=data , stdout=subprocess.PIPE)
        assert program_output.stdout.decode('utf-8') == expected_output

