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
title: String Manipulation
tags:
- strings
- string
- python
---

 Here are some string manipulation that proved useful.
 Split method:
 ------------------------------------------------------
 s = "Username: How are you today?"
  s.split(':')
  ['Username', ' How are you today?']
  s.split(':')[0]
  'Username'
  https://bit.ly/3pC2uFi
  -----------------------------------------------------
  Python String upper():
  -----------------------------------------------------
  text = 'geeKs For geEkS'
  print(text.upper())
  GEEKS FOR GEEKS
  https://bit.ly/3coDs8R
  -----------------------------------------------------
  How to get the part of a string before a specific
  character in Python:
  -----------------------------------------------------
  a_string = "docs.python.org"
  partitioned_string = a_string.partition('.')
  print(partitioned_string)
  Output: ('docs', '.', 'python.org')
  before_first_period = partitioned_string[0]
  print(before_first_period)
  Output: docs
  https://bit.ly/3oBMBgS
  -----------------------------------------------------
  Several methods to remove characters from a string,
  can be seen here: https://bit.ly/2MEM4xi
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
