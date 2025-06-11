from __future__ import annotations

__all__ = ("CNotificationInline", "CNotificationToast", "CNotificationCallout")

from kivy.properties import (
    ColorProperty,
    OptionProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    DeclarativeBehavior,
)


class CBaseNotification(AdaptiveBehavior, DeclarativeBehavior, ModalView):

    _contrast_color = ColorProperty()

    _bl_width = NumericProperty(1)

    style = OptionProperty("Info", options=["Error", "Info", "Success", "Warning"])

    icon = StringProperty()

    title = StringProperty("Notification")

    subtitle = StringProperty()


class CNotificationInline(CBaseNotification):
    pass


class CNotificationToast(CBaseNotification):
    pass
