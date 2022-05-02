"""Where we build the urls that we'll search in scrapy."""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from systemd import journal

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def build_url_list():
    """
    We get the usual structure of pypi site,
    and insert the names in the name list
    where the names usually go in the url.
    """

    with open("/home/mic/python/cli_apps/cli_apps/lists/pypi/only_names.txt", "r") as f:
        names = f.readlines()
    journal.sendv("MESSAGE=only_names_list", "CODE_FILE=build_url_list.py", "CODE_FUNC=build_url_list")
    for name in names:
        journal.sendv("MESSAGE=the name is {}".format(name), "CODE_FILE=build_url_list.py", "CODE_FUNC=build_url_list", "CODE_LINE=34")

    urls = []
    sname = [i for i in names if not (".") in i]
    journal.sendv("MESSAGE=List sname", "CODE_FILE=build_url_list.py", "CODE_FUNC=build_url_list", "CODE_LINE=39")
    for name in sname:
        lname = name.lower()
        gname = lname.replace("-", "_")
        rname = gname.strip()
        journal.sendv("MESSAGE=rname is {}".format(rname), "CODE_FILE=build_url_list.py", "CODE_FUNC=build_url_list", "CODE_LINE=43")
        url = f"https://pypi.org/project/{rname}"
        urls.append(url)

    for url in urls:
        journal.sendv("MESSAGE=url is {}".format(url), "CODE_FILE=build_url_list.py", "CODE_FUNC=build_url_list", "CODE_LINE=48")
        with open("/home/mic/python/cli_apps/cli_apps/lists/pypi/urls.txt", "a") as f:
            f.write(url)
            f.write("\n")


if __name__ == "__main__":
    build_url_list()
