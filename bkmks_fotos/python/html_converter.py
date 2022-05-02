"""Module that will convert all md files into html, using pandoc"""
import os
import subprocess
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def convert():
    """I'll be using pandoc as shell command as it is easier than programming it"""
    folder = "/srv/http/bkmks_fotos/articles"
    paths = []
    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            paths.append(os.path.join(folder, filename))
        else:
            continue

    for path in paths:
        filename = os.path.basename(path)
        html_url = filename[:-3] + ".html"
        logger.info(html_url)
        cmd = "pandoc --highlight-style=zenburn -s " + filename + " -o" + html_url
        logger.info(cmd)
        subprocess.run(cmd, cwd=folder, shell=True)

    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            cmd = "mv " + folder + "/" + filename + " /srv/http/bkmks_fotos/html_version/"
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    convert()
