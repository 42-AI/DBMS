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
            ret += f"{self.name} "
        if self.lst:
            ret += f"{self.lst} "
        if self.next:
            ret += f"{self.next.__str__()} "
        return ret

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
        "USE": False,
        "SHOW": ["DATABASES", "TABLES"]
    }
    parsingTree = None
    for each in instructions:
        while len(each) > 0:
            # print("STEP", each[0] in keywords.keys(), each)
            name = None
            if each[0] in keywords.keys():
                keyword = each[0]
                each = each[1:]
                if keyword in ["CREATE", "DROP", "INSERT"] and len(each) > 1 and each[0] in keywords[keyword]:
                    keyword += " " + each[0]
                    name = each[1]
                    each = each[2:]
                elif keyword in ["USE"] and len(each) > 0:
                    name = each[0]
                    each = each[1:]
                elif keyword in ["SHOW"] and len(each) > 0 and each[0] in keywords[keyword]:
                    keyword += " " + each[0]
                    each = each[1:]
                lst = []
                while len(each) > 0 and each[0] not in keywords.keys():
                    lst.append(each[0])
                    each = each[1:]
                lst = ''.join(lst)
                lst = ''.join(lst.split('('))
                lst = ''.join(lst.split(')'))
                lst = ''.join(lst.split('\''))
                lst = lst.split(',')
                if parsingTree is None:
                    parsingTree = ParsingNode(keyword=keyword, name=name, lst=lst)
                else:
                    tmp = parsingTree
                    while tmp.next is not None:
                        tmp = tmp.next
                    tmp.next = ParsingNode(keyword=keyword, name=name, lst=lst, previous=tmp)
            else:
                print("parsing error", file=sys.stderr)
                return
        # print("END RESULT:", parsingTree)
        return parsingTree

