"""Defines the setup of where the posts will be written"""
import urwid


def exit_on_q(key):
    """
    Sets q/Q as the keys to exit Urwid
    main loop.

    Args:
        key: str, Exits application main loop
    """
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    """Urwid class that defines a box with editable content"""

    def keypress(self, size, key):
        """
        Defines what keypresses will be taken into account for
        the application.

        Args:
            key: str, Return all keypresses, except enter, that
            is used as 'activate'.
            texto: str, Reminds user of the exit key.
        """
        if key != "enter":
            return super(QuestionBox, self).keypress(size, key)
        texto = u"%s.\n\nPress Q to exit." % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "white", "#ff6f69"),
    ("streak", "white", "light red"),
    ("bg", "white", "#ff6f69"),
]

edit = urwid.Edit(("banner", u"   DEITA CÀ PRA FORA!  \n"), align="center")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()

f = open("post.txt", "w")
f.write(edit.get_edit_text())
f.close()
