from __future__ import annotations

__all__ = (
    "CBaseNotification",
    "CNotification",
    "CNotificationCaption",
    "CNotificationCloseButton",
    "CNotificationInline",
    "CNotificationToast",
)

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    DeclarativeBehavior,
    ElevationBehavior,
)
from carbonkivy.theme.theme import CarbonTheme
from carbonkivy.uix.button import CButton
from carbonkivy.uix.label import CLabel
from carbonkivy.utils import get_latest_time


class CBaseNotification(
    AdaptiveBehavior, DeclarativeBehavior, ElevationBehavior, ModalView
):

    time_caption_enabled = BooleanProperty(False)

    _contrast_color = ColorProperty()

    _bgi_color = ColorProperty()

    _bl_width = NumericProperty(3)

    status = OptionProperty("Success", options=["Error", "Info", "Success", "Warning"])

    contrast = OptionProperty("Low", options=["Low", "High"])

    caption = StringProperty(None, allownone=True)

    icon = StringProperty()

    title = StringProperty("Notification")

    action_button = ObjectProperty()

    subtitle = StringProperty()

    cnotification_layout = ObjectProperty()

    theme_cls = ObjectProperty(CarbonTheme(defaults=False))

    def __init__(self, *args, **kwargs) -> None:
        super(CBaseNotification, self).__init__(*args, **kwargs)
        self.on_contrast()

    def on_contrast(self, *args) -> None:
        if self.contrast == "High":
            if App.get_running_app().theme in ["Gray90", "Gray100"]:
                self.theme_cls.theme = "White"
            else:
                self.theme_cls.theme = "Gray100"
        else:
            self.theme_cls.theme = App.get_running_app().theme

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

    def on_action_button(self, *args) -> None:
        def add_action_button(*args) -> None:
            self.cnotification_layout.add_widget(self.action_button)
            self.ids["cnotification_action_button"] = self.action_button

        if (
            isinstance(self.action_button, ButtonBehavior)
            and not self.ids.get("cnotification_action_button")
            and not self.caption
        ):
            Clock.schedule_once(add_action_button)


class CNotification(CBaseNotification):

    variant = OptionProperty("Toast", options=["Inline", "Toast"])

    def __init__(self, *args, **kwargs) -> None:
        super(CNotification, self).__init__(*args, **kwargs)


class CNotificationInline(CBaseNotification):
    pass


class CNotificationToast(CBaseNotification):
    pass


class CNotificationCloseButton(CButton):
    pass


class CNotificationCaption(CLabel):
    pass
