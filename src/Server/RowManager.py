from src.Server.ServerTools import ServerTools
import src.Server.ServerTools as Tools

class RowManager:

    db_name = ''
    table_name = ''
    content = ''

    ########## Insert: Public #######
    @staticmethod
    def insert_table(db_name: str, table_name: str, content):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.content = content

    ########## Insert: Private #######
    @staticmethod
    def write_table():
        #insert data

    @staticmethod
    def build_row(row_dict: dict):
        row_str = '';
        structure = get_tabel_structure()
        for field in structure:
            row_str =+ str(row_dict[field]) + ','
        return fields[:-2] + '\n'

    ########## Get: Private #######
        @saticmethod
        def get_tabel_structure():
            table_data_file_full_path = ServerTools.get_file_full_path(RowManager.table_name, RowManager.db_name, "data")
            f = open(table_data_file_full_path, "r")
            lines = f.readlines()
            line = lines[0]
            structure = line.split(",")
            return structure