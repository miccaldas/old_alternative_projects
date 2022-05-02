""" Converts several markrdown files in html """
import os
from os import walk
from os import listdir
import markdown

directory = os.getcwd()

""" Creates list of all markdown files in present folder """

files_md = [open(i, "rb") for i in os.listdir(directory) if i.endswith('.md')]
str_files = [i for i in os.listdir(directory) if i.endswith('.md')]
print(str_files)

""" We will convert all markdown files in html in a given folder, and keep them in a separate folder we'll create """
path = directory + '/html_files'

full_link = []
for i in str_files:
    a = str(directory) + '/' + i
    full_link.append(a)

for i in full_link:
    with open(i, "r") as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(i + ".html", "w") as f:
        f.write(html)

# https://do.co/37m2tOM
