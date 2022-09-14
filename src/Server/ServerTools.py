import os
import os.path as path
MAIN_PATH_NAME = ".dbms"
MAIN_PATH = path.join(os.getcwd(), MAIN_PATH_NAME)

class ServerTools:

    ##### Utils ####
    @staticmethod
    def get_dir_fullPath(_dir: str):
        if not _dir:
            print ("_get_dir_fullPath: _dir is null")
            return
        return path.join(MAIN_PATH , _dir)

    @staticmethod
    def get_file_fullPath(file: str, _dir: str):
        if not _dir:
            print ("_get_dir_fullPath: _dir is null")
            return
        if not file:
            print ("_get_dir_fullPath: file is null")
            return
        return path.join(ServerTools.get_dir_fullPath(_dir), file)
