import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

path_directory = '/home/mic/old-html/posts_notes_md'
pyfile_directory = '/home/mic/python/paste_pygments/python_config_files'
for filename in os.listdir(path_directory):
    print(os.path.join(path_directory, filename))
pyfile_directory = '/home/mic/python/paste_pygments/python_config_files'
path = os.path.join(path_directory, filename)
code = """---
title: MySQL Cheatsheet
date: 24-06-21
---

 Access monitor: mysql -u [username] -p; (will prompt for password)
    Show all databases: show databases;
    Access database: mysql -u [username] -p [database]
    Create new database: create database [database];
    Select database: use [database];
    Determine what database is in use: select database();
    Show all tables: show tables;
    Show table structure: desc [table];
    List all indexes on a table: show index from [table];
    Adding a column: ALTER TABLE [table] ADD COLUMN [column] VARCHAR(120);
    Adding a column with an unique, auto-incrementing ID: ALTER TABLE [table] \
    ADD COLUMN [column] int NOT NULL AUTO_INCREMENT PRIMARY KEY;
    Inserting a record: INSERT INTO [table] ([column], [column])\
    VALUES ('[value]', '[value]');
    MySQL function for datetime input: NOW()
    Selecting records: SELECT * FROM [table];
    Explain records: EXPLAIN SELECT * FROM [table];
    Selecting parts of records: SELECT [column], [another-column] FROM [table];
    Selecting specific records: SELECT * FROM [table] WHERE [column] = [value];\
    (Selectors: <, >, !=; combine multiple selectors with AND, OR)
    Select records containing [value]: SELECT * FROM [table] WHERE [column]\
    LIKE '%[value]%';
    Select records starting with [value]: SELECT * FROM [table] WHERE [column]\
    LIKE '[value]%';
    Select records starting with val and ending with ue: SELECT * FROM [table]\
    WHERE [column] LIKE '[val_ue]';
    Select a range: SELECT * FROM [table] WHERE [column] BETWEEN [value1] and [value2];
    Select with custom order and only limit: SELECT * FROM [table] WHERE [column]\
    ORDER BY [column] ASC LIMIT [value]; (Order: DESC, ASC)
    Updating records: UPDATE [table] SET [column] = '[updated-value]'\
    WHERE [column] = [value];
    Deleting records: DELETE FROM [table] WHERE [column] = [value];
    Delete all records from a table (without dropping the table itself):\
    DELETE FROM [table];
    Delete all records in a table: truncate table [table];
    Removing table columns: ALTER TABLE [table] DROP COLUMN [column];
    Deleting tables: DROP TABLE [table];
    Deleting databases: DROP DATABASE [database];
    Custom column output names: SELECT [column] AS [custom-column] FROM [table];
    Export a database dump (more info here): mysqldump -u [username]\
    -p [database] > db_backup.sql
    Use --lock-tables=false option for locked tables (more info here).
    Import a database dump (more info here): mysql -u [username]\
     -p -h localhost [database] < db_backup.sql
    Logout: exit;
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
