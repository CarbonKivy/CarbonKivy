from __future__ import annotations

__all__ = ("CButton",)

from kivy.properties import (
    StringProperty,
    NumericProperty,
    OptionProperty,
    ColorProperty,
    BooleanProperty,
    ObjectProperty,
)
from kivy.metrics import sp
from kivy.clock import mainthread
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import get_button_size, get_button_token, APP
from carbonkivy.behaviors import BackgroundColorBehavior, HoverBehavior


class CButton(
    BackgroundColorBehavior,
    HoverBehavior,
    ButtonBehavior,
    RelativeLayout,
):

    text = StringProperty("")

    ctoken = StringProperty("")

    icon = StringProperty(None, allownone=True)

    font_size = NumericProperty()

    text_color = ColorProperty(getattr(APP, "text_on_color"))

    _text_color = ColorProperty()

    active_color = ColorProperty()

    line_color = getattr(APP, "focus")

    role = OptionProperty(
        "Medium",
        options=[
            "Small",
            "Medium",
            "Large Productive",
            "Large Expressive",
            "Extra Large",
            "2XL",
        ],
    )

    cstate = OptionProperty("normal", options=["active", "disabled", "normal"])

    focus = BooleanProperty(False)

    cbutton_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_specs()

    def on_role(self, *args) -> None:
        self.height = get_button_size(self.role)

    def on_cstate(self, *args) -> None:
        self.set_colors()

    def set_colors(self, *args) -> None:
        """
        Defines the method to apply the bg_color.
        """
        self.bg_color = getattr(APP, get_button_token(self.cstate, self.ctoken))
        self._line_color = self.bg_color
        self.inset_color = self.bg_color

    def update_specs(self, *args) -> None:
        self.height = get_button_size(self.role)
        self.set_colors()

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        if self.cstate != "disabled":
            self.focus = self.collide_point(*touch.pos)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self.inset_color = getattr(APP, "focus_inset")
            self._line_color = self.line_color
        else:
            self.inset_color = self.bg_color
            self._line_color = self.bg_color

    def on_state(self, *args) -> None:
        if self.state == "down" and self.cstate != "disabled":
            self._bg_color = self.active_color
        else:
            self._bg_color = self.bg_color if not self.hover else self.hover_color


class CButtonPrimary(CButton):

    ctoken = "Primary"

    active_color = getattr(APP, "button_primary_active")

    hover_color = getattr(APP, "button_primary_hover")


class CButtonSecondary(CButton):

    ctoken = "Secondary"

    active_color = getattr(APP, "button_secondary_active")

    hover_color = getattr(APP, "button_secondary_hover")


class CButtonGhost(CButton):

    inset_width = 0

    ctoken = "Ghost"

    active_color = getattr(APP, "background_active")

    hover_color = getattr(APP, "background_hover")

    text_color = getattr(APP, "link_primary")

    def on_hover(self, *args) -> None:
        super().on_hover(*args)
        if self.hover:
            self._text_color = getattr(APP, "link_primary_hover")
        else:
            if not self.focus:
                self._text_color = self.text_color

    def on_focus(self, *args) -> None:
        super().on_focus(*args)
        if self.focus:
            self._text_color = getattr(APP, "link_primary_hover")
        else:
            self._text_color = self.text_color


class CButtonTeriary(CButton):
    pass

class CButtonDanger(CButton):

    type = OptionProperty(
        "Primary",
        options=[
            "Primary",
            "Tertiary",
            "Ghost",
        ],
    )


