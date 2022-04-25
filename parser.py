import re
import sys

class ParsingNode:
    def __init__(self, keyword=None, name=None, lst=None, _next=None, previous=None):
        self.keyword = keyword
        self.name = name
        self.lst = lst
        self.next = _next
        self.previous = previous

    def __str__(self):
        ret = ""
        if self.keyword:
            ret += f"{self.keyword} "
        if self.name:
            ret += f"<{self.name}> "
        if self.lst:
            ret += f"{self.lst} "
        if self.next:
            ret += f"{self.next.__str__()} "
        return ret

class AstNode:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if self.left and self.right:
            return self.left.__str__() + self.right.__str__() + f"[{self.data}]"
        elif self.left:
            return self.left.__str__() + f"[{self.data}]"
        elif self.right:
            return self.right.__str__() + f"[{self.data}]"
        else:
            return f"[{self.data}]"

precedences = {}
precedences.update(dict.fromkeys(['*', '/', '%'], 2))
precedences.update(dict.fromkeys(['+', '-'], 3))
precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!=', '!>', '!<'], 4))
precedences.update(dict.fromkeys(['NOT'], 5))
precedences.update(dict.fromkeys(['AND'], 6))
precedences.update(dict.fromkeys(['ALL', 'ANY', 'BETWEEN', 'IN', 'LIKE', 'OR', 'SOME'], 7))


def has_greater_precedence(op1, op2):
    return precedences[op1] < precedences[op2]


def peek(stack):
    return stack[-1] if stack else None


def add_to_parsing_tree(parsingTree, keyword, lst):
    if parsingTree is None:
        parsingTree = ParsingNode(keyword, lst)
    else:
        tmp = parsingTree
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = ParsingNode(keyword, lst, previous=tmp)
    return parsingTree


def parser(txt):
    instructions = [
        [e for e in re.split('([^_@$#a-zA-Z0-9])', inst) if e not in ' \n']
        for inst in txt.upper().split(';') if inst != ''
    ]
    keywords = {
        "SELECT": False,
        "FROM": False,
        "WHERE": False,
        "CREATE": ["DATABASE", "TABLE"],
        "DROP": ["DATABASE", "TABLE"],
        "INSERT": ["INTO"],
    }
    parsingTree = None
    for input_tokens in instructions:
        while len(input_tokens) > 0:
            # print("STEP", input_tokens[0] in keywords.keys(), input_tokens)
            name = None
            if input_tokens[0] in keywords.keys():
                keyword = input_tokens[0]
                input_tokens = input_tokens[1:]
                if keyword in ["CREATE", "DROP", "INSERT"] and len(input_tokens) > 1 and input_tokens[0] in keywords[keyword]:
                    keyword += " " + input_tokens[0]
                    name = input_tokens[1]
                    input_tokens = input_tokens[2:]
                elif keyword in ["USE"] and len(input_tokens) > 0:
                    name = input_tokens[0]
                    input_tokens = input_tokens[1:]
                elif keyword in ["SHOW"] and len(input_tokens) > 0 and input_tokens[0] in keywords[keyword]:
                    keyword += " " + input_tokens[0]
                    input_tokens = input_tokens[1:]
                elif keyword == "WHERE":
                    operator_stack = []
                    output_buffer = []
                    input_tokens = input_tokens[1:]
                    while len(input_tokens) > 0 and input_tokens[0] not in keywords.keys():
                        token = input_tokens[0]
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
                    print(output_buffer)
                    parsingTree = add_to_parsing_tree(parsingTree, keyword, output_buffer)

                else:
                    lst = []
                    while len(input_tokens) > 0 and input_tokens[0] not in keywords.keys():
                        lst.append(input_tokens[0])
                        input_tokens = input_tokens[1:]
                    lst = ''.join(lst)
                    lst = ''.join(lst.split('('))
                    lst = ''.join(lst.split(')'))
                    lst = ''.join(lst.split('\''))
                    lst = lst.split(',')
                    parsingTree = add_to_parsing_tree(parsingTree, keyword, lst)
            else:
                print("parsing error", file=sys.stderr)
                return
        return parsingTree

