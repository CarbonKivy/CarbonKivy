import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .toggle import (
    CToggle,
)

filename = os.path.join(UIX, "toggle", "toggle.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
