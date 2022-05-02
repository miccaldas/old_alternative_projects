"""Module that encompasses all bookmark app functionality in  one class"""
from loguru import logger
from prompt_toolkit.shortcuts import input_dialog
from mysql.connector import connect, Error
from colr import color

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


class Add:
    """Contains all functionalities for bookmarks app.

    This class has no __init__ generator nor does it have variables used by several methods.
    The value instantiation of the class is done by input variables that are defined when
    the methods are run.


    """

    @logger.catch
    def add_bkmk(self):
        """Adds new bookmark to database

        :param title: str, Title of the bookmark
        :param comment: str, Small explanation on the nature of the bookmark
        :param link: str, URL of the bookmark
        :param k1: str, Bookmark keyword
        :param k2: str, Bookmark keyword
        :param k3: str, Bookmark keyword
        :param answers: list, Collects all input results in a list
        :param query: str, Collects all input values and creates a SQL query
                       to add a new bookmark
        :param conn: list, Collects strings to connect to the database
        :param cur.execute: str/list, Feeds MySQL with query and arguments
        :raises MySQL.error as e: Error while connecting to db

        """
        title = input_dialog(title="Title", text="What is the title? ").run()
        comment = input_dialog(title="Comment", text="What is your comment? ").run()
        link = input_dialog(title="Link", text="What is the link? ").run()
        k1 = input_dialog(title="K1", text="Choose a keyword ").run()
        k2 = input_dialog(title="K2", text="Choose another... ").run()
        k3 = input_dialog(title="K3", text="And another...").run()

        answers = [title, comment, link, k1, k2, k3]
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

    @logger.catch
    def delete(self):
        """Erases from the database a given bookmark record

        We must use 'ident', not 'id' in choosing the variable name,
        as the latter is a reserved word

        :param ident: int, ID number of bookmark record to erase
        :param query: str, MySQL query that encodes the delete command for the database
        :param conn: list, Collects strings to connect to the database
        :param cur.execute: str/list, Feeds MySQL with query and arguments
        :raises MySQL.error as e: Error while connecting to db

        """
        ident = input_dialog(title="Delete Entry", text="What is the ID? ").run()
        logger.info(ident)

        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
            cur = conn.cursor()
            query = " DELETE FROM bkmks WHERE id = " + ident
            logger.info(query)
            cur.execute(query)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()

    @logger.catch
    def see(self):
        """Prints out the database content in formatted text

        :param query: str, Selects all entries in database, prints them line by line
        :param conn: list, Collects strings to connect to the database
        :param cur.execute: str/list, Feeds MySQL with query and arguments
        :returns: (id,
                                    title,
                                    comment,
                                    link,
                                    keyword,
                                    keyword,
                                    keyword)
        :rtype: Prints by bookmark
        :raises MySQLerror as e: Error while connecting to db

        """

        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
            cur = conn.cursor()
            query = """ SELECT * FROM bkmks """
            logger.info(query)
            cur.execute(query)
            records = cur.fetchall()
            for row in records:
                print(color(" [*] ID » ", fore="#928b7f"), color(str(row[0]), fore="#ffffff"))  # 1
                print(color(" [*] TITLE » ", fore="#928b7f"), color(str(row[1]), fore="#ffffff"))
                print(color(" [*] COMMENT » ", fore="#928b7f"), color(str(row[2]), fore="#ffffff"))
                print(color(" [*] LINK ? ", fore="#928b7f"), color(str(row[3]), fore="#a2cff0"))
                print(color(" [*] KEYWORD 1 » ", fore="#928b7f"), color(str(row[4]), fore="#ffffff"))
                print(color(" [*] KEYWORD 2 » ", fore="#928b7f"), color(str(row[5]), fore="#ffffff"))
                print(color(" [*] KEYWORD 3 » ", fore="#928b7f"), color(str(row[6]), fore="#ffffff"))
                print(color(" [*] TIME » ", fore="#928b7f"), color(str(row[7]), fore="#ffffff"))
                print("\n")
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()

    @logger.catch
    def search(self):
        """Gets a keyword from user and returns all records with that
        keyword.

        :param busca: str, user input. "What are you searching for?"
        :param conn: list, connects to the database with db id data
        :param query: str, Select from db where keyword matches text
                        in all other columns
        :param cur.execute: str/list, Executes the query and its data
        :returns: list, collects all records that have the
                               search term and prints it to stdout
                               in formatted text.
        :rtype: records
        :raises MySQLerror as e: Error while connecting to db

        """
        try:
            busca = input_dialog(title="Search Bookmarks", text="What are you searching for? ").run()
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
                print(color(" [*] ID » ", fore="#928b7f"), color(str(row[0]), fore="#ffffff"))
                print(color(" [*] TITLE » ", fore="#928b7f"), color(str(row[1]), fore="#ffffff"))
                print(color(" [*] COMMENT » ", fore="#928b7f"), color(str(row[2]), fore="#ffffff"))
                print(color(" [*] LINK ? ", fore="#928b7f"), color(str(row[3]), fore="#ffffff"))
                print(color(" [*] KEYWORD 1 » ", fore="#928b7f"), color(str(row[4]), fore="#ffffff"))
                print(color(" [*] KEYWORD 2 » ", fore="#928b7f"), color(str(row[5]), fore="#ffffff"))
                print(color(" [*] KEYWORD 3 » ", fore="#928b7f"), color(str(row[6]), fore="#ffffff"))
                print(color(" [*] TIME » ", fore="#928b7f"), color(str(row[7]), fore="#ffffff"))
                print("\n")
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()

    @logger.catch
    def update(self):
        """Asks for column, id number and update text, and alters a
        database record.

        :param coluna: str, user input. "Column?"
        :param ident: int, user input. "ID?"
        :param update: str, user input. "Write your update."
        :param conn: list, connects to the database
        :param query: str, "Update db set coluna X = update_text where ID = ident"
        :param cur.execute: str/list, Executes the query and its data
        :raises MySQLerror as e: Error while connecting to db

        """

        coluna = input_dialog(title="Update Column", text="Column? ").run()
        ident = input_dialog(title="Entry ID", text="ID? ").run()
        update = input_dialog(title="Update Text", text="Write your update.").run()

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
