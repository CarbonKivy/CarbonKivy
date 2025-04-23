import os

from kivy.lang import Builder

from .image import CImage
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "image", "image.kv"))
