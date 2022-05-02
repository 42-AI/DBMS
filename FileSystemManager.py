from pathlib import Path
import os, sys
import os.path as path
import shutil
_MAIN_PATH_NAME = ".dbms"
_MAIN_PATH = path.join(os.getcwd(), _MAIN_PATH_NAME)

class FileSystemManager:

    @staticmethod
    def _get_dir_fullPath(_dir: str) -> str:
        if not _dir:
            print ("_get_dir_fullPath: _dir is null")
            return
        return path.join(_MAIN_PATH , _dir)

    @staticmethod
    def _get_file_fullPath(file: str, _dir: str) -> str:
        if not _dir:
            print ("_get_dir_fullPath: _dir is null")
            return
        if not file:
            print ("_get_dir_fullPath: file is null")
            return
        return path.join(FileSystemManager._get_dir_fullPath(_dir), file)

    @staticmethod
    def create_main_directory():
        if not path.isdir(path.expanduser(_MAIN_PATH)):
            os.mkdir(path.expanduser(_MAIN_PATH))

    @staticmethod
    def create_db_dir(db_name: str):
        FileSystemManager.create_main_directory()
        db_fullPath = path.join(_MAIN_PATH , db_name)
        if path.isdir(path.expanduser(db_fullPath)):
            print(f"Error: database {db_name} already exists.", file=sys.stderr)
            return
        os.mkdir(path.expanduser(db_fullPath))

    @staticmethod
    def create_table_file(table_name: str, db_name: str, csv_def: str):
        table_fullPath = FileSystemManager._get_file_fullPath(table_name, db_name)
        if path.exists(table_fullPath):
            print(f"Error: table {table_name} already exists.", file=sys.stderr)
            return
        if not path.isdir(path.expanduser(FileSystemManager._get_dir_fullPath(db_name))):
            print(f"Error: database {db_name} doesn't exists.", file=sys.stderr)
            return
        Path(table_fullPath).touch()
        file = open(table_fullPath, "w")
        fist_line=",".join(str(elem) for elem in csv_def)
        file.write(fist_line)

    @staticmethod
    def drop_table_file(table_name: str, db_name: str):
        table_fullPath = FileSystemManager._get_file_fullPath(table_name, db_name)
        db_fullPath = FileSystemManager._get_dir_fullPath(db_name)
        if not table_fullPath:
            print("no valid table")
            return
        if not path.exists(table_fullPath):
            print(f"Error: table {table_name} doesn't exists.", file=sys.stderr)
            return
        if not path.isdir(path.expanduser(db_fullPath)):
            print(f"Error: database {db_name} doesn't exists.", file=sys.stderr)
            return
        os.remove(table_fullPath)

    @staticmethod
    def drop_db_dir(db_name: str):
        db_dir_fullPath = FileSystemManager._get_dir_fullPath(db_name)
        if not db_dir_fullPath:
            print("no valid DB used")
            return
        if not path.isdir(db_dir_fullPath):
            print(f"Error: database {db_name} doesn't exists.", file=sys.stderr)
            return
        shutil.rmtree(db_dir_fullPath)

    @staticmethod
    def get_dbs() -> list :
        elements = os.listdir(_MAIN_PATH)
        dbs = []
        for element in elements:
            if path.isdir(FileSystemManager._get_file_fullPath(element, _MAIN_PATH)):
                dbs.append(element)
        return dbs

    @staticmethod
    def get_tables(db_name) -> list :
        return os.listdir(FileSystemManager._get_dir_fullPath(db_name))
        