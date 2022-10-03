import os.path as path
import os, sys
import src.Server.ServerTools as Tools
from src.Server.ServerTools import ServerTools
from src.ErrorMessages import ErrorMessages
import shutil
import FileExistsError

class DatabaseManager:

    @staticmethod
    def create_db_dir(db_name: str):
        DatabaseManager._create_main_directory()
        db_full_path = path.join(Tools.MAIN_PATH, db_name)
        if path.isdir(path.expanduser(db_full_path)):
            raise FileExistsError(ErrorMessages.DB_ALREADY_EXIST)
        os.mkdir(path.expanduser(db_full_path))

    @staticmethod
    def drop_db_dir(db_name: str):
        db_dir_full_path = ServerTools.get_db_dir_full_path(db_name)
        if not db_dir_full_path:
            raise FileNotFoundError(ErrorMessages.DB_DOES_NOT_EXIST)
        if not path.isdir(db_dir_full_path):
            raise FileNotFoundError(ErrorMessages.DB_DOES_NOT_EXIST)
        shutil.rmtree(db_dir_full_path)

    @staticmethod
    def get_dbs():
        dir_list = os.listdir(os.getcwd())
        if Tools.MAIN_PATH_NAME not in dir_list:
            print(f"{colors.BOLD}Empty set{colors.ENDC}")
            return
        elements = os.listdir(Tools.MAIN_PATH)
        return elements

    @staticmethod
    def _create_main_directory():
        if not path.isdir(path.expanduser(Tools.MAIN_PATH)):
            os.mkdir(path.expanduser(Tools.MAIN_PATH))