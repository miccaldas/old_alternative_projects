"""Module that inserts to database the values collected from the other files"""
from mysql.connector import connect, Error


def connections():
    """
    Opens two files and drops their content
    into a database.

    Args:
        f: file, file with post text, open for reading
        f_tags: file, file with the tags belonging to said post
        conn: list, connects to the database
        answers: list, collects the post text and the tags text in a list
        query: str, "Insert into db (text, tags) VALUES (X, X)"
        cur.execute: tuple, Executes the SQL query

    Raise:
        MySQLerror as e: Error while connecting to db
    """
    f = open("post.txt", "r")
    f_tags = open("tags.txt", "r")

    post_content = f.read()
    tags_content = f_tags.read()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="micro_diary")
        cur = conn.cursor()
        answers = [post_content, tags_content]
        query = """ INSERT INTO micro_diary (text, tags) VALUES (%s, %s) """
        cur.execute(query, answers)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    f.close()
    f_tags.close()


if __name__ == "__main__":
    connections()
