import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .loading import CLoadingLayout, CLoadingIndicator

filename = os.path.join(UIX, "loading", "loading.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
