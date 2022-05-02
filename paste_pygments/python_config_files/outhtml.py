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
title: How to Output HTML Page Based on User Input
tags:
- input
- html
- css
---

In order to receive input from the user on a site
 and do something with it, do the following:
 --------------------------------------------------
 Here's a simple example:

 <!DOCTYPE html>
 <html>
   <form method="GET" action="my_result.php">
     <input type="text" name="my_value">
     <input type="submit">
   </form>
 </html>

 Your second page (the results page) should bear the
 name that you specified in the form's action
 attribute.
 This is the page which will need server-side code.
 So here is an example my_result.php:

 <!DOCTYPE html>
 <html>
   <p><?php echo $_GET['my_value']; ?></p>
 </html>
 -------------------------------------------------------
 If you want the output somewhere else, you can always
 insert it in your HTML like this:
 -------------------------------------------------------
 <? include("results.php"); ?>
 -------------------------------------------------------
 https://bit.ly/3pYaNuu
 https://bit.ly/3kllc2k
"""
pyfile = pyfile_directory + '/' + filename[:-3] + '.py'
lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')
f = open(pyfile[:-3] + '.html', 'w')
highlight(code, lexer, formatter, outfile=f)
