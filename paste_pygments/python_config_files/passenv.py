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
title: Keep Passwords in Enviromental Variables
tags:
- environmental variables
- passwords
- keys
---

 Sometimes is necessary to keep a password, secret key
 in a environmental variable, for added security.
 For this, do the following:
 ------------------------------------------------------
 import os
 export ENVIRONMENT_VARIABLE='<some_long_password>'
 <variable> = os.environ.get('<ENVIRONMENT_VARIABLE>')
 -------------------------------------------------------
 https://tinyurl.com/y47p4wp7
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
