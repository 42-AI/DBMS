-- MySQL or mariaDB

CREATE DATABASE db_name;
DROP DATABASE db_name;

CREATE TABLE customers (
    customer_id int,
    name varchar(255),
    age int
);

-- Types:
-- char(n) => 255
-- varchar(n) => 255
-- integer => 10
-- real (6 chiffre de precision) => 37

-- Keywords:
-- PRIMARY KEY
-- NOT NULL
-- NULL
-- AUTO_INCREMENT => equivalent of SERIAL in postgreSQL
-- LIMIT 10

DROP TABLE db_name;

-- ALTER TABLE => add column:
ALTER TABLE customers
ADD surname varchar(255);

-- => DROP COLUMN:
ALTER TABLE table_name
  DROP COLUMN column_name;


-- DESCRIBE provides information about the columns in a table
DESCRIBE tbl_name;

-- SHOW DATABASES lists the databases on the MariaDB server host
SHOW DATABASES;
USE db_name;
SHOW TABLES;

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
DELETE FROM table_name WHERE condition; 

Ponctuation: '()', ',', ';', '+' -- le + pour les concatenation dans les alias aussi
OPERATEURS: < > <= >= = <> != 
LOGICAL: AND, OR

SELECT (DISTINCT) value AS alias,
                  value + '_' + value AS alias
FROM TABLE AS t1
WHERE ...
