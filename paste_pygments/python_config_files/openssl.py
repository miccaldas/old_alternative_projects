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
title: Connecting Externally With Openssl
tags:
- openssl
- ssl
- mail
---

  This subject came to me, when I needed to connect with a mail
  server that had ssl encryptation. To link to it you do the
  following:
  --------------------------------------------------------------
  openssl s_client --connect <server name:port>
  --------------------------------------------------------------
  After that it will probably be needed login information, which
  can be inputted in the following manner:
  --------------------------------------------------------------
  a1 login <username> <password>
   -------------------------------------------------------------
  Notice the 'a1' tag. It can be anything you like, but it must
  be consistent. For instances, after 'a1' must come 'a2', and
  so on.
  --------------------------------------------------------------
  a2 list '' '*'
  --------------------------------------------------------------
  Shows a list of your mailboxes.
  -------------------------------------------------------------
  a3 examine <mailbox name>
  -------------------------------------------------------------
  Gives you metadata about the mailbox.
  -------------------------------------------------------------
  a4 select <mailbox name>
  -------------------------------------------------------------
  Selects a particular mailbox
  -------------------------------------------------------------
  a5 fetch 1 body[]
  -------------------------------------------------------------
  Fetches the first email in the mailbox.
  -------------------------------------------------------------
  For more information see:
  https://bit.ly/38HrK76
  https://tools.ietf.org/html/rfc3501#page-27
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
