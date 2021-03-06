import re
import sys
from parser_constants import keywords, precedences, keywords_list, datatypes
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
        # "CREATE TABLE": lambda input_tokens, keyword: Parser.create_parser(input_tokens, keyword),
        # "DROP DATABASE": lambda input_tokens, keyword: Parser.drop_parser(input_tokens, keyword),
        # "DROP TABLE": lambda input_tokens, keyword: Parser.drop_parser(input_tokens, keyword),
        # "INSERT INTO": lambda input_tokens, keyword: Parser.insert_parser(input_tokens, keyword),
        "CREATE DATABASE": lambda input_tokens, keyword: Parser.use_create_database_parser(input_tokens, keyword),
        "SHOW TABLES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "SHOW DATABASES": lambda input_tokens, keyword: Parser.show_parser(input_tokens, keyword),
        "USE": lambda input_tokens, keyword: Parser.use_create_database_parser(input_tokens, keyword),
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
                elif elem in datatypes:
                    elem_type = "datatype"
                else:
                    elem_type = "variable"
                tokens.append([elem_type, elem])
            instructions.append(tokens)
        return instructions

    @staticmethod
    def select_parser(input_tokens, keyword):
        while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            lst.append(input_tokens[0][1])
            input_tokens = input_tokens[1:]
        lst = ''.join(lst)
        lst = ''.join(lst.split('('))
        lst = ''.join(lst.split(')'))
        lst = ''.join(lst.split('\''))
        lst = lst.split(',')
        return (input_tokens, keyword)

    @staticmethod
    def from_parser(input_tokens, keyword):
        while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            lst.append(input_tokens[0][1])
            input_tokens = input_tokens[1:]
        lst = ''.join(lst)
        lst = ''.join(lst.split('('))
        lst = ''.join(lst.split(')'))
        lst = ''.join(lst.split('\''))
        lst = lst.split(',')
        return (input_tokens, keyword)

    @staticmethod
    def where_parser(input_tokens, keyword):
        operator_stack = []
        output_buffer = []
        input_tokens = input_tokens[1:]
        # Shuting yard algorithm => convert expression to RPN
        while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
            token = input_tokens[0][1]
            if token in precedences.keys():
                top = peek(operator_stack)
                while top is not None and top != '(' and not has_greater_precedence(token, top):
                    y = operator_stack.pop()
                    output_buffer.append(y)
                    top = peek(operator_stack)
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                top = peek(operator_stack)
                while top is not None and top != '(':
                    output_buffer.append(operator_stack.pop())
                    top = peek(operator_stack)
                if operator_stack[0] == '(':
                    operator_stack.pop()
            else:
                output_buffer.append(token)
        while len(operator_stack) > 0:
            output_buffer.append(operator_stack.pop())
        lst = output_buffer
        return (input_tokens, keyword)

    @staticmethod
    def drop_parser(input_tokens, keyword):
        if len(input_tokens) > 1 and input_tokens[0][0] == "keyword":
            keyword += " " + input_tokens[0][1]
            name = input_tokens[1][1]
            input_tokens = input_tokens[2:]
        print("NAME:", name)
        return (input_tokens, keyword)

    @staticmethod
    def insert_parser(input_tokens, keyword):
        if len(input_tokens) > 1 and input_tokens[0] in keywords[keyword]:
            keyword += " " + input_tokens[0]
            name = input_tokens[1]
            input_tokens = input_tokens[2:]
        return (input_tokens, keyword)

    @staticmethod
    def create_table_parser(input_tokens, keyword):
        if len(input_tokens) > 1 and input_tokens[0][0] == "keyword":
            keyword += " " + input_tokens[0][0]
            name = input_tokens[1][1]
            input_tokens = input_tokens[2:]
        if keyword == "CREATE TABLE":
            while len(input_tokens) > 0 and input_tokens[0][0] != "keyword":
                lst.append(input_tokens[0][1])
                input_tokens = input_tokens[1:]
            lst = ''.join(lst)
            lst = ''.join(lst.split('('))
            lst = ''.join(lst.split(')'))
            lst = ''.join(lst.split('\''))
            lst = lst.split(',')
        return (input_tokens, keyword)

    @staticmethod
    def use_create_database_parser(input_tokens, keyword):
        if input_tokens[0][0] != "variable":
            return
        db_name = input_tokens[0][1]
        input_tokens = input_tokens[1:]
        return input_tokens, Node(keyword=keyword, db_name=db_name)

    @staticmethod
    def show_parser(input_tokens, keyword):
        return input_tokens, Node(keyword=keyword)

    @staticmethod
    def parser(txt):
        instructions = Parser.get_input_tokens_list(txt)
        print("INSTRUCTIONS:", instructions)
        parsingTree = None
        for input_tokens in instructions:
            while len(input_tokens) > 0:
                print(input_tokens)
                # concat group of keyword (ex: "CREATE TABLE", "SHOW DATABASES"...)
                keyword = ""
                while len(input_tokens) > 0 and input_tokens[0][0] == "keyword":
                    keyword += " " + input_tokens[0][1]
                    input_tokens = input_tokens[1:]
                keyword = keyword.strip()
                print("==", keyword, input_tokens)
                if keyword != "":
                    input_tokens, new_node = Parser.keyword_functions[keyword](input_tokens, keyword)
                    parsingTree = add_to_parsing_tree(parsingTree, new_node)
                else:
                    print("parsing error", file=sys.stderr)
                    return
            return parsingTree
