#!/usr/bin/python3.9
"""Main Module of the App. Where all the commands are accessed from"""
import sys
import subprocess
import urwid
from urwid import Button, Signals, connect_signal
from loguru import logger


fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt)
logger.add("error.log", level="ERROR", format=fmt)


choices = u"Add, See, Search, Delete, Update, Exit".split()


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        menu.button = urwid.Button(c)
        logger.info(menu.button)
        urwid.connect_signal(menu.button, "click", item_chosen, c)
        body.append(urwid.AttrMap(menu.button, None, focus_map="reversed"))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button, choice):
    response = urwid.Text([choice])
    hidden = urwid.Button(u"")
    urwid.connect_signal(hidden, "click", exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response, urwid.AttrMap(hidden, None)]))
    item_chosen.pick = str(choice[:-1])  # Result comes with trailing comma. This gets rid of it.


def exit_program(button):
    raise urwid.ExitMainLoop()


main = urwid.Padding(menu(u"Bookmarks", choices), left=2, right=2)
top = urwid.Overlay(
    main,
    urwid.SolidFill(u"\N{MEDIUM SHADE}"),
    align="center",
    width=("relative", 60),
    valign="middle",
    height=("relative", 60),
    min_width=20,
    min_height=9,
)
urwid.MainLoop(top, palette=[("reversed", "standout", "")]).run()


def main():
    if item_chosen.pick == "Add":
        subprocess.run("python add_title.py", shell=True)
        subprocess.run("python add_comment.py", shell=True)
        subprocess.run("python add_link.py", shell=True)
        subprocess.run("python add_k1.py", shell=True)
        subprocess.run("python add_k2.py", shell=True)
        subprocess.run("python add_k3.py", shell=True)
        subprocess.run("python connections.py", shell=True)
    if item_chosen.pick == "See":
        subprocess.run("python see.py", shell=True)
    if item_chosen.pick == "Search":
        subprocess.run("python  search.py", shell=True)
    if item_chosen.pick == "Delete":
        subprocess.run("python delete.py", shell=True)
    if item_chosen.pick == "Update":
        subprocess.run("python update_column.py", shell=True)
        subprocess.run("python update_id.py", shell=True)
        subprocess.run("python update_update.py", shell=True)
        subprocess.run("python updt_connections.py", shell=True)
    if item_chosen.pick == "Exit":
        sys.exit()


if __name__ == "__main__":
    main()
