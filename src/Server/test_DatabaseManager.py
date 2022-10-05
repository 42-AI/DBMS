from src.Server.DatabaseManager import DatabaseManager
from src.ErrorMessages import ErrorMessages
import src.Server.ServerTools as Tools
from src.Server.ServerTools import ServerTools
import os
import shutil
import pytest

class TestDatabaseManager:


    @pytest.mark.parametrize("db_name", ["database_test"])
    # create a db
    def test_db_creation(self, db_name):
        DatabaseManager.create_db_dir(db_name)
        assert db_name in os.listdir(Tools.get_main_path())
        shutil.rmtree(Tools.get_main_path())


    @pytest.mark.parametrize("db_name", ["database_exist"])
    # create a db already exist
    def test_db_creation_already_exist(self, db_name):
        DatabaseManager.create_db_dir(db_name)
        with pytest.raises(Exception) as excinfo:
            DatabaseManager.create_db_dir(db_name)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.DB_ALREADY_EXIST
        shutil.rmtree(Tools.get_main_path())

    @pytest.mark.parametrize("db_name", ["database_delete"])
    # delete db
    def test_db_deletion(self, db_name):
        DatabaseManager.create_db_dir(db_name)
        DatabaseManager.drop_db_dir(db_name)
        assert db_name not in os.listdir(Tools.get_main_path())

    @pytest.mark.parametrize("db_name", ["database_unexistent"])
    # delete db that not exist
    def test_db_deletion_does_not_exist(self, db_name):
        with pytest.raises(Exception) as excinfo:
            DatabaseManager.drop_db_dir(db_name)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.DB_DOES_NOT_EXIST

    @pytest.mark.parametrize("db_list", [["user", "data", "likes", "comments"]])
    # gets db
    def test_get_databases(self, db_list):
        shutil.rmtree(Tools.get_main_path())
        for db in db_list:
            DatabaseManager.create_db_dir(db)
        dbs = DatabaseManager.get_dbs()
        for db in db_list:
            assert db in dbs
        for db in dbs:
            assert db in db_list

    # gets db with no main dir
    def test_get_databases_with_no_main_dir(self):
        shutil.rmtree(Tools.get_main_path())
        with pytest.raises(Exception) as excinfo:
            DatabaseManager.get_dbs()
        exception_msg = excinfo.value.args[0]
        assert exception_msg == ErrorMessages.NO_DBS_DIR