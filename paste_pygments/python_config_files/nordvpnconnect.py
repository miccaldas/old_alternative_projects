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
title: Connect to Nordvpn
tags:
- nordvpn
- openvpn
- vpn
---

 To connect to nordvpn do this:
 ---------------------------------------
 cd /etc/openvpn/ovpn_udp
 sudo openvpn se492.nordvpn.com.udp.ovpn
 user: micaldas@mailfence.com
 pwd: $Gfip9oR;H}u
 ----------------------------------------
 https://tinyurl.com/y92dmaod
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
