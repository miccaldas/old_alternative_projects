"""
This module will iterate through the names list and
check if the packages are really installed, as it
seems to me that the list represents what I
downloaded, not what I have,
"""
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
def check_package_existence():
    """
    We'll iterate through the names list and
    pass it through the linux find command.
    If the length of the response is < 1,
    it will right to another list, stating
    the name that failed the search.
    """

    with open("lists/names_linux.txt", "r") as f:
        nam = f.readlines()
    names = [i.strip() for i in nam]

    existing = []
    for name in names:
        cmd = f"/home/mic/scripts/find.sh {name}"
        sub = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        print(sub.stdout)
        if sub.stdout != b"":
            existing.append(name)

    with open("lists/existing.txt", "a") as f:
        for ex in existing:
            f.write(ex)
            f.write("\n")


if __name__ == "__main__":
    check_package_existence()
