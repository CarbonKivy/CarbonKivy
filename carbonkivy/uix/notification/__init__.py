import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .notification import CBaseNotification

filename = os.path.join(UIX, "notification", "notification.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
