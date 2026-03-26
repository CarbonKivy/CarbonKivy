import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .selectionlayout import CSelectionLayout

filename = os.path.join(UIX, "selectionlayout", "selectionlayout.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
