import os

from kivy.lang import Builder

from .icon import CIcon
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "icon", "icon.kv"))
