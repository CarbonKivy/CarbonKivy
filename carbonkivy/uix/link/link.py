from __future__ import annotations

__all__ = ("CLink",)

import webbrowser

from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.theme.icons import ibm_icons


class CLink(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    ButtonBehavior,
    HoverBehavior,
    StateFocusBehavior,
    Label,
):

    name = StringProperty()

    url = StringProperty()

    text_color = ColorProperty()

    hover_color = ColorProperty()

    cstate = OptionProperty("normal", options=["active", "disabled", "normal"])

    icon = OptionProperty("", options=ibm_icons.keys())

    icon_code = StringProperty()

    focus = BooleanProperty(False)

    external = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(CLink, self).__init__(**kwargs)

    def on_hover(self, *args) -> None:
        if self.hover:
            self.color = self.hover_color
            self.text = f"[u]{self.name}[/u][font=cicon]{self.icon_code}[/font]"
        else:
            self.color = self.text_color
            self.text = f"{self.name}[font=cicon]{self.icon_code}[/font]"

    def on_icon(self, *args) -> None:
        self.icon_code = ibm_icons[self.icon]

    def on_touch_down(self, touch) -> bool:
        if self.cstate != "disabled":
            if self.focus and self.external:
                Clock.schedule_once(lambda e: webbrowser.open_new_tab(self.url))
        return super().on_touch_down(touch)
