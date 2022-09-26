import pytest
import sys, os
import shutil
from get_project_root import root_path
from src.Server.csvHandler import csvHandler

ROOT_DIR = root_path(ignore_cwd=False)
READ_TEST_DIR = ROOT_DIR + "/tests/resources/read_test_csv/"
WRITE_TEST_DIR = ROOT_DIR + "/tests/resources/write_test_csv/"
EMPTY_DIR = READ_TEST_DIR + "empty/"
EMPTY_EXPECT = EMPTY_DIR + "empty_expectation"
VALID_DIR = READ_TEST_DIR + "valid/"
VALID_EXPECT = VALID_DIR + "valid_expectation"
WRITE_DIR = WRITE_TEST_DIR + "write/"
WRITE_EXPECT = WRITE_DIR + "write_expectation"
WRITE_TMP = WRITE_DIR + "/tmp"

from tests.resources.read_test_csv.empty.empty_expectation import empty_test_array

from tests.resources.read_test_csv.valid.valid_expectation import valid_test_array

from tests.resources.write_test_csv.write.write_expectation import write_test_array


class TestCsvHandler:

    @pytest.mark.parametrize("file_name, expected_array", empty_test_array)
    def test_read_empty_csv(self, file_name, expected_array):
        file_path = EMPTY_DIR + file_name
        csv_handler = csvHandler(file_path)
        assert csv_handler._header == expected_array

    @pytest.mark.parametrize("file_name, separator, expected_array", valid_test_array)
    def test_read_valid_csv(self, file_name, separator, expected_array):
        file_path = VALID_DIR + file_name
        csv_handler = csvHandler(file_path, separator)
        assert csv_handler.get_content() == expected_array

    @pytest.mark.parametrize("empty_file_name, full_file_name, content_array", write_test_array)
    def test_write_append_csv(self, empty_file_name, full_file_name, content_array):
        full_file_path = WRITE_DIR + full_file_name
        empty_file_path = WRITE_DIR + empty_file_name
        empty_copy_path = WRITE_TMP + empty_file_name
        shutil.copyfile(empty_file_path, empty_copy_path)
        csv_handler = csvHandler(empty_copy_path)
        csv_handler.set_content(content_array)
        csv_handler.__del__()
        control = open(full_file_path, "r")
        test = open(empty_copy_path, "r")
        assert control.readlines() == test.readlines()
        control.close()
        test.close()
