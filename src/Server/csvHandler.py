from get_project_root import root_path

class test:

    @staticmethod
    def path():
        print(root_path(ignore_cwd=False))

    @staticmethod
    def rel():
        print(pwd)