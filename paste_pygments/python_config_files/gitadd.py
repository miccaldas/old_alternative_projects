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
title: Add Project to Remote Repository
tags:
- git
- notabug
- gitea
---

  1 - Create a new repository, if needed,
  2 - Change the current working directory
      to your local project.
  3 - Initialize the local directory as a
      Git repository:
  ----------------------------------------
  git init -b main
  ----------------------------------------
  4 - Adds the files in the local
      repository and stages them for
      commit. To unstage a file, use 'git
      reset HEAD YOUR-FILE':
  -----------------------------------------
  git add .
  -----------------------------------------
  5 - Commit the files that you've staged
      in your local repository.
  -----------------------------------------
  git commit -m "First commit"
  -----------------------------------------
  6 - copy the remote repository URL.
  7 - add the URL for the remote repository
      where your local repository will be
      pushed:
  ------------------------------------------
  git remote add origin  <REMOTE_URL>
  ------------------------------------------
  8 - Push the changes in your local
      repository to remote repository:
  ------------------------------------------
  git push origin main
  ------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
