"""Here we'll be hosted all functions that deal with data visualization."""
import click
import isort
import snoop
from loguru import logger
from mysql.connector import Error, connect
from snoop import pp
from clint.textui import puts, indent

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @logger.catch
@click.command()
# @snoop
def see():
    """
    We use the Rich library to decorate the output.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_diary")
        cur = conn.cursor()
        query = """ SELECT * FROM cli_diary ORDER BY rand()"""
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(f"    [{row[0]}]")
            print(f"    {row[1]}")
            print(f"    {row[2]}")
            print("    @" + row[3] + ", @" + row[4])
            print("     ------------------------------------------------------------")
            print("\n")
            conn.close()
    except Error as e:
        print("Error while connecting to db", e)


if __name__ == "__main__":
    see()
