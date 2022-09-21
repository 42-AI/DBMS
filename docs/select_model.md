```text
Ponctuation: '()', ',', ';', '+' -- le + pour les concatenation dans les alias aussi
OPERATEURS: < > <= >= = <> != 
LOGICAL: AND, OR
```

SELECT (DISTINCT) value AS alias,
                  value + '_' + value AS alias
FROM TABLE AS t1
WHERE ...

```sql
SELECT e.last_name      AS name,
       e.commission_pct comm,
       e.salary * 12    "Annual Salary"
FROM   employees AS e
WHERE  e.salary > 1000
ORDER  BY
  e.first_name,
  e.last_name;
```

```python
keyword = "SELECT DISTINCT",
data = {
    "COLUMNS": [
        {
            "fullname": "e.last_name",
            "prefix":   "e",
            "alias":    "name",
        },
        {
            "fullname": "e.commission_pct",
            "prefix":   "e",
            "alias":    "comm",
        },
        {
            "fullname": "e.salary * 12",
            "prefix":   "e",
            "alias":    "Annual Salary",
        },
    ],
    "FROM": [
        {
            "TABLE": "employees",
            "tablealias": "e",
        },
    ],
    "WHERE": [
        "e.salary > 1000"
    ],
    "ORDER BY": [
        "e.first_name",
        "e.last_name",
    ],
}
```