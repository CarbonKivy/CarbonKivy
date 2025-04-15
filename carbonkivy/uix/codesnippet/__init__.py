import os

from kivy.lang import Builder

from .codesnippet import CodeSnippet
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "codesnippet", "codesnippet.kv"))
