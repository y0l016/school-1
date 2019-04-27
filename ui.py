import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

class Window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="craftit")
        self.set_size_request(500, 500)

        self.vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL,
                            spacing=6)
        self.add(self.vbox)

        # the user input after they press enter
        self.entry_text = ""

        # creates the widgets needed and aligns them
        self._create_textview()
        self._create_entry()

    def _create_textview(self):
        scrolledwindow = gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.vbox.pack_start(scrolledwindow, True, True, 0)

        self.textview = gtk.TextView()
        self.textview.set_editable(False)
        self.textbuffer = self.textview.get_buffer()

    def show_image(self, image_path):
        pass

    def show_text(self, text):
        pass

    def _create_entry(self):
        self.entry = gtk.Entry()
        self.vbox.pack_start(self.entry, True, True, 0)
        self.entry.connect("activate", self._do_enter_entry)

    def _do_enter_entry(self, entry):
        self.entry_text = self.entry.get_text()
        self.entry.set_text("")

    def get_input(self):
        return self.entry_text
