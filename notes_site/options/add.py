"""Collects user input, checks keywords for similarity, if they're new and their frequency.
Sends information to the database and creates the md and html pages."""
import subprocess
import time

import click
from colr import color
from loguru import logger
from mysql.connector import Error, connect
from thefuzz import fuzz  # noqa: F401
from thefuzz import process

fmt = "{time} - {name} - {level} - {message}"
logger.add("logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


class Add:
    """The class starts with user input and a list with all tags in a string list.
    Having them separated will simplify processes. With this information collected,
    first we'll ask the keywords questions and run its processes, one by one.
    After this is done we'll send the information to the database and create the
    md and html files."""

    @logger.catch
    def input_data(self):
        """All the user inputs needed to create a new entry are located here."""
        self.title = input(click.style(" Title? » ", fg="magenta", bold=True))
        self.k1 = input(click.style(" Choose a keyword » ", fg="magenta", bold=True))
        self.k2 = input(click.style(" Choose another... » ", fg="magenta", bold=True))
        self.k3 = input(click.style(" And another... » ", fg="magenta", bold=True))
        print(click.style(" Write a note.", fg="magenta", bold=True))
        time.sleep(0.2)
        self.note = click.edit().rstrip()

    if __name__ == "__main__":
        input_data()

    @logger.catch
    def taglst(self):
        """Union allows to combine two or more sets of results into one, but,
        the number and order of columns that appear in the SELECT statement
        must be the same, and the data types must be equal or compatible.
        Union removes duplicates.
        """
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
            cur = conn.cursor()
            query = "SELECT k1 FROM notes UNION SELECT k2 FROM notes UNION SELECT k3 FROM notes"
            cur.execute(query)
            records = cur.fetchall()  # Results come as one-element tuples. It's needed to turn it to list.
            self.records = [i for t in records for i in t]
            conn.close()
        except Error as e:
            print("Error while connecting to db", e)

    @logger.catch
    def tag_links(self):
        """I'll join the three lists and order them by number of connections."""
        queries = [
            "SELECT k1, count(*) as links FROM notes GROUP BY k1",
            "SELECT k2, count(*) as links FROM notes GROUP BY k2",
            "SELECT k3, count(*) as links FROM notes GROUP BY k3",
        ]
        try:
            for q in queries:
                conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
                cur = conn.cursor()
                query = q
                cur.execute(
                    query,
                )
            self.links = cur.fetchall()
            # Records is a list and row is a tuple with the tag name and number of connections.
            self.links.sort(
                key=lambda x: x[1]
            )  # This sorts the list by the value of the second element. https://tinyurl.com/yfn9alt7
            conn.close()
        except Error as e:
            print("Error while connecting to db", e)

    if __name__ == "__main__":
        tag_links()

    @logger.catch
    def issimilar(self):
        """Uses Thefuzz library to compare keyword strings. If similarity is above 80%,
        it prints a mesage asking if the user wants to change it."""
        conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
        cur = conn.cursor()
        query = "SELECT k1 FROM notes UNION SELECT k2 FROM notes UNION SELECT k3 FROM notes"
        cur.execute(query)
        records = cur.fetchall()  # Results come as one-element tuples. It's needed to turn it to list.
        self.records = [i for t in records for i in t]

        self.keywords = [self.k1, self.k2, self.k3]
        for k in self.keywords:
            value = process.extractOne(k, self.records)
            if (
                80 < value[1] < 100
            ):  # If we don't define it as less that 100, it will show message when inputing a old keyword.
                chg_tag_decision = input(
                    click.style(
                        f"You inputed the word {k}, that is similar to the word {value[0]}, that already is a keyword. Won't you use it instead? [y/n] ",
                        fg="magenta",
                        bold=True,
                    )
                )
                if chg_tag_decision == "y":
                    if k == self.k1:
                        self.k1 = value[0]
                    if k == self.k2:
                        self.k2 = value[0]
                    if k == self.k3:
                        self.k3 = value[0]
            else:
                pass

    if __name__ == "__main__":
        issimilar()

    @logger.catch
    def new_tag(self):
        """Will check the keyword names against the db records. If it doesn't find a
        match, it will produce a message saying the tag is new."""
        self.keywords = [self.k1, self.k2, self.k3]
        for k in self.keywords:
            res = any(k in i for i in self.records)
            if not res:
                print(color(f"[*] - The keyword {k} is new in the database.", fore="#f18892"))
            else:
                pass

    if __name__ == "__main__":
        new_tag()

    @logger.catch
    def count_links(self):
        """Will check the new keywords, see how many links they'll have, and return that
        information."""
        queries = [
            "SELECT k1, count(*) as links FROM notes GROUP BY k1",
            "SELECT k2, count(*) as links FROM notes GROUP BY k2",
            "SELECT k3, count(*) as links FROM notes GROUP BY k3",
        ]
        for q in queries:
            conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
            cur = conn.cursor()
            query = q
            cur.execute(
                query,
            )
        self.links = cur.fetchall()

        for i in self.links:
            if i[0] == self.k1:
                new_i = list(i)
                new_val = [new_i[0], (new_i[1] + 1)]
                print(color(f"[*] - The updated value of the keyword links is {new_val}", fore="#c6f188"))
            if i[0] == self.k2:
                new_i = list(i)
                new_val = [new_i[0], (new_i[1] + 1)]
                print(color(f"[*] - The updated value of the keyword links is {new_val}", fore="#c6f188"))
            if i[0] == self.k3:
                new_i = list(i)
                new_val = [new_i[0], (new_i[1] + 1)]
                print(color(f"[*] - The updated value of the keyword links is {new_val}", fore="#c6f188"))

    if __name__ == "__main__":
        count_links()

    @logger.catch
    def add_to_db(self):
        """Creates the urls for pages and sends the data to the database"""
        self.pg_tit = self.title.replace(" ", "_").replace("'", "")
        self.md_path = "/srv/http/notes/pages/markdown/" + self.pg_tit + ".md"
        self.url = "http://localhost/notes/pages/html/" + self.pg_tit + ".html"
        answers = [self.title, self.k1, self.k2, self.k3, self.note, self.url]
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
            cur = conn.cursor()
            query = "INSERT INTO notes (title, k1, k2, k3, note, url) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(query, answers)
            conn.commit()
            conn.close()
        except Error as e:
            print("Error while connecting to db", e)
        print(color(f"[*] - The entry named: {self.title}, was added to the database.", fore="#acac87"))

    if __name__ == "__main__":
        add_to_db()

    @logger.catch
    def add_md_page(self):
        """We create a new markdown file in its folder and write to it, the content
        of the meta-data, and the note."""
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
            cur = conn.cursor()
            query = "select * from notes order by ntid desc limit 1"
            cur.execute(
                query,
            )
            records = cur.fetchall()
            conn.close()
        except Error as e:
            print("Error while connecting to db", e)

        for row in records:
            id = row[0]
            titulo = row[1]
            time = row[7]
            k1 = row[2]
            k2 = row[3]
            k3 = row[4]
            nota = row[5]

        with open(self.md_path, "w") as f:
            f.write("---")
            f.write("\n")
            f.write("id: " + str(id))
            f.write("\n")
            f.write("title: " + titulo)
            f.write("\n")
            f.write("author: mclds")
            f.write("\n")
            f.write("time: " + str(time))
            f.write("\n")
            f.write("tags: " + k1 + ", " + k2 + ", " + k3)
            f.write("\n")
            f.write("---")
            f.write("\n")
            f.write(nota)
        print(color(f"[*] - It was created the markdown file named, {self.md_path}.", fore="#acac87"))

    if __name__ == "__main__":
        add_md_page()

    @logger.catch
    def add_html_page(self):
        """Where we create a html version of the markdown file.
        We just convert the md file into an html one, and
        put it in the html folder."""
        html_path = "/srv/http/notes/pages/html/" + self.pg_tit + ".html"
        cmd = "touch " + html_path
        subprocess.run(cmd, shell=True)
        cmd = (
            "pandoc --highlight-style=zenburn --metadata title='"
            + self.title
            + "' -s '"
            + self.md_path
            + "' -o '"
            + html_path
            + "'"
        )
        subprocess.run(cmd, shell=True)
        print(color(f"[*] - It was created the html file named, {self.url}.", fore="#acac87"))

    if __name__ == "__main__":
        add_html_page()
