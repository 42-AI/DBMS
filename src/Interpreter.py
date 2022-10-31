from src.Server.FileSystemManager import FileSystemManager as fsm
from src.Server.DatabaseManager import DatabaseManager
from src.ErrorMessages import ErrorMessages
from src.Show import Show
import sys
from src.utils import colors


class DatabaseName:
    db_name = None


class Interpreter:
    @staticmethod
    def execute(parsingTree):
        keyword_functions = {
            "DROP DATABASE": lambda node: fsm.drop_db(node.data),
            "DROP TABLE": lambda node: fsm.drop_table(DatabaseName.db_name, node.data),
            "CREATE TABLE": lambda node: fsm.create_table(DatabaseName.db_name, node.data),
            "CREATE DATABASE": lambda node: fsm.create_db(node.data),
            "SHOW DATABASES": lambda node: Show.databases(),
            "SHOW TABLES": lambda node: Show.tables(DatabaseName.db_name),
            "INSERT INTO": lambda node: fsm.insert_into(DatabaseName.db_name, node.data),
            "ALTER TABLE": lambda node: fsm.alter_table(DatabaseName.db_name, node.data),
        }
        while parsingTree:
            # print(f"{colors.WARNING}DATABASE NAME: {DatabaseName.db_name}{colors.ENDC}")
            if parsingTree.keyword.upper() == "USE":
                if parsingTree.data not in DatabaseManager.get_dbs():
                    raise Exception(ErrorMessages.DB_DOES_NOT_EXIST)
                DatabaseName.db_name = parsingTree.data
            elif parsingTree.keyword.upper() in keyword_functions.keys():
                keyword_functions[parsingTree.keyword.upper()](parsingTree)
            parsingTree = parsingTree.next
