from __future__ import annotations

__all__ = ("CButton",)

from kivy.properties import (
    StringProperty,
    OptionProperty,
    ColorProperty,
    BooleanProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import get_button_size, get_button_token, APP
from carbonkivy.behaviors.background_color_behavior import BackgroundColorBehavior


class CButton(
    BackgroundColorBehavior,
    ButtonBehavior,
    RelativeLayout,
):

    text = StringProperty("")

    icon = StringProperty(None, allownone=True)

    text_color = ColorProperty()

    hover_color = ColorProperty()

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_specs()

    def on_role(self, *args) -> None:
        self.height = get_button_size(self.role)

    def set_colors(self, *args) -> None:
        pass

    def update_specs(self, *args) -> None:
        self.height = get_button_size(self.role)
        self.set_colors()

    def on_touch_down(self, touch):
        self.focus = self.collide_point(touch.x, touch.y)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self.inset_color = getattr(APP, "focus_inset")
        else:
            self.inset_color = self.bg_color


class CButtonPrimary(CButton):

    hover_color = getattr(APP, "button_primary_hover")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_cstate(self, *args) -> None:
        self.set_colors()

    def set_colors(self, *args) -> None:
        self.bg_color = getattr(APP, get_button_token(self.cstate, "Primary"))
        self.line_color = self.bg_color
        self.inset_color = self.bg_color

    def on_state(self, *args) -> None:
        if self.state == "down":
            self.bg_color = self.hover_color
            self.line_color = getattr(APP, "focus")
        else:
            self.bg_color = getattr(APP, get_button_token(self.cstate, "Primary"))
            self.line_color = self.bg_color


# class CButtonDanger(CButton):

#     type = OptionProperty(
#         "Primary",
#         options=[
#             "Primary",
#             "Tertiary",
#             "Ghost",
#         ],
#     )


#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.update_specs()

#     def on_type(self, *args) -> None:
#         self.set_colors()

#     def on_cstate(self, *args) -> None:
#         self.set_colors()
