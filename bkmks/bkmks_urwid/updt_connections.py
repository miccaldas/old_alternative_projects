"""Here we gather all files and use them to create a query to the db"""
import sys
from mysql.connector import connect, Error
from loguru import logger


fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)


def connections():
    """We'll read the files and send the information to the db"""
    f_column = open("column.txt", "r")
    f_id = open("id.txt", "r")
    f_update = open("update.txt", "r")

    post_column = f_column.read()
    post_id = f_id.read()
    post_update = f_update.read()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = "UPDATE bkmks SET " + post_column + " = '" + post_update + "' WHERE id = " + post_id
        cur.execute(
            query,
        )
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    f_column.close()
    f_id.close()
    f_update.close()


if __name__ == "__main__":
    connections()
