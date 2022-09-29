from pathlib import Path
import os, sys
from src.Server.DatabaseManager import DatabaseManager
from src.Server.TableManager import TableManager
from src.Server.RowManager import RowManager
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
            print("Please select a DB")
        else:
            TableManager.create_table(db_name, data['NAME'], data['DESCRIPTION'])

    @staticmethod
    def get_tables(db_name):
        if db_name is None:
            print("Please select a DB")
        else:
            return TableManager.get_tables(db_name)

    @staticmethod
    def drop_table(db_name, data):
        print(db_name)
        print(data)
        TableManager.drop_table(db_name, data)

####### Row #####

    @staticmethod
    def insert_into(db_name, data):
        RowManager.insert_table(db_name, data["NAME"], data["DATA"])
