from src.Server.FileSystemManager import FileSystemManager as fsm
from src.Show import Show
import sys
from src.utils import colors


class DatabaseName:
    db_name = None


class Interpreter:
    @staticmethod
    def execute(parsingTree):
        keyword_functions = {
            # "DROP DATABASE": lambda node: fsm.drop_db_dir(node.name),
            # "DROP TABLE": lambda node: fsm.drop_table_file(node.name, node.data),
            # "CREATE TABLE": lambda node: fsm.create_table_file(node.name, node.data, node.lst),
            "CREATE DATABASE": lambda node: fsm.create_db_dir(node.data),
            "SHOW DATABASES": lambda node: Show.databases(),
            "SHOW TABLES": lambda node: Show.tables(node.data),
        }
        while parsingTree:
            # print(f"{colors.WARNING}DATABASE NAME: {DatabaseName.db_name}{colors.ENDC}")
            if parsingTree.keyword == "USE":
                DatabaseName.db_name = parsingTree.data
            elif parsingTree.keyword in keyword_functions.keys():
                keyword_functions[parsingTree.keyword](parsingTree)
            parsingTree = parsingTree.next
