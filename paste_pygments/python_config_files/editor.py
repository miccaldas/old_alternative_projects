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
title: Edit Command Line Commands in Editor
tags:
- editor
- command line
- editing
---

 Suppose you are typing a very long command line:
 PATH='/home/alw/bin:/home/alw/bin:/home/alw/bin:
 /usr/local/sbin:/usr/local/bin:/usr/sbin:
 /usr/bin:/sbin:/bin:/usr/games:/usr/local/games:
 /snap/bin'
 You discover a mistake before you hit Enter. Or
 you discover it later and call the line back in
 your history. You can edit on the command line,
 of course, but if you prefer your editor of
 choice press Control+X Control+E. Your default
 editor (usually set with $EDITOR or $VISUAL)
 will start with the command loaded.
 https://bit.ly/2Y96wc4
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
