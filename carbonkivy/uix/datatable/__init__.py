import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .datatable import CDatatable

filename = os.path.join(UIX, "datatable", "datatable.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
