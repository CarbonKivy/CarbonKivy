import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .fab import CFAB

filename = os.path.join(UIX, 'fab', 'fab.kv')
if filename not in Builder.files:
    Builder.load_file(filename)
