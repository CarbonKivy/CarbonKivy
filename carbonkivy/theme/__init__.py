import os

from kivy.lang import Builder

from carbonkivy.config import THEME

Builder.load_file(os.path.join(THEME, "theme.kv"))