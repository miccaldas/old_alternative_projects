""" Module to search the database """
import subprocess
from mysql.connector import connect, Error
from colr import color
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="DEBUG", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


def search():
    try:
        busca = input(color(" What are you searching for? ", fore="#f29b85"))
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = (
            " SELECT * FROM bkmks WHERE MATCH(title, comment, link, k1, k2, k3) AGAINST ('"
            + busca
            + "' IN NATURAL LANGUAGE MODE)"
        )
        logger.info(query)
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
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
    logger.info(subprocess.run("python /home/mic/scripts/logging/mysql_journalctl.py", shell=True))


if __name__ == "__main__":
    search()
