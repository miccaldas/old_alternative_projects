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
title: Creating Range of Variables Numbered
tags:
- numbered variables
- range
- variables with numbers
---

 For creating a range of variables with numbers, (something
 like this: 'var0', or 'var_0') you do the following:
 ----------------------------------------------------------
 for key in range(9):
    globals()['key_{}'.format(key)] = 'a'
 ----------------------------------------------------------
 This will produce a set of variables, name thusly, 'key_0,
 'key_1' and so on, that will all have the value 'a'. But
 that can be easily changed.
 https://bit.ly/3oBeANz
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
