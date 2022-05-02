""" Module to delete bookmarks from the database """

from mysql.connector import connect, Error
from colr import color
from loguru import logger
import subprocess

fmt = "{time} - {name} - {level} - {message}"
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)
logger.add("logging/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)


def delete():
    ident = input(color(" ID to delete? » ", fore="#f29b85"))
    logger.info(ident)

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = " DELETE FROM bkmks WHERE id = " + ident
        logger.info(query)
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete()
