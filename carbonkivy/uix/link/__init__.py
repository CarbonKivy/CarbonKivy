import os

from kivy.lang import Builder

from .link import CLink
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "link", "link.kv"))
