from FileSystemManager import FileSystemManager as fsm
from Show import Show
import sys
from textColor import bcolors

class DatabaseName:
    db_name = None

class Interpreter:
    @staticmethod
    def execute(parsingTree):
        keyword_functions = {
            "CREATE DATABASE": lambda node: fsm.create_db_dir(node.name),
            "DROP DATABASE": lambda node: fsm.drop_db_dir(node.name),
            "CREATE TABLE": lambda node: fsm.create_table_file(node.name, node.db_name, node.lst),
            "DROP TABLE": lambda node: fsm.drop_table_file(node.name, node.db_name),
            "SHOW DATABASES": lambda node: Show.databases(),
            "SHOW TABLES": lambda node: Show.tables(node.db_name),
        }
        while parsingTree:
            print(f"{bcolors.WARNING}DATABASE NAME: {DatabaseName.db_name}{bcolors.ENDC}")
            if parsingTree.keyword == "USE":
                DatabaseName.db_name = parsingTree.db_name
            elif parsingTree.keyword in keyword_functions.keys():
                keyword_functions[parsingTree.keyword](parsingTree)
            parsingTree = parsingTree.next