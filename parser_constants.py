precedences = {}
precedences.update(dict.fromkeys(['*', '/', '%'], 2))
precedences.update(dict.fromkeys(['+', '-'], 3))
precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!=', '!>', '!<'], 4))
precedences.update(dict.fromkeys(['NOT'], 5))
precedences.update(dict.fromkeys(['AND'], 6))
precedences.update(dict.fromkeys(['ALL', 'ANY', 'BETWEEN', 'IN', 'LIKE', 'OR', 'SOME', 'IS'], 7))

keywords = {
    "SELECT": None,
    "FROM": None,
    "WHERE": None,
    "CREATE": ["DATABASE", "TABLE"],
    "INSERT": ["INTO"],
    "DROP": ["DATABASE", "TABLE"],
    "USE": None,
    "SHOW": ["DATABASES", "TABLES"],
}

keywords_list = [
    "SELECT",
    "FROM",
    "WHERE",
    "CREATE",
    "DATABASE",
    "TABLE",
    "DROP",
    "INSERT",
    "INTO",
    "USE",
    "SHOW",
    "DATABASES",
    "TABLES",
    "DEFAULT",
]

datatypes = [
    "INT",
    "TINYINT",
    "BOOL",
    "FLOAT",
    "DATE",
    "DATETIME",
    "TIMESTAMP",
    "CHAR",
    "VARCHAR",
    "TEXT",
]