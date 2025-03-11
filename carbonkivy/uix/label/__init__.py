import os

from kivy.lang import Builder

from .label import CLabel
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "label", "label.kv"))