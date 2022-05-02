"""
This module will call the 'scrapy crawl' command
on all the files in 'spider_folders'. It will do
so in batches of 40, so as not to invoke the ire
of the Webmaster.
"""
import os
import subprocess
from time import sleep

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


def apps_cli():
    """
    We'll use os.chdir to get to the scrapy folders,
    and subprocess to give the scrapy crawl
    command.
    """

    folders = "/home/mic/python/cli_apps/cli_apps/spider_folders/"
    folder_lst = os.listdir(folders)

    for folder in folder_lst:
        os.chdir(f"{folders}/{folder}/{folder}/spiders/")
        spider_lst = os.listdir("./")
        spi = str([i[:-3] for i in spider_lst if i.endswith("spider.py")])
        spider = spi[1:-1]
        os.chdir(f"{folders}/{folder}")
        print(f"{folders}/{folder}")
        cmd = f"scrapy crawl {spider}"
        subprocess.run(cmd, shell=True)

    os.chdir("/home/mic/python/cli_apps/cli_apps/")


if __name__ == "__main__":
    apps_cli()
