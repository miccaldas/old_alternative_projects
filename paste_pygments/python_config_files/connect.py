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
title: Solve Connection Error Python MySQL
date: 24-06-21
---

 If you're getting this error message:
 “mysql.connector.errors.ProgrammingError: 1698 (28000):
 Access denied for user 'root'@'localhost'”
 I solved it doing what I show below.
 Don't ask me what it does. I don't know either.
 ------------------------------------------------------------------
 mysql -u root -p
 USE mysql;
 UPDATE user SET plugin='mysql_native_password' WHERE User ='root';
 FLUSH PRIVILEGES;
 exit;
 systemctl restart mysql
 -------------------------------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
