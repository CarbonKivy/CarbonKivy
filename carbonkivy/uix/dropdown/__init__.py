import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .dropdown import CDropdown

filename = os.path.join(UIX, "dropdown", "dropdown.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
