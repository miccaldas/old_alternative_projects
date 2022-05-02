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
title: Configuring Lighttpd Web Server
tags:
- lighttpd
- web server
- server
---

To configure a lighttpd server, take the following steps:
 --------------------------------------------------------------
 To get the latest php version in ubuntu or debian server,
 add the following repository:
 add-apt-repository -y ppa:ondrej/php
 apt update
 --------------------------------------------------------------
 apt install -y lighttpd
 --------------------------------------------------------------
 groupadd lighttpd
 useradd -g lighttpd -d /var/www/html -s /sbin/nologin lighttpd
 chown -R lighttpd:lighttpd /var/www/html/
 ---------------------------------------------------------------
 Install PHP:
 apt install -y php-{cli,gd,fpm,mysql,curl,json,xml}
 ---------------------------------------------------------------
 mv /etc/php/8.0/fpm/pool.d/www.conf \
 /etc/php/8.0/fpm/pool.d/lighttpd.conf
 ---------------------------------------------------------------
 Enter the pool config file:
 vim /etc/php/8.0/fpm/pool.d/lighttpd.conf
 Change the following:
 Change the top line inside the brackets that sets the pool \
 name from [www] to [lighttpd]
 Change the line user = www-data to user = lighttpd
 Change the line group = www-data to group = lighttpd
 Change the line listen = /run/php/php8.0-fpm.sock to listen = \
 /run/php/php8.0-lighttpd-fpm.sock
 Change listen.owner = www-data to listen.user = lighttpd
 Change listen.group = www-data to listen.group = lighttpd
 ----------------------------------------------------------------
 systemctl restart php8.0-fpm
 ----------------------------------------------------------------
 apt install -y gcc libpcre3 libpcre3-dev zlib1g-dev \
 checkinstall libssl-dev
 ----------------------------------------------------------------
 wget https://download.lighttpd.net/lighttpd/<latest-release>
 ----------------------------------------------------------------
 configure the package with this command;
 ./configure --with-openssl --sbindir=/usr/sbin
 ----------------------------------------------------------------
 Enable the cgi and php modules.
 lighttpd-enable-mod fastcgi
 lighttpd-enable-mod fastcgi-php
 ----------------------------------------------------------------
 Edit the PHP configuration
 vim etc/lighttpd/conf-enabled/15-fastcgi-php.conf
 Remove the entire file contents and replace it with the following,
 fastcgi.server += ( ".php" =>
        ((
                "socket" => "/run/php/php8.0-lighttpd-fpm.sock",
                "broken-scriptfilename" => "enable"
        ))
)
--------------------------------------------------------------------
systemctl start lighttpd
For more information see here: https://tinyurl.com/yhw9bxsr

"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
