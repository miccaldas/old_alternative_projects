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
title: Snippets
date: 24-06-2021
---

At a certain moment, you're forced to ask yourself why you keep doing it.  
Everything that you collect just makes it that much arder to keep a mental
image of what you got.  
You can get so much that it it's just unmanageable, and you're better off
with much less.  
So is my experience with collecting notes on python and linux.  
If you don't know that you've got it, you'll never remember to look for it.  
And that's probably the great reason behind this blog, to make me take heed  
of what I have. To count it, acknowledge it and, if at all possible,  
remember.  
Besides, creating blogs is fun.  
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
