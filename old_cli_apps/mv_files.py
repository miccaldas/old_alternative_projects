"""
Module that will get information from the
files in the spider folders and add the
url data to the bunch.
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
def mv_files():
    """
    We'll use 'os' to get us inside the
    the directories in 'spider_folders',
    get the information to a list of
    tuples.
    """

    cwd = os.getcwd()
    # os.chdir(f"{cwd}/spider_folders/")
    path = "/home/mic/python/cli_apps/cli_apps/spider_folders/"

    jslist = []
    for d in os.listdir(path):
        print(d)
        if "results.txt" in os.listdir(f"{path}{d}"):
            if os.path.getsize(f"{path}{d}/results.txt") != 0:
                with open(f"{path}{d}/results.txt", "r") as f:
                    data = f.readlines()
                    jslist.append((f"{d[:-7]}", f"{data}"))
        os.chdir("../")
    print(jslist)

    with open(f"{cwd}/clean_files/final_list.txt", "w") as f:
        f.write(str(jslist))
    return jslist


if __name__ == "__main__":
    mv_files()
