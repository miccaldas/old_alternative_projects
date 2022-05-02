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
title: Python Debugger Trepan3k
tags:
- trepan3k
- debug
- debugger
---

 To use the Trepan3k (python 3 version of Trepan2), we can,as an
 example, construct the following command line expression:
 ----------------------------------------------------------------
 trepan3k --highlight=light -o <somefile.txt> file_to_debugged.py
 ----------------------------------------------------------------
 The flag '--highlight', colorizes the output. It can be light or
 dark.
 The flag '-o' defines to what file will go the output of the
 debugging. BEWARE, if you choose this, you wont see the output
 when running it from the terminal.
 https://python2-trepan.readthedocs.io
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
