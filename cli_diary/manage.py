#!/usr/bin/python3
"""
We use here for the first time the Click cli system.
In order to try something new, It was put here all
management functions that do not need to visualize
the database content. That will be treated in another
module, hopefully, in a new manner.
"""
from datetime import datetime

import click
import isort
import snoop
from loguru import logger
from mysql.connector import Error, connect
from snoop import pp

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@click.command()
@click.option("-t", "--title", default=datetime.today().strftime("%d-%m-%Y"))
@click.option("--k1")
@click.option("--k2")
@snoop
def new(title, k1, k2):
    """
    Collects the options values, adds the
    entry value and send them to the db.
    """
    entry = click.edit().rstrip()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_diary")
        cur = conn.cursor()
        query = "INSERT INTO cli_diary (title, entry, k1, k2) VALUES (%s, %s, %s, %s)"
        answers = [title, entry, k1, k2]
        cur.execute(query, answers)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    new()


@logger.catch
@click.command()
@click.option("--id")
@snoop
def delete(id):
    """
    Deletes entries from the db.
    """
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_diary")
        cur = conn.cursor()
        query = "DELETE FROM cli_diary WHERE id = %s"
        answers = [id]
        cur.execute(query, answers)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete()


@logger.catch
@click.command()
@click.option("--id")
@snoop
def update(id):
    """
    Updates values in the db.
    The reason why 'column' is
    an input field and not a
    command line option is that
    strings in options get quotes
    around them, and MySQL doesn't
    like that.
    """

    column = input(click.style("What column do you want to update? ", fg="bright_white", bold=True))
    updt = click.edit().rstrip()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_diary")
        cur = conn.cursor()
        answer = [column, updt, id]
        query = "UPDATE cli_diary SET %s = %s WHERE id = %s"
        cur.execute(query, answer)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    update()
