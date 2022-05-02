"""
We'll use yay's package information system
to get information on installed packages.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def query_builder():
    """
    We'll instantiate the lists
    here, and then we'll pass its entries
    through a subprocess command, that will
    link to yay.
    """

    name_path = "/home/mic/python/cli_apps/cli_apps/lists/arch/names_linux.txt"

    with open(name_path, "r") as f:
        names = f.readlines()

    clean = [i.strip() for i in names]
    print(clean)

    for name in clean:
        cmd = f"yay -Si {name} > package_files/{name}.txt"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    query_builder()
