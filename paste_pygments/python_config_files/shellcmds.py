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
title: Execute Shell Commands in Remote Servers With Python
tags:
- fabric
- remote
- ssh
---

 Fabric is a high level Python library designed to execute
 shell commands remotely over SSH.
 Example taken from a script written to alter folder
 permissions when updating content on the hugo blog server:
 -----------------------------------------------------------
 from fabric import Connection
 c = Connection(
     host = 'constantconstipation.club',
     user = 'root',
     connect_kwargs={
         'key_filename': '/home/mic/.ssh/id_rsa'
     }
 )
 c.run('cd /var/www/constantconstipation.club/html/ &&
 chown -R www-data:www-data public')
 -----------------------------------------------------------
 http://www.fabfile.org/
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
