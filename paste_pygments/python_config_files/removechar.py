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
title: Remove Characters From String Using Translate
tags:
- remove
- string
- characters
---

 Python string translate() function replace each character in the string
 using the given translation table. We have to specify the Unicode code
 point for the character and ‘None’ as a replacement to remove it from
 the result string. We can use ord() function to get the Unicode code
 point of a character.
 -------------------------------------------------------------------------
 s = 'abc12321cba'
 print(s.translate({ord('a'): None}))
 Output: bc12321cb
 -------------------------------------------------------------------------
 If you want to replace multiple characters, that can be done easily using
 an iterator. Let’s see how to remove characters ‘a’, ‘b’ and ‘c’ from a
 string.
 --------------------------------------------------------------------------
 s = 'abc12321cba'
 print(s.translate({ord(i): None for i in 'abc'}))
 Output: 12321
 ---------------------------------------------------------------------------
 https://bit.ly/2MEM4xi
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
