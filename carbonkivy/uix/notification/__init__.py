import os

from carbonkivy.config import UIX
from kivy.lang import Builder

from .notification import (
    CBaseNotification,
    CNotification,
    CNotificationCloseButton,
    CNotificationInline,
    CNotificationToast,
)

filename = os.path.join(UIX, "notification", "notification.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
