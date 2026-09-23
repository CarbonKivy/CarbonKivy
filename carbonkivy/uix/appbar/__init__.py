import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .appbar import CAppBar

filename = os.path.join(UIX, 'appbar', 'appbar.kv')
if filename not in Builder.files:
    Builder.load_file(filename)
