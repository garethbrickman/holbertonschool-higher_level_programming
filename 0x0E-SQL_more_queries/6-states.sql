-- Creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
id INT SERIAL DEFAULT VALUE PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
