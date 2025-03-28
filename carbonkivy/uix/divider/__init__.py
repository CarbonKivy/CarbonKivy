import os

from kivy.lang import Builder

from .divider import CDivider
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "divider", "divider.kv"))
