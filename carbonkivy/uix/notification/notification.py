from __future__ import annotations

__all__ = ("CNotificationInline", "CNotificationToast", "CNotificationCallout")

from kivy.properties import StringProperty
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)

class CBaseNotification(AdaptiveBehavior, BackgroundColorBehavior, DeclarativeBehavior, ModalView):

    icon = StringProperty("info")

    title = StringProperty("Notification")

    subtitle = StringProperty()

