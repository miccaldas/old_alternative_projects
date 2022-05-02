"""
In order to have just one font in all posts, we insert into the
metadata, the 'mainfont' attribute, that is honoured by Pandoc.
"""
import os

import isort
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def new_metadata():
    """
    We insert a new line, in line number 2, with
    the text 'mainfont: Iosevka' in the markdown
    files.
    """

    old_md = os.listdir("md_posts")

    for file in old_md:
        with open(f"md_posts/{file}", "r") as f:
            contents = f.readlines()
        contents.insert(2, "mainfont: Iosevka\n")
        with open(f"new_md/{file}", "w") as f:
            contents = "".join(contents)
            f.write(contents)


if __name__ == "__main__":
    new_metadata()
