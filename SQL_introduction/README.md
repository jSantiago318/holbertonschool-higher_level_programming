# SQL - Introduction

An introduction to databases and SQL using MySQL 8.0 on Ubuntu 22.04 LTS.

## Learning Objectives

- What a database and a relational database are
- What SQL and MySQL stand for
- How to create a database in MySQL
- What DDL and DML stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What subqueries are
- How to use MySQL functions

## Requirements

- Files are executed on Ubuntu 22.04 LTS using MySQL 8.0 (version 8.0.25)
- All files end with a new line
- Every SQL query is preceded by a comment describing it
- Every file starts with a comment describing the task
- All SQL keywords are in uppercase

## Tasks

| File | Description |
| ---- | ----------- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |

## Usage

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
