""" Module to delete bookmarks from the database """

import sqlite3
import click


def delete():
    ident = input(click.style(' ID to delete? » ', fg='red', bold=True))

    try:
        conn = sqlite3.connect('bkmk.db')
        cur = conn.cursor()
        query = " DELETE FROM bkmk WHERE id = " + ident
        cur.execute(query)
        conn.commit()

    except sqlite3.Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    delete()
