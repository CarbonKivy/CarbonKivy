import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .link import CLink

Builder.load_file(os.path.join(UIX, "link", "link.kv"))
