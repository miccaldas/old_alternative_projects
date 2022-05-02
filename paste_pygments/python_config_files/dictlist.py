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
title: Convert Dictionary to List
tags:
- dictionary
- list
- python
---

 Converting the values of a dictionary to a list creates a new list
 where each element is a value from the dictionary. For example,
 converting the values of {a:1,b:2} to a list results in [1,2].
 Call dict.values() to create a view of the dictionary's values.
 Use list(item) with the view of dictionary values as item to return
 a list.
 Example:
 a_dictionary = {a: 1, b: 2}
 values = a_dictionary.values()
 Retrieve dictionary values
 values_list = list(values)
 Convert to list
 print(values_list)
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
