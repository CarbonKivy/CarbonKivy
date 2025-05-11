import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .divider import CDivider

Builder.load_file(os.path.join(UIX, "divider", "divider.kv"))
