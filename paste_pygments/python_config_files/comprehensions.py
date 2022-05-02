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
title: Dictionaty Comprehensions
date: 24-06-21
---

 Dictionary comprehension is a method for transforming one dictionary
 into another dictionary. During this transformation, items within
 the original dictionary can be conditionally included in the new
 dictionary and each item can be transformed as needed. This is the
 general template you can follow for dictionary comprehension in
 Python:
 --------------------------------------------------------------------
 dict_variable = {key:value for (key,value) in dictonary.items()}
 --------------------------------------------------------------------
 a simple dictionary comprehension:
 --------------------------------------------------------------------
 dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
 # Double each value in the dictionary
 double_dict1 = {k:v*2 for (k,v) in dict1.items()}
 print(double_dict1)
 {'e': 10, 'a': 2, 'c': 6, 'b': 4, 'd': 8}
 --------------------------------------------------------------------
 https://bit.ly/2Ysf4ev
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
