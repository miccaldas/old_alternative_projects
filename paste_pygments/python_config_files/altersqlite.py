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
title: Alter SQLite
date: 24-06-21 
---

 Para alterar uma table que não possa ser alterada por
 sqlite-utils,podemos usar este modelo. É também mais seguro,
 que o sqlite-utils também faz alguma merda.
 -------------------------------------------------------------
 PRAGMA foreign_keys=off;
 BEGIN TRANSACTION;
 CREATE TABLE IF NOT EXISTS new_table(
    column_definition,
 );
 INSERT INTO new_table(column_list)
 SELECT column_list
 FROM table;
 DROP TABLE table;
 ALTER TABLE new_table RENAME TO table;
 COMMIT;
 PRAGMA foreign_keys=on;
 -------------------------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
