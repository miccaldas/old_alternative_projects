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
title: CMUS Cheatsheet
date: 24-06-21
---

  Here are some cmus commands:
  ------------------------------
  1 - Library
  3 - Playlist
  4 - Queue
  5 - File browser
  7 - Settings
  a - next line down
  b - next track
  z - previous track
  c - pause/unpause
  s - shuffle
  y - add selection to playlist
  v - stop
  -  decrease volume
  + - increase volume
  4 - View/edit queue
  -----------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
