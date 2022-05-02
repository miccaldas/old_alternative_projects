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
title: Turn MD to HTML
tags:
- pygmentize
- markdown
- html
---

 This is the process to turn to html
 the original markdown files. After
 building the corteousquestions.club
 to substitute the
 constantconstipation.club blog, that
 was terminated as it was predicated
 in using static site platforms to
 build it and serve it, and since
 finding out that, for all the trouble
 it gave, you're better off just
 doing everything by yourself.
 Because of slowness on the server, I
 recommend that post manipulations be
 be done in home computer, and then
 send only the files on the 'public'
 folder.
 After some time finding a good
 converter from md to html, and after
 kissing many frogs, I decided to use
 pygmentize. Who had the added
 advantage of already being installed.
 This is the command:
 -------------------------------------
 pygmentyze -f html -o \
 <new-html-to-create> <old md file>
 --------------------------------------
 After that it's needed to insert this
 new html into the post template created.
 This couldn't be done on site, as was
 taking too much time on site.
 After that it's necessary to upload the
 files to the server, create new entry on
 the index page, and that is all she wrote.
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
