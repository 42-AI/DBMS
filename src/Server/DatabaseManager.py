import os.path as path
import os, sys
import src.Server.ServerTools as Tools
from src.Server.ServerTools import ServerTools
import shutil


class DatabaseManager:

    @staticmethod
    def create_db_dir(db_name: str):
        DatabaseManager._create_main_directory()
        db_fullPath = path.join(Tools.MAIN_PATH, db_name)
        if path.isdir(path.expanduser(db_fullPath)):
            print(f"Error: database {db_name} already exists.", file=sys.stderr)
            return
        os.mkdir(path.expanduser(db_fullPath))

    @staticmethod
    def drop_db_dir(db_name: str):
        db_dir_fullPath = ServerTools.get_dir_fullPath(db_name)
        if not db_dir_fullPath:
            print("no valid DB used")
            return
        if not path.isdir(db_dir_fullPath):
            print(f"Error: database {db_name} doesn't exists.", file=sys.stderr)
            return
        shutil.rmtree(db_dir_fullPath)

    @staticmethod
    def get_dbs():
        dir_list = os.listdir(os.getcwd())
        if Tools.MAIN_PATH_NAME not in dir_list:
            print(f"{colors.BOLD}Empty set{colors.ENDC}")
            return
        elements = os.listdir(Tools.MAIN_PATH)
        dbs = []
        for element in elements:
            if path.isdir(ServerTools.get_file_fullPath(element, Tools.MAIN_PATH)):
                dbs.append(element)
        return dbs

    @staticmethod
    def _create_main_directory():
        if not path.isdir(path.expanduser(Tools.MAIN_PATH)):
            os.mkdir(path.expanduser(Tools.MAIN_PATH))