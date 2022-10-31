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
        RowManager._add_item(data["FIELD"], data["DEFAULT"])

    ######### Delete: Public ########
    @staticmethod
    def delete_table(db_name: str, table_name: str, conditional_func, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        RowManager._remove_lines(conditional_func)

    @staticmethod
    def delete_item(db_name: str, table_name: str, item, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        RowManager._remove_item(item)

    ######## Update: Public #########
    @staticmethod
    def modify_table(db_name: str, table_name: str, conditional_func, modifier_func, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        RowManager._modifyLine(conditional_func, modifier_func)

    @staticmethod
    def change_row(db_name: str, table_name: str, command, file_type="data"):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.file_type = file_type
        values = command["VALUE"]
        RowManager._ChangeRowName(values["OLD_NAME"], values["NEW_NAME"])

    ########## Insert: Private #######
    @staticmethod
    def _append_line():
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
    def _remove_lines(conditional_func):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        for row in data:
            if conditional_func(row):
                data.remove(row)
        csv_handler.set_content(data)
        csv_handler.__del__()

    @staticmethod
    def _remove_item(item):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        list(map(lambda x: x.pop(item), data))
        csv_handler.set_content(data)
        csv_handler.__del__()

    ######## Update: Private #########
    @staticmethod
    def _modifyLine(conditional_func, modifier_func):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        for row in data:
            if conditional_func(row):
                index = data.index(row)
                data[index] = modifier_func(row)
        csv_handler.set_content(data)
        csv_handler.__del__()

    @staticmethod
    def _ChangeRowName(old_name, new_name):
        csv_handler = RowManager._getCsvHandler()
        data = csv_handler.get_content()
        for row in data:
            row[new_name] = row[old_name]
            row.pop(old_name)
        csv_handler.set_content(data)
        csv_handler.__del__()

    ######## Get: Private #######
    @staticmethod
    def _getCsvHandler():
        file_full_path = ServerTools.get_file_full_path(RowManager.table_name, RowManager.db_name, RowManager.type)
        return csvHandler(file_full_path)

