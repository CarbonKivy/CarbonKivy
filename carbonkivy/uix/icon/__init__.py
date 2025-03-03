import os

from kivy.lang import Builder

from carbonkivy.uix.icon.icon import CIcon
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "icon", "icon.kv"))
