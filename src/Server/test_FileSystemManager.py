import pytest
from src.Server.FileSystemManager import FileSystemManager as fsm
from src.ErrorMessages import ErrorMessages
import src.Server.ServerTools as Tools
import shutil



class TestFileSystemManager:

    def setup_class(self):
        shutil.rmtree(Tools.get_main_path(), ignore_errors=True)

    def test_create_table_without_db(self):
        with pytest.raises(Exception) as excinfo:
            fsm.create_table(None, {"test": "test"})
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.NO_DB_SELECTED

    def test_get_tables_without_db(self):
        with pytest.raises(Exception) as excinfo:
            fsm.get_tables(None)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.NO_DB_SELECTED

    def test_drop_without_db(self):
        with pytest.raises(Exception) as excinfo:
            fsm.drop_table(None, "drop test")
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.NO_DB_SELECTED

    def test_insert_into_without_db(self):
        with pytest.raises(Exception) as excinfo:
            fsm.insert_into(None, {"test": "test"})
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.NO_DB_SELECTED