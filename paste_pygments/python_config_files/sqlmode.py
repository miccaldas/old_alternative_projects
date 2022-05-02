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
title: Change MySQL sql_mode
tags:
- mysql
- sql_mode
- global
---

 If you're getting several errors inputting commands,
 it might be that the cause is that the mysql_mode is
 defined with STRICT_TRANS_TABLES which comes by
 default currently. To change this, do:
 -----------------------------------------------------
 SELECT @@GLOBAL.sql_mode global, \
 @@SESSION.sql_mode session;
 SET sql_mode = '';
 SET GLOBAL sql_mode = '';
 -----------------------------------------------------
 This turns sql_mode into a empty string.
 https://bit.ly/2LMtH9G
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
