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
title: Update MySQL Value by Subtracting
tags:
- mysql
- operations
- arithmetic
---

 To use an arithmetical operation on
 MySQL db's you can do the following:
 example with subtraction:
 ------------------------------------
 UPDATE <table_name>
 SET <column_to_be_altered> = \
 <column_to_be_altered> - <value>
 -------------------------------------
 Although this is interesting, if
 possible use generated columns, like
 this example taken from the adventure
 game:
 --------------------------------------
 ALTER TABLE mana ADD COLUMN total \
 GENERATED ALWAYS AS (value+damage) \
 STORED;
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
