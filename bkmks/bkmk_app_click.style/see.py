""" Module to see all of the database """

import sqlite3
import click


def see():
    try:
        conn = sqlite3.connect("bkmk.db")
        cur = conn.cursor()
        query = """ SELECT * FROM bkmk """
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(click.style(" [*] ID » ", fg="blue", bold=True), click.style(str(row[0]), fg="red", bold=True))
            print(click.style(" [*] TITLE » ", fg="cyan", bold=True), click.style(str(row[1]), fg="yellow", bold=True))
            print(
                click.style(" [*] COMMENT » ", fg="blue", bold=True), click.style(str(row[2]), fg="yellow", bold=True)
            )
            print(click.style(" [*] LINK ? ", fg="cyan", bold=True), click.style(str(row[3]), fg="yellow", bold=True))
            print(
                click.style(" [*] KEYWORD 1 » ", fg="blue", bold=True), click.style(str(row[4]), fg="yellow", bold=True)
            )
            print(
                click.style(" [*] KEYWORD 2 » ", fg="cyan", bold=True), click.style(str(row[5]), fg="yellow", bold=True)
            )
            print(
                click.style(" [*] KEYWORD 3 » ", fg="blue", bold=True), click.style(str(row[6]), fg="yellow", bold=True)
            )
            print(click.style(" [*] TIME » ", fg="cyan", bold=True), click.style(str(row[7]), fg="yellow", bold=True))
            print("\n")
    except sqlite3.Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    see()
