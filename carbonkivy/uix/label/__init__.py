import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .label import CBaseLabel, CLabel, CLabelCircular

filename = os.path.join(UIX, "label", "label.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
