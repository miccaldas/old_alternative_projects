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
title: Add Clipboard to Vim
date: 24-06-21
---

 To add clipboard functionality to vim running
 on a server has several steps.
 ---------------------------------------------
 1 - Install Xorg
 2 - Select a 'huge' distribution from vim
 3 - Verify that ~/.ssh/config exists on your
     local computer and add this:
     Host myserver
        ForwardX11 yes
        ForwardX11Trusted yes
 ---------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
