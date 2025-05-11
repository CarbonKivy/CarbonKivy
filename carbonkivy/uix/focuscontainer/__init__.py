import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .focuscontainer import FocusContainer

Builder.load_file(os.path.join(UIX, "focuscontainer", "focuscontainer.kv"))
