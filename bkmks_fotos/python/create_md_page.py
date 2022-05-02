"""Module Docstring"""
from loguru import logger
from mysql.connector import connect, Error
import subprocess

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch
def create_md_page():
    """We create a new markdown file in its folder and write to it, the content
    of the meta-data, and the bkmk."""
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = "SELECT * FROM bkmks"
        cur.execute(
            query,
        )
        records = cur.fetchall()
        for row in records:
            title = str(row[1])
            change_tit = title.replace(" ", "_")
            change_tit1 = change_tit.replace("/", "")
            filename = change_tit1 + ".md"
            logger.info(filename)
            writepath = "/srv/http/bkmks_fotos/md_files/" + filename
            logger.info(writepath)
            with open(writepath, "w+") as file:
                file.write("id: ")
                file.write(str(row[0]))
                file.write("\n")
                file.write("title: ")
                file.write(str(row[1]))
                file.write("\n")
                file.write("tags: ")
                file.write(str(row[4]))
                file.write(", ")
                file.write(str(row[5]))
                file.write(", ")
                file.write(str(row[6]))
                file.write("\n")
                file.write("time: ")
                file.write(str(row[8]))
                file.write("\n")
                file.write("\n")
                file.write(str(row[2]))
                file.write("\n")
                file.write("\n")
                file.write("![](http://localhost/bkmks_fotos/pics/" + str(row[7]) + ")")
                file.write("\n")
                file.write("[LINK](row[3])")

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_md_page()
