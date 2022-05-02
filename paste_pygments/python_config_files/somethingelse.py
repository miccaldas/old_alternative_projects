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
title: Change Default Apps in xdg-open
tags:
- xdg-open
- default
- xdg
---

 Here is an example of what I did to change default
 browser from Firefox to Vivaldi, in xdg:
 ______________________________________________________
 xdg-mime dfefault vivaldi-stable.desktop browser/http
 xdg-mime dfefault vivaldi-stable.desktop browser/https
 xdg-mime dfefault vivaldi-stable.desktop browser/ftp
 -------------------------------------------------------
 https://tinyurl.com/ybyepetq
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
