import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .icon import CBaseIcon, CIcon, CIconCircular

filename = os.path.join(UIX, "icon", "icon.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
