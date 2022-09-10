```sql
create table customers
(
	customer_id  int AUTO_INCREMENT comment="This is a random comment",
	first_name	char(32) NOT NULL,
	last_name	char(32),
	status		int DEFAULT 1,
	comment		varchar(255),
);
```

new node:

```python
keyword = "CREATE TABLE",
data = {
	'NAME': 'CUSTOMERS',
	'DESCRIPTION': [
		{
			'FIELD': 'CUSTOMER_ID',
			'TYPE': 'INT',
			'LENGTH': 11,
			'NULL': True,
			'KEY': '',
			'DEFAULT': '',
			'EXTRA': 'AUTO_INCREMENT',
			'COMMENT': '"THIS IS A RANDOM COMMENT"'
		},
		{
			'FIELD': 'FIRST_NAME',
			'TYPE': 'CHAR',
			'LENGTH': '32',
			'NULL': False,
			'KEY': '',
			'DEFAULT': '',
			'EXTRA': '',
			'COMMENT': ''
		},
		{
			'FIELD': 'LAST_NAME',
			'TYPE': 'CHAR',
			'LENGTH': '32',
			'NULL': True,
			'KEY': '',
			'DEFAULT': '',
			'EXTRA': '',
			'COMMENT': ''
		},
		{
			'FIELD': 'STATUS',
			'TYPE': 'INT',
			'LENGTH': 11,
			'NULL': True,
			'KEY': '',
			'DEFAULT': '1',
			'EXTRA': '',
			'COMMENT': ''
		},
		{
			'FIELD': 'COMMENT',
			'TYPE': 'VARCHAR',
			'LENGTH': '255',
			'NULL': True,
			'KEY': '',
			'DEFAULT': '',
			'EXTRA': '',
			'COMMENT': ''
		}
	]
}
```