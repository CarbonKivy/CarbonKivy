from __future__ import annotations

__all__ = ("CNotificationInline", "CNotificationToast", "CNotificationCallout")

from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import AdaptiveBehavior, DeclarativeBehavior
from carbonkivy.uix.button import CButton


class CBaseNotification(AdaptiveBehavior, DeclarativeBehavior, ModalView):

    _contrast_color = ColorProperty()

    _bgi_color = ColorProperty()

    _bl_width = NumericProperty(1)

    main_notification_layout = ObjectProperty()

    style = OptionProperty("Success", options=["Error", "Info", "Success", "Warning"])

    caption = StringProperty()

    icon = StringProperty()

    title = StringProperty("Notification")

    subtitle = StringProperty()


class CNotification(CBaseNotification):

    variant = OptionProperty("Toast", options=["Inline", "Toast"])


class CNotificationInline(CBaseNotification):
    pass


class CNotificationToast(CBaseNotification):
    pass


class CNotificationCloseButton(CButton):
    pass
