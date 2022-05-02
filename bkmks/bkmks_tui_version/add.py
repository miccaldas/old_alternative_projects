""" Module to insert bookmarks to database """
import sys
import subprocess
from datetime import datetime
from mysql.connector import connect, Error
from colr import color
from loguru import logger

now = datetime.now()
agora = now.strftime("%Y-%m-%d %H:%M:%S")

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch
def add():
    titulo = input(color(" Title? » ", fore="#f29b85"))
    comentario = input(color(" Comment » ", fore="#f29b85"))
    link = input(color(" Link » ", fore="#f29b85"))
    kwd1 = input(color(" Choose a keyword » ", fore="#f29b85"))
    kwd2 = input(color(" Choose another ... » ", fore="#f29b85"))
    kwd3 = input(color(" And another... » ", fore="#f29b85"))

    answers = [titulo, comentario, link, kwd1, kwd2, kwd3]
    logger.info(answers)

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """INSERT INTO bkmks (title, comment, link, k1, k2, k3) VALUES (%s, %s, %s, %s, %s, %s)"""
        logger.info(query)
        cur.execute(query, answers)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    add()
