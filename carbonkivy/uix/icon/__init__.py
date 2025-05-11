import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .icon import CBaseIcon, CIcon, CIconCircular

Builder.load_file(os.path.join(UIX, "icon", "icon.kv"))
