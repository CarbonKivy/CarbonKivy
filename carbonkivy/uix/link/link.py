from __future__ import annotations

__all__ = ("CLink",)

import webbrowser

from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label

from carbonkivy.behaviors import BackgroundColorBehavior, HoverBehavior
from carbonkivy.theme.icons import ibm_icons
from carbonkivy.utils import APP


class CLink(BackgroundColorBehavior, ButtonBehavior, HoverBehavior, Label):

    name = StringProperty()

    url = StringProperty()

    text_color = ColorProperty()

    cstate = OptionProperty("normal", options=["active", "disabled", "normal"])

    icon = OptionProperty("", options=ibm_icons.keys())

    icon_code = StringProperty()

    external = BooleanProperty(False)

    def on_hover(self, *args) -> None:
        if self.hover:
            self.color = getattr(APP, "link_primary_hover")
            self.text = f"[u]{self.name}[/u] [font=cicon]{self.icon_code}[/font]"
        else:
            self.color = self.text_color
            self.text = f"{self.name} [font=cicon]{self.icon_code}[/font]"

    def on_icon(self, *args) -> None:
        self.icon_code = ibm_icons[self.icon]

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        if self.cstate != "disabled":
            self.focus = self.collide_point(*touch.pos)
            if self.focus and self.external:
                webbrowser.open_new_tab(self.url)
        return super().on_touch_down(touch)
