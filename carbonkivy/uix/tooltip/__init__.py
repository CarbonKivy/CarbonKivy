import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .tooltip import CTooltip

filename = os.path.join(UIX, "tooltip", "tooltip.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
