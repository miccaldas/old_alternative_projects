"""
Module where we define the tasks
of the yay update process.
"""

import subprocess

import click
import isort  # noqa: F401
import snoop
from crontab import CronTab
from loguru import logger

from app import app
from db_upload import db_upload
from query_builder import query_builder

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@app.task
def run():
    """
    We call all the functions and send
    a dunst warning, telling that the
    process has ran.
    """

    query_builder()
    cmd = "/home/mic/python/cli_apps/cli_apps/yay_querying/extract_file_info.sh"
    subprocess.run(cmd, shell=True)
    db_upload()
    cron = CronTab("mic")
    dunst = "/usr/bin/dunstify"
    job = cron.new(command=f'{dunst} "cli_apps yay has updated and waits inspection."')
    job.minute.every(59)
    cron.write()
