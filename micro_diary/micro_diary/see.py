"""Prints the whole content of the database"""
from mysql.connector import connect, Error
import urwid


def exit_on_q(key):
    """Defines characters that will exit Urwid main loop"""
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


def see():
    """
    Prints all the database

    Args:
        palette: list, List of tuples with app colors definitions
        conn: list, Connects to the database
        query: str, "Select all from the db"
        records: dict, Fetch all db records and print them
        txt: str, Defines how the db will be shown in the app

    Returns:
        records, dict, Database print

    Raises:
        MySQLerror as e: Error while connecting to the db
    """
    palette = [
        ("banner", "white", "#ff6f69"),
        ("streak", "white", "light red"),
        ("bg", "white", "#ff6f69"),
    ]

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="micro_diary")
        cur = conn.cursor()
        query = "SELECT * FROM micro_diary"
        cur.execute(
            query,
        )
        records = cur.fetchall()
        for row in records:
            txt = urwid.Text(("banner", "%s\n\n%s" % (row[1], row[2])), align="center")
            fill = urwid.Filler(txt)
            loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
            loop.screen.set_terminal_properties(colors=256)
            loop.widget = urwid.AttrMap(fill, "bg")
            loop.run()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    see()
