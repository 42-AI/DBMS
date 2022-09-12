from pathlib import Path
import os, sys
from src.Server.DatabaseManager import DatabaseManager
import os.path as path
import shutil
from src.utils import colors

class FileSystemManager:

    @staticmethod
    def create_db(db_name):
        DatabaseManager.create_db_dir(db_name)
