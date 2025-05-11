import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .label import CLabel

Builder.load_file(os.path.join(UIX, "label", "label.kv"))
