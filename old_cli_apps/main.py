"""Main module of Arch cli packages list update."""
import os
import shutil
import subprocess

import click
import isort  # noqa: F401
import snoop
from crontab import CronTab
from loguru import logger

from build_url_list import build_url_list
from db_upload import db_upload
from main_scrapy import main_scrapy
from move import move
from mv_files import mv_files
from pip_links_upld import links_upload
from run_spider import apps_cli

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def main():
    """
    We'll call functions in order, to get
    not a finished product, because the
    'final_text.txt' generated last, needs
    Sed intervention that can only be done
    seeing it and solving for specific
    problems. Not the kind of thing you can
    program for.
    """

    cmd = "./initiation_scripts.sh"
    subprocess.run(cmd, shell=True)
    build_url_list()
    main_scrapy()
    apps_cli()
    cmd0 = "/home/mic/python/cli_apps/cli_apps/scrapy_files_pre_clean.sh"
    subprocess.run(cmd, shell=True)
    mv_files()
    cmd = "/home/mic/python/cli_apps/cli_apps/clean_files/sed_scripts.sh"
    subprocess.run(cmd, user="mic", shell=True)
    move()
    # db_upload()
    # links_upld.py


if __name__ == "__main__":
    main()


@logger.catch
@snoop
def dunst():
    """
    Sends a dunst notification, saying
    that the update process has run and
    that it awaits inspection.
    """

    cron = CronTab("mic")
    dunst = "/usr/bin/dunstify"
    job = cron.new(command=f'{dunst} "cli_apps has updated and waits inspection."')
    job.minute.every(59)
    cron.write()


if __name__ == "__main__":
    dunst()
