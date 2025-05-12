import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .image import CImage

filename = os.path.join(UIX, "image", "image.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
