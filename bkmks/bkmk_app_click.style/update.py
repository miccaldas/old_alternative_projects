""" Module to update bookmarks to database """
import time
import sqlite3
import click


def update():
    coluna = input(click.style(' Column? » ', fg='red', bold=True))
    ident = input(click.style(' ID? » ', fg='red', bold=True))
    print(click.style(' Write your update', fg='red', bold=True))
    time.sleep(0.3)
    update = click.edit()

    try:
        conn = sqlite3.connect('bkmk.db')
        cur = conn.cursor()
        query = " UPDATE bkmk SET " + coluna + " = '" + update + "' WHERE id = " + ident
        print(query)
        cur.execute(query)
        conn.commit()

    except sqlite3.Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    update()
