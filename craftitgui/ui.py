"""
this file handles all the ui elements.
provides the Window class which can be used to spawn
a Gtk window.
the Window class has several helper functions that the
frontend can use to display text, image and get what
the user has last entered.
"""

import gi
import os
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf

import config

# TODO: fix image scaling

# utilities
def _hex2rgb(hex: str) -> [float]:
    """
    convert hex to rgb list
    """
    if hex is None:
        return None

    if '#' == hex[0]:
        hex = hex[1:]

    r = hex[0:2]
    g = hex[2:4]
    b = hex[4:]

    return [int(i, 16)/255.0 for i in (r, g, b)]

class ImageNotFoundError(Exception):
    """
    the given image cannot be found. raised in the Window class
    """
    pass

class Window(Gtk.Window):
    def __init__(self, config_path=config.CONFIG):
        """
        doesn't need any mandatory argument.
        optional arguemnt:
        config_path -> path to config file.
        falls back to AppData/craftitgui in nt
            XDG_CONFIG_HOME/craftitgui in posix
            falls back to ~/.config in case if env var is not defined
        """
        Gtk.Window.__init__(self, title="craftit")
        self.set_size_request(500, 500)

        self.conf = config.get_config(config_path)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        # the user input after they press enter
        self.entry_text = ""

        # creates the widgets needed and aligns them
        self._create_textview()
        self._create_entry()

    def main(self, func_do_enter):
        """
        starts running the main loop.
        arguments:
        func_do_enter -> function that should be run after the user
        presses enter.
        """
        self.func_do_enter = func_do_enter
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def _modify_color(self, widget, color_field):
        """
        modify given widget's color to color_field.
        if fg is in the color_field, it changes the fg color.
        """
        _ = _hex2rgb(config.get_color_field(self.conf, color_field))

        if "fg" in color_field:
            widget.override_color(Gtk.StateType.NORMAL,
                                  Gdk.RGBA(_[0], _[1], _[2]))
        else:
            widget.override_background_color(Gtk.StateType.NORMAL,
                                             Gdk.RGBA(_[0], _[1], _[2]))

    def _create_textview(self):
        """
        creates a textview which makes displaying both image and text
        possible. creates textview in a scrolled window so the user
        can scroll back.
        sets the window color's f/bg to window_f/bg in config
        """
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        self.grid.attach(self.scrolledwindow, 0, 0, 100, 90)

        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        padding = self.conf.get("padding", 5)
        self.textview.set_bottom_margin(padding)
        self.textview.set_top_margin(padding)
        self.textview.set_right_margin(padding)
        self.textview.set_left_margin(padding)

        self._modify_color(self.textview, "window_bg")
        self._modify_color(self.textview, "window_fg")

        self.textbuffer = self.textview.get_buffer()
        self.scrolledwindow.add(self.textview)

    def show_image(self, image_path):
        """
        display an image in the text view.
        arguments:
        image_path -> relative/abs path to the image
        raises:
        raises ImageNotFoundError if the file does not exist or
        if GdkPixBuf cannot create an object from the file path
        """
        try:
            image_path = os.path.abspath(image_path)
        except:
            print(f"error: cannot load image {image_path}", file=sys.stderr)
            raise ImageNotFoundError
        try:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image_path, 50,
                                                             50, True)
        except:
            print(f"error: cannot load image {image_path}", file=sys.stderr)
            raise ImageNotFoundError

        self.add_text("")
        self.textbuffer.insert_pixbuf(self.textbuffer.get_end_iter(), pixbuf)

    def add_text(self, text):
        # TODO: consider making text a tuple? *text
        """
        add text to the textview.
        argument:
        text -> text to display
        """
        self.textbuffer.insert(self.textbuffer.get_end_iter(),
                               f"\n{text}")

    def _create_entry(self):
        """
        create an entry and place it below the scrolledwindow.
        also makes a prompt window left to the entry and set its
        prompt to `prompt` value in config. falls back to `>` if
        it is not defined.
        """
        prompt_label = Gtk.Label()
        prompt_label.set_text(self.conf.get("prompt", ">"))
        prompt_label.set_selectable(False)
        prompt_label.set_justify(Gtk.Justification.RIGHT)
        self._modify_color(prompt_label, "window_bg")
        self._modify_color(prompt_label, "window_fg")

        self.grid.attach_next_to(prompt_label, self.scrolledwindow,
                                 Gtk.PositionType.BOTTOM, 2, 10)

        self.entry = Gtk.Entry()
        self.grid.attach_next_to(self.entry, prompt_label,
                                 Gtk.PositionType.RIGHT, 98, 10)

        self.entry.connect("activate", self._do_enter_entry)
        self.entry.set_inner_border(None)
        self._modify_color(self.entry, "input_bg")
        self._modify_color(self.entry, "input_fg")

    def _do_enter_entry(self, entry):
        """
        do the things that needs to be done after a user presses enter.
        calls func_do_enter given in main among other things
        """
        self.entry_text = self.entry.get_text()
        self.entry.set_text("")

        self.func_do_enter()

    def get_input(self):
        """
        return what the user has last entered.
        """
        return self.entry_text
