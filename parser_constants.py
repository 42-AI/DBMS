precedences = {}
precedences.update(dict.fromkeys(['*', '/', '%'], 2))
precedences.update(dict.fromkeys(['+', '-'], 3))
precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!='], 4))
# precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!=', '!>', '!<'], 4))
precedences.update(dict.fromkeys(['NOT'], 5))
precedences.update(dict.fromkeys(['AND'], 6))
precedences.update(dict.fromkeys(['OR'], 7))
# precedences.update(dict.fromkeys(['ALL', 'ANY', 'BETWEEN', 'IN', 'LIKE', 'OR', 'SOME', 'IS'], 7))

keywords = {
    "SELECT": None, # [None, "DISTINCT"], ??
    "FROM": None,
    "WHERE": None,
    "CREATE": ["DATABASE", "TABLE"],
    "INSERT": ["INTO"],
    "DROP": ["DATABASE", "TABLE"],
    "USE": None,
    "SHOW": ["DATABASES", "TABLES"],
    "DESCRIBE": None,
    "ALTER": ["TABLE"],
}

keywords_list = [
    "SELECT",
    "FROM",
    "WHERE",
    "CREATE",
    "DATABASE",
    "DATABASES",
    "TABLE",
    "TABLES",
    "DROP",
    "INSERT",
    "INTO",
    "USE",
    "SHOW",
    "DEFAULT",
    "DESCRIBE",
    "ALTER",
    "DISTINCT",
]

datatypes = [
    "INT",
    "INTEGER", # synonym for INT
    # "TINYINT",
    # "BOOL",
    # "FLOAT",
    "REAL", # synonym of DOUBLE => real(6 digits for precision)
    # "DATE",
    # "DATETIME",
    # "TIMESTAMP",
    "CHAR", # char(n)
    "VARCHAR", # varchar(n)
    # "TEXT",
]