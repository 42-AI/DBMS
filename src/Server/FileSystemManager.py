from pathlib import Path
import os, sys
from src.Server.DatabaseManager import DatabaseManager
from src.Server.TableManager import TableManager
from src.Server.RowManager import RowManager
from src.ErrorMessages import ErrorMessages
import os.path as path
from src.utils import colors

class FileSystemManager:

###### Database ######
    @staticmethod
    def create_db(db_name):
        DatabaseManager.create_db_dir(db_name)

    @staticmethod
    def drop_db(db_name):
        DatabaseManager.drop_db_dir(db_name)

    @staticmethod
    def get_databases():
        return DatabaseManager.get_dbs()

######   Table   ######

    @staticmethod
    def create_table(db_name, data):
        if db_name is None:
            raise Exception(ErrorMessages.NO_DB_SELECTED)
        TableManager.create_table(db_name, data['NAME'], data['DESCRIPTION'])

    @staticmethod
    def get_tables(db_name):
        if db_name is None:
            raise Exception(ErrorMessages.NO_DB_SELECTED)
        return TableManager.get_tables(db_name)

    @staticmethod
    def drop_table(db_name, table_name):
        if db_name is None:
            raise Exception(ErrorMessages.NO_DB_SELECTED)
        TableManager.drop_table(db_name, table_name)

####### Row #####

    @staticmethod
    def insert_into(db_name, data):
        if db_name is None:
            raise Exception(ErrorMessages.NO_DB_SELECTED)
        RowManager.insert_table(db_name, data["NAME"], data["DATA"])
