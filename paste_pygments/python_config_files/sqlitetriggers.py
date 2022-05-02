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
title: Create SQLite Triggers
tags:
- sqlite
- trigger
- triggers
---

 ---------------------------------------------------------------------------
 CREATE TRIGGER aft_insert AFTER INSERT ON pwd
 BEGIN
 INSERT INTO pwd_fts(pwdid, site, username, passwd, comment, time)
 VALUES(new.pwdid, new.site, new.username, new.passwd, new.comment, new.time);
 END;
 ---------------------------------------------------------------------------
 CREATE TRIGGER aft_del AFTER DELETE ON pwd
 BEGIN
INSERT INTO pwd_fts(pwdid, site, username, passwd, comment, time)
 VALUES ('delete', old.pwdid, old.site, old.username, old.passwd, old.comment, old.time);
 END;
 --------------------------------------------------------------------------
 CREATE TRIGGER aft_updt AFTER UPDATE ON pwd
 BEGIN
 INSERT INTO pwd_fts(pwdid, site, username, passwd, comment, time)
 VALUES ('delete', old.pwdid, old.site, old.username, old.passwd, old.comment, old.time);
 INSERT INTO pwd_fts(pwdid, site, username, passwd, comment, time)
 VALUES(new.pwdid, new.site, new.username, new.passwd, new.comment, new.time);
 END;
 --------------------------------------------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
