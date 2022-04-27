from FileSystemManager import FileSystemManager as fsm
import sys

class DatabaseName:
    db_name = None

class Interpreter:
    @staticmethod
    def execute(parsingTree):
        while parsingTree:
            if parsingTree.keyword == "USE":
                DatabaseName.db_name = parsingTree.name
                print("DATABASE NAME:", DatabaseName.db_name)
            elif parsingTree.keyword == "CREATE DATABASE":
                fsm.create_db_dir(parsingTree.name)
            elif parsingTree.keyword == "DROP DATABASE":
                fsm.drop_db_dir(parsingTree.name)
            elif parsingTree.keyword == "CREATE TABLE":
                print("DATABASE NAME:", DatabaseName.db_name)
                fsm.create_table_file(parsingTree.name, DatabaseName.db_name, parsingTree.lst)
            elif parsingTree.keyword == "DROP TABLE":
                fsm.drop_table_file(parsingTree.name, DatabaseName.db_name)
            elif parsingTree.keyword == "SHOW DATABASES":
                pass
            elif parsingTree.keyword == "SHOW TABLES":
                pass

            parsingTree = parsingTree.next