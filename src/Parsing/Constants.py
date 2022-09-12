precedences = {}
precedences.update(dict.fromkeys(['*', '/', '%'], 2))
precedences.update(dict.fromkeys(['+', '-'], 3))
precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!='], 4))
# precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!=', '!>', '!<'], 4))
precedences.update(dict.fromkeys(['NOT'], 5))
precedences.update(dict.fromkeys(['AND'], 6))
precedences.update(dict.fromkeys(['OR'], 7))
# precedences.update(dict.fromkeys(['ALL', 'ANY', 'BETWEEN', 'IN', 'LIKE', 'OR', 'SOME', 'IS'], 7))

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
    "DESCRIBE",
    "ALTER",
    "DISTINCT",
]

data_types = {
    "INT": 11,
    "INTEGER": 11,
    "REAL": 37,
    "CHAR": 255,
    "VARCHAR": 255,
}
