from configparser import ParsingError
from src.Parsing.Constants import precedences, keywords_list, data_types
from src.Parsing.ParsingNode import Node


def add_to_parsing_tree(parsingTree, new_node):
    if parsingTree is None:
        parsingTree = new_node
    else:
        tmp = parsingTree
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = new_node
    return parsingTree


class Parser:
    SyntaxErrorTxt = "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near "
    keyword_functions = {
        # "SELECT": lambda input_tokens, keyword: Parser.select_parser(input_tokens, keyword),
        "CREATE TABLE": lambda input_tokens, keyword: Parser.create_table_parser(input_tokens, keyword),
        "DROP DATABASE": lambda input_tokens, keyword: Parser.drop_db_parser(input_tokens, keyword),
        "DROP TABLE": lambda input_tokens, keyword: Parser.drop_table_parser(input_tokens, keyword),
        "INSERT INTO": lambda input_tokens, keyword: Parser.insert_parser(input_tokens, keyword),
        "CREATE DATABASE": lambda input_tokens, keyword: Parser.create_db_parser(input_tokens, keyword),
        "SHOW TABLES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "SHOW DATABASES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "USE": lambda input_tokens, keyword: Parser.use_db_parser(input_tokens, keyword),
        "DESCRIBE": lambda input_tokens, keyword: Parser.describe_parser(input_tokens, keyword),
    }

    @staticmethod
    def split_instruction(inst):
        printable_list = list(range(ord('!'), ord('~') + 1)) + \
            list(range(ord('¡'), ord('ÿ') + 1)) + [ord('€')]
        result = []
        word = ""
        quote = ""
        i = 0
        while i < len(inst):
            if inst[i] in "\"'":
                quote = inst[i]
                i += 1
                while i < len(inst) and inst[i] != quote:
                    word += inst[i]
                    i += 1
                if inst[i] == quote:
                    i += 1
                    result.append(word)
                    word = ""
                    quote = ""
            elif inst[i] in "(),=":
                result.append(inst[i])
                i += 1
            elif inst[i] in "\t\r\n ":
                i += 1
            elif ord(inst[i]) in printable_list:
                while i < len(inst) and (ord(inst[i]) in printable_list) and not (inst[i] in "\t\r\n (),=\"\'"):
                    word += inst[i]
                    i += 1
                result.append(word)
                word = ""
            else:
                raise ParsingError(f"Error: Character {inst[i]} not recognized")
        # print(result)
        return result

    @staticmethod
    def get_input_tokens_list(txt):
        tmp = [Parser.split_instruction(inst)
               for inst in txt.split(';') if inst != '']
        instructions = []
        for line in tmp:
            tokens = []
            for elem in line:
                if elem.upper() in keywords_list:
                    elem_type = "keyword"
                elif elem.upper() in precedences.keys():
                    elem_type = "operator"
                elif len(elem) == 1 and elem[0] in "()[]{}\t\n\r ,":
                    elem_type = "separator"
                elif elem.upper() in data_types.keys():
                    elem_type = "datatype"
                else:
                    elem_type = "variable"
                if elem not in "\t\n\r":
                    tokens.append([elem_type, elem])
            instructions.append(tokens)
        return instructions

    @staticmethod
    def fill_description(i_t, data):
        description = {
            "FIELD": "",
            "TYPE": "",
            "LENGTH": None,
            "NULL": True,  # ==> Nullable
            "KEY": "",
            "DEFAULT": "",
            "EXTRA": "",
            "COMMENT": "",
        }
        description['FIELD'] = i_t[0][1]
        i_t = i_t[1:]
        while not (i_t[0][0] == "separator" and i_t[0][1] == ",") and len(i_t) > 1:
            if i_t[0][1].upper() in data_types.keys():
                description["TYPE"] = i_t[0][1].upper()
                description["LENGTH"] = data_types[i_t[0][1].upper()]
                if len(i_t[1:]) > 3 and i_t[1][1] == "(" and i_t[3][1] == ")" and i_t[2][0] == "variable":
                    description["LENGTH"] = i_t[2][1]
                    i_t = i_t[3:]
            elif i_t[0][0] == "variable":
                if i_t[0][1].upper() == "AUTO_INCREMENT":
                    description["EXTRA"] = i_t[0][1]
                elif i_t[0][1].upper() == "COMMENT" and len(i_t[1:]) > 2 and i_t[1][1] == '=' and i_t[2][0] == 'variable':
                    description["COMMENT"] = i_t[2][1]
                    i_t = i_t[2:]
                elif i_t[0][1].upper() == "DEFAULT" and len(i_t) > 2 and i_t[1][0] == "variable":
                    description["DEFAULT"] = i_t[1][1]
                    i_t = i_t[1:]
                elif i_t[0][1].upper() == "PRIMARY" and len(i_t) > 2 and i_t[1][1].upper() == "KEY":
                    description["KEY"] = 'PRI'
                    i_t = i_t[1:]
                else:
                    raise ParsingError("Error while filling Description")
            elif i_t[0][1].upper() == "NOT" and len(i_t) > 2 and i_t[1][1].upper() == "NULL":
                description["NULL"] = False
                i_t = i_t[1:]
            i_t = i_t[1:]
        if i_t[0][0] != "separator":
            raise ParsingError(f"ERROR {i_t[0][1]} is not a separator")
        data["DESCRIPTION"].append(description)
        if i_t[0][1] == ",":
            i_t = i_t[1:]
        elif i_t[0][1] != ")":
            raise ParsingError(f"ERROR {i_t[0][1]} is not a valid separator")
        return i_t, data

    @staticmethod
    def create_table_parser(input_tokens, keyword):
        if input_tokens[0][0] != "variable":
            raise ParsingError(f"{Parser.SyntaxErrorTxt}'{input_tokens[0][1]}'")
        data = {
            "NAME": input_tokens[0][1],
            "DESCRIPTION": []
        }
        input_tokens = input_tokens[1:]
        brackets_stack = []
        while input_tokens and len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            i_t = input_tokens
            if i_t[0][0] == "separator" and i_t[0][1] == "(":
                brackets_stack.append(i_t[0][1])
                i_t = i_t[1:]
            elif i_t[0][0] == "variable" and len(i_t[1:]) > 1:
                i_t, data = Parser.fill_description(i_t, data)
            if i_t and i_t[0][1] == ")":
                i_t = i_t[1:]
            input_tokens = i_t

        return input_tokens, Node(keyword=keyword, data=data)

    @staticmethod
    def fill_insert_header(input_tokens):
        header = []
        while input_tokens and len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            i_t = input_tokens
            if i_t[0][0] == "variable" and len(i_t[1:]) > 1:
                header.append(i_t[0][1])
            input_tokens = i_t[1:]
        if input_tokens[0][1].upper() != "VALUES":
            raise ParsingError("Parsing Error: keyword VALUES missing")
        else:
            input_tokens = input_tokens[1:]
        return header, input_tokens

    @staticmethod
    def fill_insert_data(header, data, input_tokens):
        brackets_stack = []
        tmp = []
        while input_tokens and len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            i_t = input_tokens
            if i_t[0][1] == "(":
                brackets_stack.append(i_t[0][1])
            elif i_t[0][0] == "variable":
                tmp.append(i_t[0][1])
            elif i_t and i_t[0][1] == ")":
                # brackets_stack.append(i_t[0][1])
                if len(tmp) != len(header):
                    raise ParsingError(f"Header length different form line length.")
                else:
                    dic = dict([(h, d) for h, d in zip(header, tmp)])
                    data["DATA"].append(dic)
                tmp = []
            elif i_t[0][0] == "separator":
                pass
            else:
                raise ParsingError(f"character {input_tokens[0][1]} not recognized.")
            input_tokens = i_t[1:]
        return data, input_tokens

    @staticmethod
    def insert_parser(input_tokens, keyword):
        if input_tokens[0][0] != "variable":
            raise ParsingError(f"{Parser.SyntaxErrorTxt}'{input_tokens[0][1]}'")
        data = {
            "NAME": input_tokens[0][1],
            "DATA": []
        }
        input_tokens = input_tokens[1:]
        header, input_tokens = Parser.fill_insert_header(input_tokens)
        data, input_tokens = Parser.fill_insert_data(header, data, input_tokens)

        return input_tokens, Node(keyword=keyword, data=data)

    @staticmethod
    def simple_parser(input_tokens, keyword):
        if input_tokens[0][0] != "variable":
            raise ParsingError(f"{Parser.SyntaxErrorTxt}'{input_tokens[0][1]}'")
        name = input_tokens[0][1]
        input_tokens = input_tokens[1:]
        return input_tokens, Node(keyword=keyword, data=name)

    @staticmethod
    def drop_table_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)

    @staticmethod
    def drop_db_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)

    @staticmethod
    def use_db_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)

    @staticmethod
    def describe_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)

    @staticmethod
    def create_db_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)

    @staticmethod
    def show_parser(input_tokens, keyword):
        return input_tokens, Node(keyword=keyword)

    @staticmethod
    def pretty_print(txt, array):
        print("========================", file=sys.stderr)
        print(txt, file=sys.stderr)
        for index, line in enumerate(array):
            print(f"Line {index}:", file=sys.stderr)
            for elem in line:
                print(elem, file=sys.stderr)
        print("========================", file=sys.stderr)

    @staticmethod
    def concat_keywords(input_tokens):
        # concat group of keyword (ex: "CREATE TABLE", "SHOW DATABASES"...)
        keyword = ""
        while len(input_tokens) > 0 and input_tokens[0][0] == "keyword":
            keyword += " " + input_tokens[0][1]
            input_tokens = input_tokens[1:]
        keyword = keyword.strip()
        return keyword, input_tokens

    @staticmethod
    def print_node(node):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", file=sys.stderr)
        print("KEYWORD:", node.keyword, file=sys.stderr)
        print("DATA:", node.data, file=sys.stderr)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", file=sys.stderr)

    @staticmethod
    def parser(txt):
        instructions = Parser.get_input_tokens_list(txt)
        Parser.pretty_print("INSTRUCTIONS:", instructions)
        parsingTree = None
        for input_tokens in instructions:
            while input_tokens and len(input_tokens) > 0:
                keyword, input_tokens = Parser.concat_keywords(input_tokens)

                if keyword != "":
                    input_tokens, new_node = Parser.keyword_functions[keyword.upper()](
                        input_tokens, keyword)
                    Parser.print_node(new_node)
                    parsingTree = add_to_parsing_tree(parsingTree, new_node)
                else:
                    raise ParsingError("Error in Parser function")
        return parsingTree
