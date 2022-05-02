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
title: Send Notifications Through Cron
date: 24-06-21
---

 To send notifications through cron (as done in the todo app),
 the command in the cron jobs need the following structure:
 -------------------------------------------------------------
 export DISPLAY=:0.0 && XDG_RUNTIME_DIR=/run/user/$(id -u)
 /usr/bin/notify-send '<text for notifications>'
 -------------------------------------------------------------
 Remember it must be sent as root. 'sudo crontab -e'
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
