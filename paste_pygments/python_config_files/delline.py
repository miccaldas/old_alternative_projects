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
title: Delete Lines in Files
---
title: Markdown
date: 24-06-21
---

 You need to open the file and read its contents in memory,
 then open the file again write the line to it but without
 the line you wish to omit
 Example:
 ---------------------------------------------------------
 with open('yourfile.txt', 'r') as f:
     lines = f.readlines()
 with open('yourfile.txt', 'w') as f:
     for line in lines:
             if line.strip('
') != 'nickname_to_delete':
                 f.write(line)'
 --------------------------------------------------------
 https://bit.ly/3nUlzRp
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
