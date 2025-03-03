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
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import get_button_size, get_button_token, APP, DEVICE_TYPE
from carbonkivy.behaviors import BackgroundColorBehavior, HoverBehavior


class CButton(
    BackgroundColorBehavior,
    HoverBehavior,
    ButtonBehavior,
    RelativeLayout,
):

    text = StringProperty("")

    icon = StringProperty(None, allownone=True)

    font_size = NumericProperty()

    text_color = ColorProperty()

    active_color = ColorProperty()

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

    def set_colors(self, *args) -> None:
        """
        Defines the method to apply the bg_color.
        """

    def update_specs(self, *args) -> None:
        self.height = get_button_size(self.role)
        self.set_colors()

    def on_touch_down(self, touch) -> bool:
        if self.cstate != "disabled":
            self.focus = self.collide_point(touch.x, touch.y)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self.inset_color = getattr(APP, "focus_inset")
        else:
            self.inset_color = self.bg_color

    def element_hover(self, instance: object, pos: list, *args) -> None:
        if self.collide_point(pos[0], pos[1]):
            if not self.focus:
                self._bg_color = self.hover_color
                self.line_color = self.hover_color
                self.inset_color = self.hover_color
            else:
                self._bg_color = self.hover_color
        else:
            self._bg_color = self.bg_color
            if not self.focus:
                self.line_color = self.bg_color
                self.inset_color = self.bg_color
        return super().element_hover(instance, pos, *args)


class CButtonPrimary(CButton):

    active_color = getattr(APP, "button_primary_active")

    hover_color = getattr(APP, "button_primary_hover")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_cstate(self, *args) -> None:
        self.set_colors()

    def set_colors(self, *args) -> None:
        self.bg_color = getattr(APP, get_button_token(self.cstate, "Primary"))
        self.line_color = self.bg_color
        self.inset_color = self.bg_color

    @mainthread
    def on_state(self, *args) -> None:
        if self.state == "down" and self.cstate != "disabled":
            self._bg_color = self.active_color
            self.line_color = getattr(APP, "focus")
        else:
            self._bg_color = self.bg_color if not self.hover else self.hover_color
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
