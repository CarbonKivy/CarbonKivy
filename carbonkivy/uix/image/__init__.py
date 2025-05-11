import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .image import CImage

Builder.load_file(os.path.join(UIX, "image", "image.kv"))
