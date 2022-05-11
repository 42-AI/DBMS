class Node:
    def __init__(self):
        pass


class keywordNode(Node):
    def __init__(self, keyword=None):
        self.keyword = keyword

class SelectStatementNode(keywordNode):
    def __init__(self, selectClause=None, fromClause=None, whereClause=None, orderByClause=None):
        self.keyword = "SELECT"
        self.selectClause = selectClause
        self.fromClause = fromClause
        self.whereClause = whereClause
        self.orderByClause = orderByClause

class InsertStatementNode(keywordNode):
    def __init__(self, table=None, columns=[], values=[]):
        self.keyword = "INSERT"
        self.table = table
        self.columns = columns
        self.values = values

class UpdateStatement(keywordNode):
    def __init__(self, table=None, setClause=None, whereClause=None):
        self.keyword = "UPDATE"
        self.table = table
        self.setClause = setClause
        self.whereClause = whereClause

class DeleteStatement(keywordNode):
    def __init__(self, table=None, setClause=None, whereClause=None):
        self.keyword = "DELETE"
        self.table = table
        self.setClause = setClause
        self.whereClause = whereClause


class OperatorNode(Node):
    def __init__(self, operator=None):
        self.operator = operator

class VariableNode(Node):
    def __init__(self, variable=None):
        self.variable = variable
        

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