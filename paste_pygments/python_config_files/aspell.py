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
title: Aspell Micro Plugin
date: 24-06-21
---

 The aspell plugin for the Micro editor is a spell-checker.
 It starts automatically and you just have to accept or not
 the suggestions. You can accept suggestions via this
 command:
 ----------------------------------------------------------
 acceptsug 'n'
 ----------------------------------------------------------
 Or use the 'Tab' key to cycle through possibilities and
 accept.
 It should be noted that the tab shortcut is not just for
 accepting suggestions, you can also do autocomplete,
 indent the selected text, or insert tab.
 You can add words that aspell considers a mistake, to your
 personal dictionary, and this way they won't be picked
 again. The command for this is:
 ----------------------------------------------------------
 addpersonal
 ----------------------------------------------------------
  https://bit.ly/39c21Uz
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
