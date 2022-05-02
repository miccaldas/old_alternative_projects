"""
I completely forgot to add the packages urls to
the information sent when we were dealing with
pypi. We're here to remedy this situation.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def pip_links_upld():
    """
    We'll prepare the information to
    to be sent to the db. We're going
    to get a list of links, extract
    from them the package name, and
    then we'll build a mysql query
    where we upload the url to the
    package.
    """

    with open("/home/mic/python/cli_apps/cli_apps/lists/urls_pip.txt", "r") as f:
        urls = f.readlines()

    clean = [i.strip() for i in urls]

    db_lst = []
    for i in clean:
        name = os.path.basename(os.path.normpath(f"{i}"))
        db_lst.append((name, i))

    return db_lst


if __name__ == "__main__":
    pip_links_upld()


@logger.catch
@snoop
def links_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each a
    to a column and the upload is
    complete.
    """

    data = pip_links_upld()
    for i in data:
        name = i[0]
        url = i[1]
        answers = [url, name]
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "UPDATE cli_apps SET url = %s WHERE name = %s"
            cur.execute(query, answers)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    links_upload()
