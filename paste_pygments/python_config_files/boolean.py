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
title: Send Boolean Mask Arrays
date: 24-06-21
---

 Boolean mask is very useful and handy, when it comes to count, modify,
 extract or manipulate values in an array based on certain condition
 or criteria:
 --------------------------------------------------------------------
 arr([1,2,3,4,5,6,7,8,9])
 --------------------------------------------------------------------
 Now we create a boolean condition:
 --------------------------------------------------------------------
 bool_array = arr > 3
 print(bool_array)
 output: array([False,False,False,True,True,True,True,True,True])
 -------------------------------------------------------------------
 Now we create a boolean mask to filter all even numbers in 'arr':
 -------------------------------------------------------------------
 mask = 0 == arr % 2
 print(mask)
 output: array([False,True,False,True,False,True,False,True,False])
 ------------------------------------------------------------------
 Now with our mask, 'mask', we index on 'arr', that will return a
 1D array with the values that satisfy the condition:
 ------------------------------------------------------------------
 even_values = arr[mask]
 print(even_values)
 output: [2,4,6,8]
 ------------------------------------------------------------------
 https://bit.ly/2MPWcUb
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
