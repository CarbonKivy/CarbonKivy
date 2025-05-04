import os

from kivy.lang import Builder

from .icon import CBaseIcon, CIcon, CIconCircular
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "icon", "icon.kv"))
