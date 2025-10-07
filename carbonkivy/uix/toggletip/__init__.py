import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .toggletip import CToggletip

filename = os.path.join(UIX, "toggletip", "toggletip.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
