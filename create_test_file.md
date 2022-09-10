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
    "NAME": "customers",
    "DESCRIPTION": [
        {
            "FIELD": "customer_id",
             "TYPE" : "int",
             "LENGTH": 11,
             "NULL": False, # ==> NOT NULL
             "KEY": "PRIMARY",
             "DEFAULT": "",
             "EXTRA": "AUTO_INCREMENT",
             "COMMENT": "This is a random comment"
         },
        {
            "FIELD_NAME", "first_name",
            "TYPE" , "char",
            "LENGTH", 32,
            "ALLOW NULL", False, # ==> NOT NULL
            "KEY", None,
            "DEFAULT", "",
            "EXTRA", None,
            "COMMENT", ""
        },
        {
            "FIELD_NAME", "last_name",
            "TYPE" , "char",
            "LENGTH", 32,
            "ALLOW NULL", True, # ==> NULL ALLOWED
            "KEY", None,
            "DEFAULT", "",
            "EXTRA", None,
            "COMMENT", ""
        },
        {
            "FIELD_NAME", "status" ,
            "TYPE" , "int" ,
            "LENGTH", 11 ,
            "ALLOW NULL", True, # ==> NULL ALLOWED
            "KEY", None,
            "DEFAULT", "1",
            "EXTRA", None,
            "COMMENT", ""
        },
        {
            "FIELD_NAME", "status",
            "TYPE" , "int",
            "LENGTH", 11,
            "ALLOW NULL", True, # ==> NULL ALLOWED
            "KEY", None,
            "DEFAULT", "1",
            "EXTRA", None,
            "COMMENT", ""
            
        }
        
    ]
}
```
