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
title: Give Write Permissions to Multiple User on a Folder
tags:
- permissions
- users
- chmod
---

 1 - Create new group:
 -------------------------------------------------
 sudo groupadd <new_group>
 -------------------------------------------------
 2 - Add users to it:
 -------------------------------------------------
 sudo usermod -a -G <new_group> <user1>
 sudo usermod -a -G <new_group> <user2>
 -------------------------------------------------
 3 - Set new permissions:
 -------------------------------------------------
 sudo chgrp -R <new_group> /path/to/the/directory
 sudo chmod -R 770 /path/to/the/directory
 -------------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
