from __future__ import annotations

__all__ = (
    "CButton",
    "CButtonPrimary",
    "CButtonSecondary",
    "CButtonGhost",
    "CButtonTertiary",
)

from kivy.app import App
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
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
)
from carbonkivy.uix.icon import CIcon
from carbonkivy.utils import get_button_size, get_button_token


APP = App.get_running_app()


class CButton(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    ButtonBehavior,
    DeclarativeBehavior,
    HoverBehavior,
    RelativeLayout,
):

    text = StringProperty("")

    icon = StringProperty(None, allownone=True)

    font_size = NumericProperty()

    actual_width = NumericProperty()

    padding = VariableListProperty([0], length=4)

    icon_color = ColorProperty([1, 1, 1, 1])

    text_color = ColorProperty([1, 1, 1, 1])

    text_color_focus = ColorProperty([1, 1, 1, 1])

    text_color_disabled = ColorProperty()

    text_color_hover = ColorProperty()

    _text_color = ColorProperty()

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

    focus = BooleanProperty(False)

    cbutton_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(CButton, self).__init__(**kwargs)
        self.update_specs()

    def on_font_size(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon.font_size = self.font_size + sp(8)
        except Exception:
            return

    def on_role(self, *args) -> None:
        self.height = get_button_size(self.role)

    def on_icon_color(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon._color = self.icon_color
        except Exception as e:
            return

    def on_icon(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon.icon = self.icon
            return
        except Exception as e:  # nosec
            pass
        if self.icon and (not "cbutton_layout_icon" in self.ids):
            self.cbutton_layout_icon = CIcon(
                icon=self.icon,
                pos_hint={"center_y": 0.5},
                _color=self.icon_color,
                font_size=self.font_size + sp(8),
            )
            self.cbutton_layout.add_widget(self.cbutton_layout_icon)
            self.ids["cbutton_layout_icon"] = self.cbutton_layout_icon
        else:
            try:
                self.cbutton_layout.remove_widget(self.ids.cbutton_layout_icon)
            except Exception:
                return

    def update_specs(self, *args) -> None:
        self.height = get_button_size(self.role)

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        if self.cstate != "disabled":
            self.focus = self.collide_point(*touch.pos)
        return super().on_touch_down(touch)

    def on_hover(self, *args) -> None:
        if self.hover:
            self._text_color = self.text_color_hover
        else:
            if not self.focus:
                self._text_color = self.text_color
        self.icon_color = self._text_color
        return super().on_hover(*args)

    def on_focus(self, *args) -> None:
        if self.focus:
            self._inset_color = self.inset_color_focus
            self._line_color = self.line_color_focus
            self._text_color = self.text_color_focus
        else:
            self._bg_color = self.bg_color
            self._inset_color = self.bg_color
            self._line_color = self.line_color
            self._text_color = self.text_color
        self.icon_color = self._text_color

    def on_state(self, *args) -> None:
        if self.state == "down" and self.cstate != "disabled":
            self._bg_color = self.active_color
        else:
            self._bg_color = (self.bg_color_focus if self.focus else self.bg_color) if not self.hover else self.hover_color


class CButtonPrimary(CButton):
    pass


class CButtonSecondary(CButton):
    pass


class CButtonGhost(CButton):
    pass


class CButtonTertiary(CButton):

    def __init__(self, **kwargs):
        super(CButtonTertiary, self).__init__(**kwargs)

    def on_focus(self, *args) -> None:
        self.hover_enabled = not self.focus
        return super().on_focus(*args)
