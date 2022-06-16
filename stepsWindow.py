import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from numbify import NumberEntry

class askForSteps(Gtk.Window):
    def __init__(self, parent):
        super().__init__(title="Antes de iniciar", transient_for=parent)

        self.set_default_size(400, 200)
        self.set_border_width(10)

        lbl_labels = []
        lbl_values = []

        # Label - Pasos
        lbl_steps = Gtk.Label(label="Pasos a ejecutar")

        # Entry - Pasos
        self.ent_steps = NumberEntry()
        self.ent_steps.set_placeholder_text("Numero de pasos")
        self.ent_steps.connect("changed", self.check)

        # Boton - Confirmar pasos
        self.btn_steps_confirmation = Gtk.Button(label="Confirmar Datos [✔]")
        self.btn_steps_confirmation.set_sensitive(False)

        # Box - Pasos
        box_steps = Gtk.Box(spacing=5)
        box_steps.pack_start(self.ent_steps,True,True,0)
        box_steps.pack_start(self.btn_steps_confirmation,True,True,0)

        # Box - Datos Antes de iniciar
        '''Labels de organizacion'''
        for label in parent.labels:
            lbl_labels.append(Gtk.Label(label=(label.get_text()+":"),xalign=1))
            
        box_labels = Gtk.Box(orientation = 1)
        
        for label in lbl_labels:
            box_labels.pack_start(label,True,False,0)
        
        '''Labels de informacion'''
        for label in parent.entrys:
            lbl_values.append(Gtk.Label(label=label.get_text(),xalign=0))
        
        box_values = Gtk.Box(orientation = 1,)

        for label in lbl_values:
            box_values.pack_start(label,True,True,0)


        box_info = Gtk.Box(spacing=5)
        box_info.pack_start(box_labels,True,True,0)
        box_info.pack_start(box_values,True,True,0)

        # Box - Pasos y Confirmación
        box_confirmation = Gtk.Box(orientation = 1,spacing=10)
        box_confirmation.pack_start(lbl_steps,True,True,0)
        box_confirmation.pack_start(box_steps,True,True,0)

        # Box - Madre
        box = Gtk.Box(orientation = 1, spacing = 30)
        box.pack_start(box_info,True,True,0)
        box.pack_start(box_confirmation,True,True,0)

        self.add(box)

        self.show_all()

    def check(self, widget):
        if self.ent_steps.get_text() == "":
            self.btn_steps_confirmation.set_sensitive(False)
        else:
            self.btn_steps_confirmation.set_sensitive(True)