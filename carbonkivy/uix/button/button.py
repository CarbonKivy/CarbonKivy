from __future__ import annotations

__all__ = (
    "CButton",
    "CButtonPrimary",
    "CButtonSecondary",
    "CButtonGhost",
)

from kivy.properties import (
    StringProperty,
    NumericProperty,
    OptionProperty,
    ColorProperty,
    BooleanProperty,
    VariableListProperty,
    ObjectProperty,
)
from kivy.metrics import sp
from kivy.clock import mainthread
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    BackgroundColorBehavior,
    HoverBehavior,
    DeclarativeBehavior,
)
from carbonkivy.uix.icon import CIcon
from carbonkivy.utils import get_button_size, get_button_token, APP


class CButton(
    BackgroundColorBehavior,
    ButtonBehavior,
    DeclarativeBehavior,
    HoverBehavior,
    RelativeLayout,
):

    text = StringProperty("")

    ctoken = StringProperty("")

    icon = StringProperty(None, allownone=True)

    font_size = NumericProperty()

    padding = VariableListProperty([0], length=4)

    text_color = ColorProperty()

    _text_color = ColorProperty()

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
        super(CButton, self).__init__(**kwargs)
        self.update_specs()

    def on_role(self, *args) -> None:
        self.height = get_button_size(self.role)

    def on_ctoken(self, *args) -> None:
        self.set_colors()

    def on_cstate(self, *args) -> None:
        self.set_colors()
        if self.ctoken == "" and self.cstate == "active":
            self.bg_color = self.active_color

    def on_icon(self, *args) -> None:
        if self.icon:
            self.cbutton_layout.add_widget(
                CIcon(
                    icon=self.icon,
                    pos_hint={"center_y": 0.5},
                    _color=self._text_color,
                    font_size=self.font_size + sp(8),
                )
            )
        else:
            for child in self.cbutton_layout.children:
                if isinstance(child, CIcon):
                    self.cbutton_layout.remove_widget(child)

    # def on_text_color(self, *args) -> None:
    #     self._text_color = self.text_color

    @mainthread
    def set_colors(self, *args) -> None:
        """
        Defines the method to apply the bg_color.
        """
        try:
            self.bg_color = getattr(APP, get_button_token(self.cstate, self.ctoken))
        except Exception as e:  # nosec
            pass
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
    pass


class CButtonSecondary(CButton):
    pass


class CButtonGhost(CButton):

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


# class CButtonDanger(CButton):

#     type = OptionProperty(
#         "Primary",
#         options=[
#             "Primary",
#             "Tertiary",
#             "Ghost",
#         ],
#     )
