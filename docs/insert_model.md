```sql
INSERT INTO customers (first_name, last_name, comment)
VALUES
 ('Rébecca', 'Armand', 'Saint-Didier-des-Bois'),
 ('Aimée', 'Hebert', 'Marigny-le-Châtel'),
 ('Marielle', 'Ribeiro', 'Maillères'),
 ('Hilaire', 'Savary', 'Conie-Molitard');
```

```python
keyword = "INSERT INTO",
data = {
    'NAME': 'CUSTOMERS',
    'DATA': [
        {
            'first_name': 'Rébecca',
            'last_name': 'Armand',
            'comment': 'Saint-Didier-des-Bois',
        },
        {
            'first_name': 'Aimée',
            'last_name': 'Hebert',
            'comment': 'Marigny-le-Châtel',
        },
        {
            'first_name': 'Marielle',
            'last_name': 'Ribeiro',
            'comment': 'Maillères',
        },
        {
            'first_name': 'Hilaire',
            'last_name': 'Savary',
            'comment': 'Conie-Molitard',
        },
    ]
}

```

```sql
create table customers
(
	customer_id  int PRIMARY KEY AUTO_INCREMENT comment="This is a random comment",
	first_name	char(32) NOT NULL,
	last_name	char(32),
	status		int DEFAULT 1,
	comment		varchar(255),
);
```