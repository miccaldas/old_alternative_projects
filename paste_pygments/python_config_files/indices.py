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
title: Replace Multiple indices in String
tags:
- string
- replace
- remove
---

 To replace various indices in a string,
 do the following:
 ----------------------------------------
 test_str = 'geeksforgeeks is best'
 indices = [2, 4, 7, 10]
 repl_char = '*'   # replacement_character
 temp = list(test_str)
 for idx in indices:
    temp[idx] = repl_char
 res = ''.join(temp)
 print(res)
 Output: 'ge*k*fo*ge*ks is best'
 -----------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
