import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NumberEntry(Gtk.Entry):
    def __init__(self, limit=0):
        Gtk.Entry.__init__(self)
        self.limit = limit
        self.connect('changed', self.on_changed)

    def on_changed(self, *args):
        text = self.get_text().strip()
        self.set_text(''.join([i for i in text if i in '0123456789']))
        
        if self.get_text() != "":
            if self.limit != 0:
                if int(self.get_text()) > self.limit:
                    self.set_text(str(self.limit))