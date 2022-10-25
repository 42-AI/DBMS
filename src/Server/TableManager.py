from src.Server.ServerTools import ServerTools
from src.Server.RowManager import RowManager
from src.Server.csvHandler import csvHandler
from src.ErrorMessages import ErrorMessages
import src.Server.ServerTools as Tools
import os.path as path
import os, sys
import shutil


class TableManager:

    db_name = ''
    table_name = ''
    table_description = ''
    meta_description = ''

########## Creation: Public #######
    @staticmethod
    def create_table(db_name: str, table_name: str, table_description):
        TableManager.db_name = db_name
        TableManager.table_name = table_name
        TableManager.table_description = table_description
        TableManager.meta_description = table_description[0].keys()
        TableManager._create_table_dir()
        TableManager._create_table_file()
        TableManager._create_meta_table_file()

    ########## Delete: Public #######
    @staticmethod
    def drop_table(db_name: str, table_name: str):
        TableManager.db_name = db_name
        TableManager.table_name = table_name
        TableManager._delete_table_dir()

    ########## get: Public #######
    @staticmethod
    def get_tables(db_name: str):
        TableManager.db_name = db_name
        return TableManager._get_tables_array()

    ######### Update: Public #########

    @staticmethod
    def alter_table(db_name: str, table_name: str, command: str):
        file_type = "meta"
        field_name = command #TODO: extract field name from command
        if add :
            RowManager.insert_table(db_name, table_name, command, file_type=file_type)
            RowManager.add_item(db_name, field_name, command)
        elif drop:
            RowManager.delete_table(db_name, table_name, command, file_type=file_type)
            RowManager.delete_item(db_name, table_name, field_name)
        elif modify:
            



    ######### Creation: Private ########
    @staticmethod
    def _create_table_file():
        table_fields = TableManager._get_table_fields();
        file_type = "data"
        return TableManager._create_file(TableManager.table_name, TableManager.db_name, file_type, table_fields, [])

    @staticmethod
    def _create_meta_table_file():
        meta_description = TableManager._get_meta_description()
        meta_content = TableManager.table_description
        file_type = "meta"
        return TableManager._create_file(TableManager.table_name, TableManager.db_name, file_type, meta_description, meta_content)

    @staticmethod
    def _create_file(table_name: str, dir_name: str, file_type: str, header, content: str):
        file_full_path = ServerTools.get_file_full_path(table_name, dir_name, file_type)
        if path.exists(file_full_path):
            raise Exception(ErrorMessages.TABLE_ALREADY_EXIST)
        csv_handler = csvHandler(file_full_path, header=header, content=content)
        csv_handler.__del__()
        return file_full_path

    @staticmethod
    def _create_table_dir():
        table_dir_full_path = ServerTools.get_table_dir_full_path(TableManager.db_name, TableManager.table_name)
        os.mkdir(path.expanduser(table_dir_full_path))


    ######### Get: Private ########

    @staticmethod
    def _get_table_fields():
        fields = []
        for field in TableManager.table_description:
            fields.append(field["FIELD"])
        return fields

    @staticmethod
    def _get_meta_description():
        return TableManager.table_description[0].keys()

    @staticmethod
    def _get_tables_array():
        dir_list = os.listdir(os.getcwd())
#        if dir_list not in Tools.MAIN_PATH:
#            print(f"{colors.BOLD}Empty set{colors.ENDC}")
#            return
        tables = os.listdir(ServerTools.get_db_dir_full_path(TableManager.db_name))
        return tables

    ######### Delete: Private ########

    @staticmethod
    def _delete_table_dir():
        table_dir_full_path = ServerTools.get_table_dir_full_path(TableManager.db_name, TableManager.table_name)
        shutil.rmtree(table_dir_full_path)
