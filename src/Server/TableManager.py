class TableManager:

    db_name = ''
    table_name = ''
    table_description = ''
    meta_description = TableManager.table_description[0].keys()

########## Creation: Public #######
    @staticmethod
    def create_table(table_name: str, db_name: str, table_description: array):
        TableManager.db_name = db_name
        TableManager.table_name = table_name
        TableManager.table_description = table_description
        TableManager._create_table_file()
        TableManager._create_meta_table_file()



######### Creaton: Private ########
    @staticmethod
    def _create_table_file():
        table_fields = TableManager._get_table_fields();
        return TableManager.create_file(TableManager.table_name, TableManager.db_name, table_fields)

    @staticmethod
    def _create_meta_table_file():
        meta_tabel_name = "meta" + TableManager.table_name
        meta_description = TableManager._get_meta_description
        meta_content = TableManager._get_meta_content
        return TableManager.create_file(meta_tabel_name, TableManager.db_name, f"{meta_description}\n{meta_content}")

    @staticmethod
    def _create_file(file_name: str, dir_name: str, file_content: str):
        file_fullPath = FileSystemManager._get_file_fullPath(dir_name, file_name)
        if path.exists(file_fullPath):
            print(f"Error: table {file_name} already exists.", file=sys.stderr)
            return
        if not path.isdir(path.expanduser(FileSystemManager._get_dir_fullPath(db_name))):
            print(f"Error: database {dir_name} doesn't exists.", file=sys.stderr)
            return
        f = open(file_name, "x")
        f.write(file_content)
        f.close()
        return file_fullPath

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
                field_meta += field[meta_field] + ','
            meta_content += field_meta[:-1] + '\n'
        return meta_content[:-1]



    @staticmethod
    def drop_table_file(table_name: str, db_name: str):
        table_fullPath = FileSystemManager._get_file_fullPath(table_name, db_name)
        db_fullPath = FileSystemManager._get_dir_fullPath(db_name)
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

    @staticmethod
    def get_tables(db_name):
        dir_list = os.listdir(os.getcwd())
        if _MAIN_PATH_NAME not in dir_list:
            print(f"{colors.BOLD}Empty set{colors.ENDC}")
            return
        return os.listdir(FileSystemManager._get_dir_fullPath(db_name))

