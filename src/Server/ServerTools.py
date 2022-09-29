import os
import os.path as path
MAIN_PATH_NAME = ".dbms"
MAIN_PATH = path.join(os.getcwd(), MAIN_PATH_NAME)

class ServerTools:

    ##### Utils ####
    @staticmethod
    def get_db_dir_full_path(_db_dir: str):
        if not _db_dir:
            print("_get_db_dir_full_path: _dir is null")
            return
        return path.join(MAIN_PATH , _db_dir)

    @staticmethod
    def get_table_dir_full_path(_db_dir: str, _table_dir):
        if not _db_dir:
            print("_get_db_dir_full_path: _dir is null")
            return
        return path.join(ServerTools.get_db_dir_full_path(_db_dir), _table_dir)

    @staticmethod
    def get_file_full_path(_table_dir: str, _db_dir: str, file_type:str):
        file_name = file_type + ".csv"
        if not _db_dir:
            print ("_get_db_dir_full_path: _dir is null")
            return
        if not file_name:
            print ("_get_db_dir_full_path: file is null")
            return
        return path.join(ServerTools.get_table_dir_full_path(_db_dir, _table_dir), file_name)
