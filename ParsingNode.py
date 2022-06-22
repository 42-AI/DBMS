# for:
#  - SHOW (DATABASES OR TABLES)
class Node:
    def __init__(self, keyword=None, db_name=None, _next=None, previous=None):
        self.keyword = keyword
        self.db_name = db_name
        self.next = _next
        self.previous = previous

    def __str__(self):
        ret = ""
        if self.keyword:
            ret += f"{self.keyword} "
        if self.next:
            ret += f"{self.next.__str__()} "
        return ret

class CreateTableStatementNode(Node):
    # columns == list of {name: "", type: "", null?: False, default?: None } objects
    def __init__(self, keyword=None, db_name=None, tableName=None, columns=[]):
        super().__init__(keyword)
        self.tableName = tableName
        self.columns = ""

# class SelectStatementNode(Node):
#     def __init__(self, selectClause=None, fromClause=None, whereClause=None, orderByClause=None):
#         self.keyword = "SELECT"
#         self.selectClause = selectClause
#         self.fromClause = fromClause
#         self.whereClause = whereClause
#         self.orderByClause = orderByClause

# class SelectClauseNode():
#     def __init__(self, columnsList = []):
#         self.columnsList = columnsList
    # columnsList = { fullName: "", prefix: "", column: "", alias: ""}


# class InsertStatementNode(Node):
#     def __init__(self, table=None, columns=[], values=[]):
#         self.keyword = "INSERT"
#         self.table = table
#         self.columns = columns
#         self.values = values

# class UpdateStatement(Node):
#     def __init__(self, table=None, setClause=None, whereClause=None):
#         self.keyword = "UPDATE"
#         self.table = table
#         self.setClause = setClause
#         self.whereClause = whereClause

# class DeleteStatement(Node):
#     def __init__(self, table=None, setClause=None, whereClause=None):
#         self.keyword = "DELETE"
#         self.table = table
#         self.setClause = setClause
#         self.whereClause = whereClause

# class TreeNode():
#     keyword: str
#     children: List[TreeNode] = []

# class keyword(TreeNode, keyword, input):
    # get_children("select", input)

    # obj:
    #       name = SELECT / CREATE TABLE / CREATE DATABASE / SHOW DATABASE / WHERE...
    #       type = keyword / operator / variable / separator
    #       statment = "*" / list of objects 
            # self.next = {
            #     'FROM': None,
            #     'WHERE': None,
            #     'VALUES': None,
            # }
    #       self.FROM = obj
    #       self.WHERE = NONE


# class OperatorNode(Node):
#     def __init__(self, operator=None):
#         self.operator = operator

# class VariableNode(Node):
#     def __init__(self, variable=None):
#         self.variable = variable
        

# class ParsingNode:
#     def __init__(self, keyword=None, name=None, lst=None, _next=[], previous=None):
#         self.keyword = keyword
#         self.name = name
#         self.lst = lst
#         self.next = _next
#         self.previous = previous

#     def __str__(self):
#         ret = ""
#         if self.keyword:
#             ret += f"{self.keyword} "
#         if self.name:
#             ret += f"<{self.name}> "
#         if self.lst:
#             ret += f"{self.lst} "
#         if self.next:
#             ret += f"{self.next.__str__()} "
#         return ret