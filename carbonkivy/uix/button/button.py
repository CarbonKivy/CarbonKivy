from __future__ import annotations

__all__ = (
    "CButton",
    "CButtonDanger",
    "CButtonPrimary",
    "CButtonSecondary",
    "CButtonGhost",
    "CButtonTertiary",
)

from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.icon import CIcon
from carbonkivy.uix.label import CLabel
from carbonkivy.utils import get_button_size


class CButton(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    ButtonBehavior,
    DeclarativeBehavior,
    HoverBehavior,
    RelativeLayout,
):

    dynamic_width = BooleanProperty(True)

    icon_color = ColorProperty([1, 1, 1, 1])

    text_color = ColorProperty([1, 1, 1, 1])

    text_color_focus = ColorProperty([1, 1, 1, 1])

    text_color_disabled = ColorProperty()

    text_color_hover = ColorProperty()

    _text_color = ColorProperty()

    cbutton_layout = ObjectProperty()

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

    actual_width = NumericProperty()

    font_size = NumericProperty()

    _width = NumericProperty()

    text = StringProperty(None, allownone=True)

    icon = StringProperty(None, allownone=True)

    padding = VariableListProperty([0], length=4)

    def __init__(self, **kwargs) -> None:
        super(CButton, self).__init__(**kwargs)

    def on_font_size(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon.font_size = self.font_size + sp(8)
        except Exception:
            return

    def on_text_color(self, instance: object, color: list | str) -> None:
        self._text_color = color
        self.icon_color = color

    def on_icon(self, *args) -> None:

        def add_icon(*args) -> None:
            try:
                self.add_widget(self.cbutton_layout_icon)
                self.ids["cbutton_layout_icon"] = self.cbutton_layout_icon
                return
            except Exception:
                return

        if self.icon and (not "cbutton_layout_icon" in self.ids):
            self.cbutton_layout_icon = CButtonIcon(
                base_button=self,
            )
            Clock.schedule_once(add_icon)
        elif self.icon == None:
            try:
                self.remove_widget(self.ids.cbutton_layout_icon)
            except Exception:
                return
        else:
            try:
                self.ids.cbutton_layout_icon.icon = self.icon
                return
            except Exception:
                return

    def on_text(self, *args) -> None:

        def add_label(*args) -> None:
            try:
                self.add_widget(self.cbutton_layout_label, index=0)
                self.ids["cbutton_layout_label"] = self.cbutton_layout_label
                self.adjust_width()
                return
            except Exception:
                return

        if self.text and (not "cbutton_layout_label" in self.ids):
            self.cbutton_layout_label = CButtonLabel(base_button=self)
            Clock.schedule_once(add_label)
        elif self.text == None:
            try:
                self.remove_widget(self.ids.cbutton_layout_label)
            except Exception:
                return
        else:
            try:
                self.ids.cbutton_layout_label.text = self.text
                self.adjust_width()
                return
            except Exception:
                return

    def on_hover(self, *args) -> None:
        if self.hover:
            self._text_color = self.text_color_hover
        else:
            self._text_color = self.text_color
        self.icon_color = self._text_color
        return super().on_hover(*args)

    def on_state(self, *args) -> None:
        if self.state == "down" and self.cstate != "disabled":
            self._bg_color = self.active_color
        else:
            self._bg_color = (
                (self.bg_color_focus if self.focus else self.bg_color)
                if not self.hover
                else self.hover_color
            )

    def on_focus(self, *args) -> None:
        if self.focus:
            if not self.hover:
                self._bg_color = self.bg_color_focus
            self._text_color = self.text_color_focus
        else:
            self._text_color = self.text_color
        self.icon_color = self._text_color
        return super().on_focus(*args)

    def adjust_width(self, *args) -> None:
        if self.dynamic_width == True:
            _width = dp(0)
            if self.ids.get("cbutton_layout_label"):
                _width += self.ids.cbutton_layout_label.width
                self._width = _width + dp(80)


class CButtonDanger(CButton):

    variant = OptionProperty("Primary", options=["Ghost", "Primary", "Tertiary"])

    def __init__(self, **kwargs) -> None:
        super(CButtonDanger, self).__init__(**kwargs)

    def on_focus(self, *args) -> None:
        if self.variant == "Tertiary":
            self.hover_enabled = not self.focus
        return super().on_focus(*args)


class CButtonIcon(CIcon):

    base_button = ObjectProperty()


class CButtonLabel(CLabel):

    base_button = ObjectProperty()


class CButtonPrimary(CButton):
    pass


class CButtonSecondary(CButton):
    pass


class CButtonGhost(CButton):
    pass


class CButtonTertiary(CButton):

    def __init__(self, **kwargs) -> None:
        super(CButtonTertiary, self).__init__(**kwargs)

    def on_focus(self, *args) -> None:
        self.hover_enabled = not self.focus
        return super().on_focus(*args)
