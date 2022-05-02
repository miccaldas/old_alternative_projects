"""Adding a new note. k1 question"""
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
        texto = u"%s" % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "white", "#5f8787", "bold"),
    ("streak", "white", "#5f8787", "bold"),
    ("bg", "white", "#5f8787", "bold"),
]

edit = urwid.Edit(("banner", u"ID ?.\n"), align="center")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()

f = open("id.txt", "w")
f.write(edit.get_edit_text())
f.close()
