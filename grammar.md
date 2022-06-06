# SQL Grammar syntax

## KEY WORDS
- SELECT (AS)
- FROM
- WHERE
- CREATE DATABASE
- DROP DATABASE
- VALUES
- CREATE TABLE
- DROP TABLE <IF EXISTS> <name>
- INSERT INTO
- SHOW DATABASES
- SHOW TABLES
- USE <db_name>

## BASIC OPERATORS
- `=`
- `>`
- `<`
- `>=`
- `<=`
- `!=` (or `<>`)

## LOGICAL OPERATORS
- AND
- ANY
- BETWEEN
- EXISTS
- IN
- LIKE
- NOT
- OR
- (SOME)
- (ALL)

## PATTERNS
``` SQL
DELETE FROM table_name WHERE condition;
CREATE DATABASE IF NOT EXISTS db_name;
CREATE DATABASE db_name;
CREATE TABLE table_name (
 column1 datatype,
 column2 datatype,
 name VARCHAR(20) NOT NULL
);
INSERT INTO table (nom_colonne_1, nom_colonne_2, ...)
 VALUES ('valeur 1', 'valeur 2', ...)
```

## DATATYPES
** see https://www.w3schools.com/sql/sql_datatypes.asp **
- VARCHAR(size)
- CHAR(size)
- TEXT(size)
- BOOL (or BOOLEAN)
- INT(size) [or INTEGER(size)]
- FLOAT(p)	A floating point number. MySQL uses the p value to determine whether to use FLOAT or DOUBLE for the resulting data type. If p is from 0 to 24, the data type becomes FLOAT(). If p is from 25 to 53, the data type becomes DOUBLE()
- DATE => A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
- TIMESTAMP(fsp)	A timestamp. TIMESTAMP values are stored as the number of seconds since the Unix epoch ('1970-01-01 00:00:00' UTC). Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1970-01-01 00:00:01' UTC to '2038-01-09 03:14:07' UTC. Automatic initialization and updating to the current date and time can be specified using DEFAULT CURRENT_TIMESTAMP and ON UPDATE CURRENT_TIMESTAMP in the column definition
- TIME(fsp)	A time. Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'
- YEAR	A year in four-digit format. Values allowed in four-digit format: 1901 to 2155, and 0000.
MySQL 8.0 does not support year in two-digit format.

## TMP Notes
select 'a', b 'c' from alphabet
select 'a', b, 'c' WHERE a > b from alphabet
select 'a', b, 'c' WHERE (aaa > bbb) and b < c from alphabet
select a, b, c WHERE (a AND b) OR ((c LIKE 'pattern') AND a != 3) AND 


## How to connect to a local mysql server (with mamp)

``` zsh
mysql -u root -proot -h localhost
mysql> show databases;
mysql> create database dbms;
mysql> show tables
    -> ;
```
