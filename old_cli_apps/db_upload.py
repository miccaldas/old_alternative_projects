"""
We'll read the last file of the transient files in
'clean_files', turn it into a list of tuples
and send it to a MySQL database.
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
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each a
    to a column and the upload is
    complete.
    """

    folders = "/home/mic/python/cli_apps/cli_apps/yay_querying/results/"
    paths = [os.path.join(folders, file) for file in os.listdir(folders)]

    for file in paths:
        name = file[2]
        presentation = file[0]
        url = file[1]
        answers = [name, presentation, url]
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "INSERT INTO cli_apps (name, presentation, url) VALUES (%s, %s, %s)"
            cur.execute(query, answers)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    db_upload()
