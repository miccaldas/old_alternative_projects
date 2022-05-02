"""This module will take a list of urls and take screenshots of them,
    to add, somewhat to the db."""
from loguru import logger
import subprocess
import webbrowser

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch
def take_photos():
    """We'll use function webbrowser to open the links, and scrot to take
    the pictures."""

    with open("urls_bkmks", "r") as f:
        urls = f.readlines()

    for lnk in enumerate(urls):
        webbrowser.open(lnk[1])
        cmd = "scrot -u -d5 " + str(lnk[0])
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    take_photos()
