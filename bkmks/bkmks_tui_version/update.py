""" Module to update bookmarks to database """
import time
from mysql.connector import connect, Error
import click
from colr import color
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


def update():
    coluna = input(color(" Column? » ", fore="#f29b85"))
    ident = input(color(" ID? » ", fore="#f29b85"))
    print(color(" Write your update", fore="#f29b85"))
    time.sleep(0.3)
    update = click.edit()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = "UPDATE bkmks SET " + coluna + " = '" + update + "' WHERE id = " + ident
        logger.info(query)
        cur.execute(
            query,
        )
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    update()
