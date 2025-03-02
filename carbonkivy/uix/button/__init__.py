import os

from kivy.lang import Builder

from carbonkivy.uix.button.button import CButtonPrimary
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "button", "button.kv"))
