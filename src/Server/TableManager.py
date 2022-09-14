from src.Server.ServerTools import ServerTools
import os.path as path
import os, sys


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
        TableManager._create_table_file()
        TableManager._create_meta_table_file()

    @staticmethod
    def drop_table(db_name: str, table_name: str):
        TableManager.db_name = db_name
        TableManager.table_name = table_name
        TableManager._delete_table_file()
        TableManager._delete_meta_table_file()


######### Creation: Private ########
    @staticmethod
    def _create_table_file():
        table_fields = TableManager._get_table_fields();
        return TableManager._create_file(TableManager.table_name, TableManager.db_name, table_fields)

    @staticmethod
    def _create_meta_table_file():
        meta_tabel_name = TableManager.get_meta_name()
        meta_description = TableManager._get_meta_description()
        meta_content = TableManager._get_meta_content()
        return TableManager._create_file(meta_tabel_name, TableManager.db_name, f"{meta_description}\n{meta_content}")

    @staticmethod
    def _create_file(file_name: str, dir_name: str, file_content: str):
        file_fullPath = ServerTools.get_file_fullPath(file_name, dir_name)
        if path.exists(file_fullPath):
            print(f"Error: table {file_name} already exists.", file=sys.stderr)
            return
        if not path.isdir(path.expanduser(ServerTools.get_dir_fullPath(dir_name))):
            print(f"Error: database {dir_name} doesn't exists.", file=sys.stderr)
            return
        f = open(file_fullPath, "x")
        f.write(file_content)
        f.close()
        return file_fullPath

    ######### Get: Private ########

    @staticmethod
    def _get_table_fields():
        fields = ''
        for field in TableManager.table_description:
            fields += field["FIELD"] + ", "
        return fields[:-2] + '\n'

    @staticmethod
    def _get_meta_description():
        return ",".join(str(key) for key in TableManager.table_description[0].keys())

    @staticmethod
    def _get_meta_content():
        meta_content = ''
        for field in TableManager.table_description:
            field_meta = ''
            for meta_field in TableManager.meta_description:
                field_meta += str(field[meta_field]) + ','
            meta_content += str(field_meta[:-1]) + '\n'
        return meta_content[:-1]

    @staticmethod
    def get_tables(db_name):
        dir_list = os.listdir(os.getcwd())
        if _MAIN_PATH_NAME not in dir_list:
            print(f"{colors.BOLD}Empty set{colors.ENDC}")
            return
        return os.listdir(ServerTools.get_dir_fullPath(db_name))

######### Delete: Private ########

    @staticmethod
    def _delete_table_file():
        TableManager._delete_file(TableManager.db_name, TableManager.table_name)

    @staticmethod
    def _delete_meta_table_file():
        TableManager._delete_file(TableManager.db_name, TableManager.get_meta_name())

    @staticmethod
    def _delete_file(db_name: str, table_name: str):
        table_fullPath = ServerTools.get_file_fullPath(table_name, db_name)
        db_fullPath = ServerTools.get_dir_fullPath(db_name)
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

######### Delete: Private ########
    @staticmethod
    def get_meta_name():
        return "meta_" + TableManager.table_name