"""Collects the bookmark tags written by the user"""
import urwid


def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


class Tags(urwid.Filler):
    """
    Urwid filler is a widget that is in the background and
    occupies empty space.
    """

    def keypress(self, size, key):
        if key != "enter":
            return super(Tags, self).keypress(size, key)
        texto = u"%s.\n\nPress Q to exit." % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "white", "#ff6f69"),
    ("streak", "", ""),
    ("bg", "white", "#ff6f69"),
]

edit = urwid.Edit(u"Tags:\n\n", align="center")
fill = Tags(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()

f = open("tags.txt", "w")
f.write(edit.get_edit_text())
f.close()
