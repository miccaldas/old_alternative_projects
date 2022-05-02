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
title: Add an App to Ufw List
date: 24-06-21
---

 To add an app, do the following:  
 ------------------------------------
 vi /etc/ufw/applications.d/nginx.ini  
 Place this inside file  

 [Nginx HTTP]  
 title=Web Server  
 description=Enable NGINX HTTP traffic  
 ports=80/tcp  

 [Nginx HTTPS] \  
 title=Web Server (HTTPS) \  
 description=Enable NGINX HTTPS traffic  
 ports=443/tcp  

 [Nginx Full]  
 title=Web Server (HTTP,HTTPS)  
 description=Enable NGINX HTTP and HTTPS traffic  
 ports=80,443/tcp  
 --------------------------------------
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
