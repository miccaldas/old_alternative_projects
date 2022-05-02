"""Converts mardown files to html."""
import os
import subprocess

import isort
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def convert_md_to_html():
    """
    We'll use Pandoc, through Subprocess,
    to convert markdown  files to HTML.
    """

    md_files = os.listdir("md_posts")

    for file in md_files:
        title = file[:-3]
        cmd = f"pandoc --highlight-style=zenburn -s -o html_posts/{title}.html md_posts/{file}"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    convert_md_to_html()
