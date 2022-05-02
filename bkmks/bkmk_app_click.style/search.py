""" Module to search the database """

import sqlite3
import click


def search():
    try:
        busca = input(click.style(' What are you searching for? ', fg='red', bold=True))
        conn = sqlite3.connect('bkmk.db')
        cur = conn.cursor()
        query = " SELECT * FROM bkmk_fts WHERE bkmk_fts MATCH '" + busca + "' ORDER BY rank"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(click.style(' [*] ID » ', fg='cyan', bold=True), click.style(str(row[0]), fg='cyan', bold=True))
            print(click.style(' [*] TITLE » ', fg='blue', bold=True), click.style(str(row[1]), fg='blue', bold=True))
            print(click.style(' [*] COMMENT » ', fg='cyan', bold=True), click.style(str(row[2]), fg='cyan', bold=True))
            print(click.style(' [*] LINK » ', fg='blue', bold=True), click.style(str(row[3]), fg='yellow', bold=True))
            print(click.style(' [*] KEYWORD 1 » ', fg='cyan', bold=True), click.style(str(row[4]), fg='cyan', bold=True))
            print(click.style(' [*] KEYWORD 2 » ', fg='blue', bold=True), click.style(str(row[5]), fg='blue', bold=True))
            print(click.style(' [*] KEYWORD 3 » ', fg='cyan', bold=True), click.style(str(row[6]), fg='cyan', bold=True))
            print('\n')
    except sqlite3.Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    search()
