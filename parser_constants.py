precedences = {}
precedences.update(dict.fromkeys(['*', '/', '%'], 2))
precedences.update(dict.fromkeys(['+', '-'], 3))
precedences.update(dict.fromkeys(['=', '>', '<', '>=', '<=', '<>', '!=', '!>', '!<'], 4))
precedences.update(dict.fromkeys(['NOT'], 5))
precedences.update(dict.fromkeys(['AND'], 6))
precedences.update(dict.fromkeys(['ALL', 'ANY', 'BETWEEN', 'IN', 'LIKE', 'OR', 'SOME'], 7))

keywords = {
    "SELECT": False,
    "FROM": False,
    "WHERE": False,
    "CREATE": ["DATABASE", "TABLE"],
    "DROP": ["DATABASE", "TABLE"],
    "INSERT": ["INTO"],
    "USE": False,
    "SHOW": False
}
