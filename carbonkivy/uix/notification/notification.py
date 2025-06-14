from __future__ import annotations

__all__ = (
    "CBaseNotification",
    "CNotification",
    "CNotificationCaption",
    "CNotificationCloseButton",
    "CNotificationInline",
    "CNotificationToast",
)

from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import AdaptiveBehavior, DeclarativeBehavior
from carbonkivy.uix.button import CButton
from carbonkivy.uix.label import CLabel
from carbonkivy.utils import get_latest_time


class CBaseNotification(AdaptiveBehavior, DeclarativeBehavior, ModalView):

    time_caption_enabled = BooleanProperty(False)

    _contrast_color = ColorProperty()

    _bgi_color = ColorProperty()

    _bl_width = NumericProperty(3)

    status = OptionProperty("Success", options=["Error", "Info", "Success", "Warning"])

    caption = StringProperty(None, allownone=True)

    icon = StringProperty()

    title = StringProperty("Notification")

    subtitle = StringProperty()

    cnotification_layout = ObjectProperty()

    def on_time_caption_enabled(self, *args) -> None:
        if self.time_caption_enabled and not self.caption:
            self.caption = get_latest_time()

    def on_caption(self, *args) -> None:

        def add_caption(caption: CNotificationCaption, *args) -> None:
            self.cnotification_layout.add_widget(caption)
            self.ids["cnotification_caption"] = caption

        if not self.ids.get("cnotification_caption"):
            caption = CNotificationCaption(
                text=self.caption,
            )
            Clock.schedule_once(lambda e: add_caption(caption))
        else:
            self.ids["cnotification_caption"].text = self.caption


class CNotification(CBaseNotification):

    variant = OptionProperty("Toast", options=["Inline", "Toast"])


class CNotificationInline(CBaseNotification):
    pass


class CNotificationToast(CBaseNotification):
    pass


class CNotificationCloseButton(CButton):
    pass


class CNotificationCaption(CLabel):
    pass
