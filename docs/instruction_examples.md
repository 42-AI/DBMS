# SQL instructions examples

## For USE :
`USE <db_name>`
NB: USE works without the final `;`

mysql console messages format:
`Database changed`
`ERROR 1049 (42000): Unknown database '<db_name>'`

## For SHOW :
`SHOW DATABASES ;`
`SHOW TABLES ;` => only works if a `USE <db_name>` was made before!!

mysql console messages format:
`4 rows in set (0.00 sec)`

## For CREATE :

### CREATE DATABASE:
`CREATE DATABASE <db_name> ;`
`CREATE DATABASE IF NOT EXISTS <db_name> ;`

mysql console messages format :
`Query OK, 1 row affected (0.00 sec)`
`ERROR 1007 (HY000): Can't create database 'test'; database exists`

### CREATE TABLE:
``` sql
CREATE TABLE table_name (
 column1 datatype,
 column2 datatype,
 name VARCHAR(20) NOT NULL
);
```

``` sql
create table new_employees
(
	employee_id  int,
	first_name  varchar(15) null,
	last_name varchar(15),
    age datetime,
	hire_date date default sysdate,
	created_at timestamp,
	updated_at timestamp,
	deleted_at timestamp
);
```
