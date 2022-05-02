"""Renames all post files."""
import os

import isort
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def rename():
    """
    We'll get a list of the post file names,
    change a character and specific prefixes,
    and rename the files.
    """

    html = os.listdir("html_posts")
    md = os.listdir("md_posts")

    new_name = []
    for name in md:
        if "-" in name:
            rep = name.replace("-", "_")
            os.rename(f"md_posts/{name}", f"md_posts/{rep}")


if __name__ == "__main__":
    rename()
