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
title: Numpy Fancy Indexing
tags:
- numpy
- fancy indexing
- indexing
---

 Fancy indexing allows us to select entire rows or columns out of
 order.
 Fancy indexing allows us to grab any row using its index, let’s
 grab row 1, 2 and 3.
 We need to pass in a list of required rows in square brackets:
 Let's suppose a 2D array named 'arr':
 ----------------------------------------------------------------
 arr[[1,2,3]]
 output: array([[1,1,1],
                [2,2,2],
                [3,3,3]])
 ----------------------------------------------------------------
 Now with columns:
 ---------------------------------------------------------------
 arr[:,[3,2]]
 output: array([[3,2],
                [7,6],
                [1,0],
                [0,1]])
 -----------------------------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
