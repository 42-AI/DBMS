CREATE DATABASE sports;
USE sports;
CREATE TABLE activity (
 name char(32) NOT NULL,
 duration int DEFAULT 0,
 animator VARCHAR(42) NOT NULL
);
create table users
(
 users_id int PRIMARY KEY AUTO_INCREMENT,
 first_name	char(32) NOT NULL,
 last_name char(32),
 status int DEFAULT 1,
 comment varchar(255),
);
CREATE TABLE places (
 name char(32) NOT NULL,
 location VARCHAR(42) NOT NULL,
 activities_ids VARCHAR(42) NOT NULL
);
SHOW TABLES ;