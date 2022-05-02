"""Here we gather all files and use them to create a query to the db"""
import sys
from mysql.connector import connect, Error
from loguru import logger


fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)


def connections():
    """We'll read the files and send the information to the db"""
    f_title = open("title.txt", "r")
    f_k1 = open("k1.txt", "r")
    f_k2 = open("k2.txt", "r")
    f_k3 = open("k3.txt", "r")
    f_comment = open("comment.txt", "r")
    f_link = open("link.txt", "r")

    post_title = f_title.read()
    post_link = f_link.read()
    post_comment = f_comment.read()
    post_k1 = f_k1.read()
    post_k2 = f_k2.read()
    post_k3 = f_k3.read()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        answers = [post_title, post_link, post_comment, post_k1, post_k2, post_k3]
        query = """ INSERT INTO bkmks (title, comment, link, k1, k2, k3) VALUES (%s, %s, %s, %s, %s, %s) """
        cur.execute(query, answers)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    f_title.close()
    f_comment.close()
    f_link.close()
    f_k1.close()
    f_k2.close()
    f_k3.close()


if __name__ == "__main__":
    connections()
