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
title: MySQL Generated Columns
tags:
- mysql
- columns
- generated
---

 MySQL's generated columns, allow you to create
 columns that are the result of an arithmetical
 calculation. For example:
 -----------------------------------------------
 ALTER TABLE products
 ADD COLUMN stockValue
 GENERATED ALWAYS AS (buyprice*stock) STORED;
 -----------------------------------------------
 STORED refers if you create a normal column or
 use a virtual one. Keep in mind the default is
 virtual. So you have to put STORED.
 ------------------------------------------------
 https://tinyurl.com/yhdmfsj2
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
