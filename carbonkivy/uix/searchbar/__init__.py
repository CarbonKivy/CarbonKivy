import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .searchbar import CSearchBar

filename = os.path.join(UIX, 'searchbar', 'searchbar.kv')
if filename not in Builder.files:
    Builder.load_file(filename)
