"""Adding a new note. Title question"""
import sys
import urwid
from loguru import logger


fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)


def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    """We'll create a tui window in urwid to ask the question"""

    def keypress(self, size, key):
        if key != "enter":
            return super(QuestionBox, self).keypress(size, key)
        texto = u"%s.\n\nPRESS Q TO EXIT." % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "black", "light gray", "bold"),
    ("streak", "black", "light gray", "bold"),
    ("bg", "black", "light gray", "bold"),
]

edit = urwid.Edit(("banner", u"WHAT IS THE TITTLE?\n"), align="center")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()

f = open("title.txt", "w")
f.write(edit.get_edit_text())
f.close()
