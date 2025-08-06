import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .checkbox import CCheckbox

filename = os.path.join(UIX, "checkbox", "checkbox.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
