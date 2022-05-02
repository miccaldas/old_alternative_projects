"""This is where the 'scrapy_project' module will be started."""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

from scrapy_project import ScrapyProject

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def main_scrapy():
    """
    We'll instantiate the ScrapyProject class with the
    values for project name, spider name and url, and
    run all its methods.
    """
    cwd = os.getcwd()
    os.chdir(f"{cwd}/spider_folders/")

    names = []
    with open(f"{cwd}/lists/pypi/only_names.txt", "r") as f:
        nam = f.readlines()
        for na in nam:
            nam = na.strip()
            n = nam.replace("-", "_")
            nb = n.lower()
            names.append(nb)

    with open(f"{cwd}/lists/pypi/urls.txt", "r") as f:
        urlsss = f.readlines()
        urlss = [i.strip() for i in urlsss]
        urls = [i.replace("-", ".") for i in urlss]

    name_url = list(zip(names, urls))
    name_urls = sorted(name_url)

    for name, url in name_urls:
        project_name = f"{name}_scrapy"
        spider_name = f"{project_name}_spider.py"
        scr = ScrapyProject(project_name, spider_name, url)
        scr.project_creation()
        scr.settings_definition()
        scr.spider()


if __name__ == "__main__":
    main_scrapy()
