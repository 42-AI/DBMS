from src.Server.FileSystemManager import FileSystemManager as fsm


class Show:
    @staticmethod
    def print_content(title, lst):
        m = len(max(lst, key=len))
        print(f"+{'-'* (max([m, len(title)]) + 2)}+")
        print(f"| {title: <{m}} |")
        print(f"+{'-'* (max([m, len(title)]) + 2)}+")
        for elem in lst:
            print(f"| {elem: <{max([m, len(title)])}} |")
        print(f"+{'-'* (max([m, len(title)]) + 2)}+")
        print(f"{len(lst) + 4} rows in set\n")

    @staticmethod
    def databases():
        dbs = fsm.get_dbs()
        if dbs is not None:
            Show.print_content("Database", dbs)

    @staticmethod
    def tables(db_name):
        if db_name is not None:
            tables = fsm.get_tables(db_name)
            if tables is not None:
                Show.print_content("Tables_in_" + db_name.lower(), tables)
