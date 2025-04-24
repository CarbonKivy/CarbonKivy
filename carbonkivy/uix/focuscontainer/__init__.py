import os

from kivy.lang import Builder

from .focuscontainer import FocusContainer
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "focuscontainer", "focuscontainer.kv"))
