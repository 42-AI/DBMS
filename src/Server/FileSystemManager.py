from pathlib import Path
import os, sys
from src.Server.DatabaseManager import DatabaseManager
import os.path as path
from src.utils import colors

class FileSystemManager:

    @staticmethod
    def create_db(db_name):
        DatabaseManager.create_db_dir(db_name)

    @staticmethod
    def drop_db(db_name):
        DatabaseManager.drop_db_dir(db_name)
