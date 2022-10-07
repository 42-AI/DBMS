from src.Interpreter import Interpreter, DatabaseName
from src.Server.DatabaseManager import DatabaseManager
from src.ErrorMessages import ErrorMessages
from src.Parsing.ParsingNode import Node
import src.Server.ServerTools as Tools
import shutil
import pytest

class TestInterpreter:

    @classmethod
    def setup_class(self):
        shutil.rmtree(Tools.get_main_path(), ignore_errors=True)

    @classmethod
    def teardown_class(self):
        shutil.rmtree(Tools.get_main_path(), ignore_errors=True)


    @pytest.mark.parametrize("db_name", ["database_test"])
    def test_use(self, db_name):
        DatabaseManager.create_db_dir(db_name)
        Interpreter.execute(Node(keyword="USE", data=db_name))
        assert DatabaseName.db_name == db_name

    @pytest.mark.parametrize("db_name", ["database_prim"])
    def test_use_lowcase(self, db_name):
        DatabaseManager.create_db_dir(db_name)
        Interpreter.execute(Node(keyword="use", data=db_name))
        assert DatabaseName.db_name == db_name

    @pytest.mark.parametrize("db_name", ["void"])
    def test_use_unexistent_db(self, db_name):
        with pytest.raises(Exception) as excinfo:
            Interpreter.execute(Node(keyword="USE", data=db_name))
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.DB_DOES_NOT_EXIST


