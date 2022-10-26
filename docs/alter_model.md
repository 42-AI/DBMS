```sql
ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype;

ALTER TABLE table_name
  CHANGE COLUMN old_name TO new_name;
```

Examples:

```sql
ALTER TABLE Customers
ADD Email varchar(255);

ALTER TABLE customers
DROP COLUMN Email;
```

```python
keyword = "ALTER TABLE"
data = {
    'NAME' = 'Customers',
    'DATA' = [
        [
            'ACTION': 'ADD',
            'VALUE': {
			    'FIELD': 'Email',
			    'TYPE': 'varchar',
			    'LENGTH': 255,
			    'NULL': True,
			    'KEY': '',
			    'DEFAULT': '',
			    'EXTRA': '',
			    'COMMENT': ''
		    }
        ],
        [
            'ACTION': 'MODIFY',
            'VALUE': {
		    	'FIELD': 'Email',
		    	'TYPE': 'varchar',
		    	'LENGTH': 30,
		    	'NULL': True,
		    	'KEY': '',
		    	'DEFAULT': '',
		    	'EXTRA': '',
		    	'COMMENT': ''
		    },
        ],
        [
            'ACTION': 'CHANGE',
            'VALUE': {
                'OLD_NAME': 'Email',
                'NEW_NAME': 'mail',
            }
        ],
        [
            'ACTION': 'DROP',
            'VALUE': {
                'NAME': 'mail',
            }
        ]
    ]
}
```
