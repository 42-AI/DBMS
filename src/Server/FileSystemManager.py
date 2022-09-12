from pathlib import Path
import os, sys
import os.path as path
import shutil
from src.utils import colors
_MAIN_PATH_NAME = ".dbms"
_MAIN_PATH = path.join(os.getcwd(), _MAIN_PATH_NAME)

class FileSystemManager:

    @staticmethod
    def _get_dir_fullPath(_dir: str):
        if not _dir:
            print ("_get_dir_fullPath: _dir is null")
            return
        return path.join(_MAIN_PATH , _dir)

    @staticmethod
    def _get_file_fullPath(file: str, _dir: str):
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