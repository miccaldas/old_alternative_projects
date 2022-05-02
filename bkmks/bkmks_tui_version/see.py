""" Module to see all of the database """

from mysql.connector import connect, Error
from colr import color
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


def see():
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """ SELECT * FROM bkmks """
        logger.info(query)
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(" [*] ID » ", fore="#85a585"), color(str(row[0]), fore="#fdf3d3"))  # 1
            print(color(" [*] TITLE » ", fore="#85a585"), color(str(row[1]), fore="#fdf3d3"))
            print(color(" [*] COMMENT » ", fore="#85a585"), color(str(row[2]), fore="#fdf3d3"))
            print(color(" [*] LINK ? ", fore="#85a585"), color(str(row[3]), fore="#f29b85"))
            print(color(" [*] KEYWORD 1 » ", fore="#85a585"), color(str(row[4]), fore="#fdf3d3"))
            print(color(" [*] KEYWORD 2 » ", fore="#85a585"), color(str(row[5]), fore="#fdf3d3"))
            print(color(" [*] KEYWORD 3 » ", fore="#85a585"), color(str(row[6]), fore="#fdf3d3"))
            print(color(" [*] TIME » ", fore="#85a585"), color(str(row[7]), fore="#fdf3d3"))
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    see()

# 1)
# Because of the problem of the bkmk_fts_content replicating the id field,
# which I still don't understand why, if you start the the row count from
# '0', the id and title will be exactly the same, and all the fields will
# be wrong. In the case of 'see' function, that reads the 'bkmk' table,
# you have to start the count from '1', for the headers are correctly
# aligned with the values.
# If you're reading the 'bkmk_fts' table, you don't need to change nothing.
# Hacky I know, bu it seems to work for now.
