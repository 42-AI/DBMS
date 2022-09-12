import re
import sys
from parser_constants import precedences, keywords_list, data_types
from ParsingNode import Node


def has_greater_precedence(op1, op2):
    return precedences[op1] < precedences[op2]


def peek(stack):
    return stack[-1] if stack else None


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
    keyword_functions = {
        # "SELECT": lambda input_tokens, keyword: Parser.select_parser(input_tokens, keyword),
        # "FROM": lambda input_tokens, keyword: Parser.from_parser(input_tokens, keyword),
        # "WHERE": lambda input_tokens, keyword: Parser.where_parser(input_tokens, keyword),
        "CREATE TABLE": lambda input_tokens, keyword: Parser.create_table_parser(input_tokens, keyword),
        "DROP DATABASE": lambda input_tokens, keyword: Parser.drop_db_parser(input_tokens, keyword),
        "DROP TABLE": lambda input_tokens, keyword: Parser.drop_table_parser(input_tokens, keyword),
        # "INSERT INTO": lambda input_tokens, keyword: Parser.insert_parser(input_tokens, keyword),
        "CREATE DATABASE": lambda input_tokens, keyword: Parser.create_db_parser(input_tokens, keyword),
        "SHOW TABLES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "SHOW DATABASES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "USE": lambda input_tokens, keyword: Parser.use_db_parser(input_tokens, keyword),
    }

    @staticmethod
    def get_input_tokens_list(txt):
        tmp = [
            [e for e in re.split(
                '("[ !#-&(-~]*"|\'[ !#-&(-~]*\'|[^_@$#a-zA-Z0-9])', inst) if e not in ' \n']
            for inst in txt.upper().split(';') if inst != ''
        ]
        instructions = []
        for line in tmp:
            tokens = []
            for elem in line:
                if elem in keywords_list:
                    elem_type = "keyword"
                elif elem in precedences.keys():
                    elem_type = "operator"
                elif len(elem) == 1 and elem[0] in "()[]\{\}\t\n\r ,":
                    elem_type = "separator"
                elif elem in data_types.keys():
                    elem_type = "datatype"
                else:
                    elem_type = "variable"
                if elem not in "\t\n\r":
                    tokens.append([elem_type, elem])
            instructions.append(tokens)
        return instructions

    # @staticmethod
    # def select_parser(input_tokens, keyword):
    #     while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
    #         lst.append(input_tokens[0][1])
    #         input_tokens = input_tokens[1:]
    #     lst = ''.join(lst)
    #     lst = ''.join(lst.split('('))
    #     lst = ''.join(lst.split(')'))
    #     lst = ''.join(lst.split('\''))
    #     lst = lst.split(',')
    #     return (input_tokens, keyword)
    # @staticmethod
    # def from_parser(input_tokens, keyword):
    #     while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
    #         lst.append(input_tokens[0][1])
    #         input_tokens = input_tokens[1:]
    #     lst = ''.join(lst)
    #     lst = ''.join(lst.split('('))
    #     lst = ''.join(lst.split(')'))
    #     lst = ''.join(lst.split('\''))
    #     lst = lst.split(',')
    #     return (input_tokens, keyword)
    # @staticmethod
    # def where_parser(input_tokens, keyword):
    #     operator_stack = []
    #     output_buffer = []
    #     input_tokens = input_tokens[1:]
    #     # Shuting yard algorithm => convert expression to RPN
    #     while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
    #         token = input_tokens[0][1]
    #         if token in precedences.keys():
    #             top = peek(operator_stack)
    #             while top is not None and top != '(' and not has_greater_precedence(token, top):
    #                 y = operator_stack.pop()
    #                 output_buffer.append(y)
    #                 top = peek(operator_stack)
    #             operator_stack.append(token)
    #         elif token == '(':
    #             operator_stack.append(token)
    #         elif token == ')':
    #             top = peek(operator_stack)
    #             while top is not None and top != '(':
    #                 output_buffer.append(operator_stack.pop())
    #                 top = peek(operator_stack)
    #             if operator_stack[0] == '(':
    #                 operator_stack.pop()
    #         else:
    #             output_buffer.append(token)
    #     while len(operator_stack) > 0:
    #         output_buffer.append(operator_stack.pop())
    #     lst = output_buffer
    #     return (input_tokens, keyword)
    # @staticmethod
    # def drop_parser(input_tokens, keyword):
    #     if len(input_tokens) > 1 and input_tokens[0][0] == "keyword":
    #         keyword += " " + input_tokens[0][1]
    #         name = input_tokens[1][1]
    #         input_tokens = input_tokens[2:]
    #     print("NAME:", name)
    #     return (input_tokens, keyword)
    # @staticmethod
    # def insert_parser(input_tokens, keyword):
    #     if len(input_tokens) > 1 and input_tokens[0] in keywords[keyword]:
    #         keyword += " " + input_tokens[0]
    #         name = input_tokens[1]
    #         input_tokens = input_tokens[2:]
    #     return (input_tokens, keyword)

    @staticmethod
    def fill_description(i_t, data):
        description = {
            "FIELD": "",
            "TYPE": "",
            "LENGTH": None,
            "NULL": True,  # ==> NOT NULL
            "KEY": "",
            "DEFAULT": "",
            "EXTRA": "",
            "COMMENT": "",
        }
        description['FIELD'] = i_t[0][1]
        i_t = i_t[1:]
        while not (i_t[0][0] == "separator" and i_t[0][1] == ",") and len(i_t) > 1:
            if i_t[0][0] == "datatype" and i_t[0][1] in data_types.keys():
                description["TYPE"] = i_t[0][1]
                description["LENGTH"] = data_types[i_t[0][1]]
                if len(i_t[1:]) > 3 and i_t[1][1] == "(" and i_t[3][1] == ")" and i_t[2][0] == "variable":
                    description["LENGTH"] = i_t[2][1]
                    i_t = i_t[3:]
            elif i_t[0][0] == "variable":
                if i_t[0][1] == "AUTO_INCREMENT":
                    description["EXTRA"] = i_t[0][1]
                elif i_t[0][1] == "COMMENT" and len(i_t[1:]) > 2 and i_t[1][1] == '=' and i_t[2][0] == 'variable':
                    c = i_t[2][1].split('"')
                    if (len(c) == 3):
                        description["COMMENT"] = c[1]
                    else:
                        return None, None
                    i_t = i_t[2:]
                elif i_t[0][1] == "DEFAULT" and len(i_t) > 2 and i_t[1][0] == "variable":
                    description["DEFAULT"] = i_t[1][1]
                    i_t = i_t[1:]
                else:
                    print("ERROR WHILE FILLING DESCRIPTION")
                    return None, None
            elif i_t[0][1] == "NOT" and len(i_t) > 2 and i_t[1][1] == "NULL":
                description["NULL"] = False
                i_t = i_t[1:]
            i_t = i_t[1:]
        if i_t[0][0] != "separator":
            print(f"ERROR {i_t[0][1]} is not a separator")
            return None, None
        data["DESCRIPTION"].append(description)
        if i_t[0][1] == ",":
            i_t = i_t[1:]
        else:
            print(f"ERROR {i_t[0][1]} is not a valid separator")
            return None, None
        return i_t, data

    @staticmethod
    def create_table_parser(input_tokens, keyword):
        # print("INSIDE CREATE TABLE PARSER")
        if input_tokens[0][0] != "variable":
            # print("RETURN 1")
            return None, None
        data = {
            "NAME": input_tokens[0][1],
            "DESCRIPTION": []
        }
        input_tokens = input_tokens[1:]
        brackets_stack = []
        while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            i_t = input_tokens
            if i_t[0][0] == "separator" and i_t[0][1] == "(":
                brackets_stack.append(i_t[0][1])
                i_t = i_t[1:]
            elif i_t[0][0] == "variable" and len(i_t[1:]) > 1:
                # call to fill description
                i_t, data = Parser.fill_description(i_t, data)
            if i_t[0][1] == ")":
                i_t = i_t[1:]
            input_tokens = i_t

        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(data)
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return input_tokens, Node(keyword=keyword, data=data)

    @staticmethod
    def simple_parser(input_tokens, keyword):
        if input_tokens[0][0] != "variable":
            return
        db_name = input_tokens[0][1]
        input_tokens = input_tokens[1:]
        return input_tokens, Node(keyword=keyword, data=db_name)

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
    def create_db_parser(input_tokens, keyword):
        return Parser.simple_parser(input_tokens, keyword)
        

    @staticmethod
    def show_parser(input_tokens, keyword):
        return input_tokens, Node(keyword=keyword)

    @staticmethod
    def pretty_print(txt, array):
        print("========================")
        print(txt)
        for index, line in enumerate(array):
            print(f"Line {index}:")
            for elem in line:
                print(elem)
        print("========================")

    @staticmethod
    def parser(txt):
        instructions = Parser.get_input_tokens_list(txt)
        # Parser.pretty_print("INSTRUCTIONS:", instructions)
        parsingTree = None
        for input_tokens in instructions:
            while len(input_tokens) > 0:
                # print(input_tokens)

                # concat group of keyword (ex: "CREATE TABLE", "SHOW DATABASES"...)
                keyword = ""
                while len(input_tokens) > 0 and input_tokens[0][0] == "keyword":
                    keyword += " " + input_tokens[0][1]
                    input_tokens = input_tokens[1:]
                keyword = keyword.strip()
                # print("==", keyword, input_tokens)

                if keyword != "":
                    input_tokens, new_node = Parser.keyword_functions[keyword](
                        input_tokens, keyword)
                    parsingTree = add_to_parsing_tree(parsingTree, new_node)
                else:
                    print("parsing error", file=sys.stderr)
                    return
            return parsingTree
