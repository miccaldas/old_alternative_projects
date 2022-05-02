#!/usr/bin/env python3
"""Encrypted version of the Micro Blog. Now done with Peewee ORM"""
import sys
import os
from collections import OrderedDict
import datetime
from loguru import logger
from getpass import getpass
from peewee import *
from playhouse.sqlcipher_ext import SqlCipherDatabase
from colr import color

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)

# Defer initialization of the database until the script is executed from the
# command-line.
db = SqlCipherDatabase(None)


class Entry(Model):
    """Defines table and its structure"""

    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        """ """

        database = db


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def initialize():
    """Defines db connection and a
    db table.
    """
    pwd = str(os.environ["MICRO_PWD"])
    db.init("micro_blog.db", passphrase=pwd)
    Entry.create_table()


@logger.catch
def menu_loop():
    """Sets the loop where the all application will run."""
    choice = None
    while choice != "q":
        for key, value in menu.items():
            print(color("%s) %s" % (key, value.__doc__), fore="#c3bcb1"))
        choice = input(color("Actions: ", fore="#c3bcb1")).lower().strip()
        if choice in menu:
            menu[choice]()


@logger.catch
def add_entry():
    """Add Entry"""
    print(color("Enter your entry. Press ctrl+d when finished.", fore="#c3bcb1"))
    data = sys.stdin.read().strip()
    if data and input(color("Save entry? [Yn] ", fore="#c3bcb1")) != "n":
        Entry.create(content=data)
        print(color("Saved successfully.", fore="#a4bdba"))


@logger.catch
def view_entries(search_query=None):
    """View previous entries"""
    query = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        query = query.where(Entry.content.contains(search_query))

    for entry in query:
        timestamp = entry.timestamp.strftime("%A %B %d, %Y %I:%M%p")
        print("\n")
        print(color(timestamp, fore="#a4bdba"))
        print(color("=" * len(timestamp), fore="#a4bdba"))
        print(color(entry.content, fore="#c3bcb1"))
        print(color("n) next entry", fore="#a4bdba"))
        print(color("d) delete entry", fore="#a4bdba"))
        print(color("q) return to main menu", fore="#a4bdba"))
        if input(color("Choice? (Nq) ", fore="#a4bdba")) == "q":
            break


@logger.catch
def search_entries():
    """Search entries"""
    view_entries(input(color("Search query: ", fore="#c3bcb1")))


@logger.catch
def delete_entry():
    """Deletes entry in database"""
    del_id = input(color("What is the ID of the entry you want to delete? "))
    del_row = Entry.delete().where(Entry.id == del_id)
    del_row.execute()


@logger.catch
def update_query():
    """Updates a value in a row"""
    updt_id = input(color("What is the id of your update? ", fore="#a4bdba"))
    Entry.updt_column = input(color("What column do you want to update? ", fore="#a4bdba"))
    updt_content = input(color("What is it you want to change? ", fore="#a4bdba"))
    updt_val = Entry.update({Entry.updt_column: updt_content}).where(Entry.id == updt_id)
    updt_val.execute()


menu = OrderedDict(
    [
        ("a", add_entry),
        ("v", view_entries),
        ("s", search_entries),
        ("d", delete_entry),
        ("u", update_query),
    ]
)


if __name__ == "__main__":
    # Collect the passphrase using a secure method.
    pwd = str(os.environ["MICRO_PWD"])
    if pwd is None:
        passphrase = getpass(color("Enter password: ", fore="#c3bcb1"))
        if passphrase != pwd:
            sys.stderr.write("Passphrase required to access diary.\n")
            sys.stderr.flush()
            sys.exit(1)

    # Initialize the database.
    initialize()
    menu_loop()
