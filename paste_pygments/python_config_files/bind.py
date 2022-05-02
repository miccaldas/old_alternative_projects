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
title: Bindkeys in Zsh
date: 24-06-21
---

  To bind a key to a preset command or a command of your own, we first
  need to know what is the code of the key that you intend on using.
  Let's say I want to use the F2 key;
  ------------------------------------------------------------------------------
  1 - 'showkey -a'
  ------------------------------------------------------------------------------
 	After opening the session, just click on the key you want:
  ------------------------------------------------------------------------------
  2 - 'F2'
  3 - ^[OQ 	27 0033 0x1b
  			79 0117 0x4f
  	        81 0121 0x51
  ------------------------------------------------------------------------------
  The code to use is '^[OQ'. Then it can be as simple as:
  ------------------------------------------------------------------------------
  bindkey ^[OQ 'ls -la'
  ------------------------------------------------------------------------------
  or more complex as the case of the one that opens a file in the right
  side of current window, as a scratchpad:
  ------------------------------------------------------------------------------
  bindkey -s '^[OQ tilix -a session-add-right -x '
  micro /home/mic/scratchpad'<simbolo de acento circumflexo>M
  -------------------------------------------------------------------------------
  https://bit.ly/3c9doyn
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
