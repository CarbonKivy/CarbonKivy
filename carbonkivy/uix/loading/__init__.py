import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .loading import CLoadingIndicator, CLoadingLayout

filename = os.path.join(UIX, "loading", "loading.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
