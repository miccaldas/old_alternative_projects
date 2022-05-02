"""Searches entries in db """
import sys
from mysql.connector import connect, Error
import urwid
from loguru import logger
from colr import color


fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)


def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    """Create the window and asks what is search keyword"""

    def keypress(self, size, key):
        if key != "enter":
            return super(QuestionBox, self).keypress(size, key)
        texto = u"%s" % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "white", "#5f8787", "bold"),
    ("streak", "white", "#5f8787", "bold"),
    ("bg", "white", "#5f8787", "bold"),
]

edit = urwid.Edit(("banner", u"WHAT ARE YOU LOOKING FOR?\n"), align="center")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()


def search():
    """Connects to db and gets results of query"""
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = (
            " SELECT * FROM bkmks WHERE MATCH(title, comment, link, k1, k2, k3) AGAINST ('"
            + str(edit.get_edit_text())
            + "' IN NATURAL LANGUAGE MODE)"
        )
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


if __name__ == "__main__":
    search()
