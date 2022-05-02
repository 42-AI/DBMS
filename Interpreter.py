from FileSystemManager import FileSystemManager as fsm
from Show import Show
import sys

class DatabaseName:
    db_name = None

class Interpreter:
    @staticmethod
    def execute(parsingTree):
        keyword_functions = {
            "CREATE DATABASE": lambda name, db_name, lst: fsm.create_db_dir(name),
            "DROP DATABASE": lambda name, db_name, lst: fsm.drop_db_dir(name),
            "CREATE TABLE": lambda name, db_name, lst: fsm.create_table_file(name, db_name, lst),
            "DROP TABLE": lambda name, db_name, lst: fsm.drop_table_file(name, db_name),
            "SHOW DATABASES": lambda name, db_name, lst: Show.databases(),
            "SHOW TABLES": lambda name, db_name, lst: Show.tables(db_name),
        }
        while parsingTree:
            print("DATABASE NAME:", DatabaseName.db_name)
            if parsingTree.keyword == "USE":
                DatabaseName.db_name = parsingTree.name
            elif parsingTree.keyword in keyword_functions.keys():
                keyword_functions[parsingTree.keyword](parsingTree.name, DatabaseName.db_name, parsingTree.lst)
            parsingTree = parsingTree.next