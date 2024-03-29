from get_project_root import root_path


class csvHandler:

    def __init__(self, file_full_path, separator=',', header=None, content=None):
        #self._file_path_is_valide(file_full_path)  # raise exception
        self.raw_data = ""
        self._separator = separator
        self._file_full_path = file_full_path
        if header is None:
            self._get_header_from_file()
        else:
            self._header = header
        if content is None:
            self._get_content_from_file()
        else:
            self._content = content

    def __del__(self):
        self._store_data_in_file()

    ################# Public: Get ####################

    def get_content(self):
        return self._content

    ################# Public: set ####################

    def set_content(self, content):
        self._content = content

    ################# Private: Get ####################

    def _get_row_data(self):
        with open(self._file_full_path, "r") as file:
            self.raw_data = file.readlines()
            file.close()

    def _get_header_from_file(self):
        if len(self.raw_data) == 0:
            self._get_row_data()
        if len(self.raw_data) > 0:
            self._header = self.raw_data[0].replace('\n', '').split(self._separator)

    def _get_content_from_file(self):
        if len(self.raw_data) == 0:
            self._get_row_data()
        raw_data = self.raw_data
        if len(raw_data) > 1:
            raw_data.pop(0)
            self._content = self._get_content(raw_data)
        else:
            self._content = []

    def _get_content(self, raw_content):
        content = []
        header = self._header
        for line in raw_content:
            row = {}
            row_data = line.replace('\n', '').split(self._separator)
            i = 0
            for field in row_data:
                row[header[i]] = field
                i += 1
            content.append(row)
        return content

    ############## Private: Store #####################

    def _store_data_in_file(self):
        data = ''
        data += self._separator.join(str(x) for x in self._header) + '\n'
        for array_line in self._content:
            str_line = ''
            for field in self._header:
                if field in array_line.keys():
                    str_line += str(array_line[field])
                str_line += ','
            data += str_line[:-1] + '\n'
        with open(self._file_full_path, "w") as file:
            file.write(data[:-1])
            file.close()
