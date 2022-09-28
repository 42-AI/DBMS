class RowValidator:

    @staticmethod

    @staticmethod
    def valid_insert(db_name: str, table_name: str, content):
        RowManager.db_name = db_name
        RowManager.table_name = table_name
        RowManager.content = content

    @staticmethod
    def valid_input():
        