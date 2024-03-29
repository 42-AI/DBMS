from src.Server.ServerTools import ServerTools
import src.Server.ServerTools as Tools
from src.Server.csvHandler import csvHandler

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
        RowManager.appendLine()

    ########## Insert: Private #######
    @staticmethod
    def appendLine():
        file_full_path = ServerTools.get_file_full_path(RowManager.table_name, RowManager.db_name, "data")
        csv_handler = csvHandler(file_full_path)
        data = csv_handler.get_content()
        data.extend(RowManager.content)
        csv_handler.set_content(data)
