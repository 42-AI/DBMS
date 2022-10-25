from src.Server.ServerTools import ServerTools
import src.Server.ServerTools as Tools
from src.Server.csvHandler import csvHandler

class RowManager:

    db_name = ''
    table_name = ''
    content = ''
    file_type = ''

    ########## Insert: Public #######
    @staticmethod
    def insert_table(db_name: str, table_name: str, content, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.content = content
        RowManager.file_type = file_type
        RowManager._append_line()

    @staticmethod
    def add_item(db_name: str, table_name: str, data, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        RowManager._add_item(data["item"], data["default_value"])

    ######### Delete: Public ########
    @staticmethodc
    def delete_table(db_name: str, table_name: str, command, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        conditional_func, replacement_func = command #TODO method to convert command to functions
        RowManager._removeLines(conditional_func, replacement_func)

    ######## Update: Public #########
    @staticmethodc
    def modify_table(db_name: str, table_name: str, conditional_func, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        conditional_func = command  # TODO method to convert command to function
        RowManager._modifyLine(conditional_func)

    ########## Insert: Private #######
    @staticmethod
    def _appendLine():
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        data.extend(RowManager.content)
        csv_handler.set_content(data)

    @staticmethod
    def _add_item(item, default_value=""):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        list(map(lambda x: x.update({item, default_value}), data))
        csv_handler.set_content(data)
        csv_handler.__del__()

    ######## Delete: Private
    @staticmethod
    def _removeLines(conditional_func):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        for row in data:
            if conditional_func(row):
                data.remove(data)
        csv_handler.set_content(data)
        csv_handler.__del__()

    ######## Update: Public #########
    @staticmethod
    def _modifyLine(conditional_func, replacement_func):


    ######## Get: Private #######
    @staticmethod
    def _getCsvHandler():
        file_full_path = ServerTools.get_file_full_path(RowManager.table_name, RowManager.db_name, RowManager.type)
        return csvHandler(file_full_path)

