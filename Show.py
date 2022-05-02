from FileSystemManager import FileSystemManager as fsm


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
        Show.print_content("Database", fsm.get_dbs())

    @staticmethod
    def tables(db_name):
        Show.print_content("Tables_in_" + db_name.lower(), fsm.get_tables(db_name))
