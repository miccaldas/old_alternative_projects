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
title: Create Dictionary With Multiple Values
tags:
- dictionary
- python
- key
---

 There are a couple of ways to add values to key, and to create a list
 if one isn't already there. I'll show one such method in little steps.
 ----------------------------------------------------------------------
 key = somekey
 a.setdefault(key, [])
 a[key].append(1)
 ----------------------------------------------------------------------
 Results:
 ----------------------------------------------------------------------
 >>> a
 {'somekey': [1]}
 Next, try:
 key ='somekey'
 a.setdefault(key, [])
 a[key].append(2)
 -----------------------------------------------------------------------
 Results:
 -----------------------------------------------------------------------
 >>> a
 {'somekey': [1, 2]}
 ------------------------------------------------------------------------
 The magic of setdefault is that it initializes the value for that key
 if that key is not defined, otherwise it does nothing. Now, noting
 that setdefault returns the key you can combine these into a single line:
 -------------------------------------------------------------------------
 a.setdefault('somekey',[]).append('bob')
 -------------------------------------------------------------------------
 Results:
 -------------------------------------------------------------------------
 >>> a
 {'somekey': [1, 2, 'bob']}
 -------------------------------------------------------------------------
 https://bit.ly/3p3h2O4
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
