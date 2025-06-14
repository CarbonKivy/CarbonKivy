from __future__ import annotations

__all__ = (
    "CButton",
    "CButtonDanger",
    "CButtonPrimary",
    "CButtonSecondary",
    "CButtonGhost",
    "CButtonTertiary",
)

from kivy.clock import Clock, mainthread
from kivy.metrics import sp
from kivy.properties import (
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

    text = StringProperty(None, allownone=True)

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

    cbutton_layout = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CButton, self).__init__(**kwargs)
        self.update_specs()

    def on_font_size(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon.font_size = self.font_size + sp(8)
        except Exception:
            return

    def on_role(self, *args) -> None:
        self.height = get_button_size(self.role)

    def on_text_color(self, instance: object, color: list | str) -> None:
        self._text_color = color
        self.icon_color = color

    def on_icon_color(self, *args) -> None:
        try:
            self.ids.cbutton_layout_icon._color = self.icon_color
        except Exception as e:
            return

    def on_icon(self, *args) -> None:
        
        def add_icon(*args) -> None:
            self.cbutton_layout.add_widget(self.cbutton_layout_icon)
            self.ids["cbutton_layout_icon"] = self.cbutton_layout_icon

        try:
            self.ids.cbutton_layout_icon.icon = self.icon
            return
        except Exception as e:  # nosec
            pass
        if self.icon and (not "cbutton_layout_icon" in self.ids):
            self.cbutton_layout_icon = CButtonIcon(
                base_button=self,
            )
            Clock.schedule_once(add_icon)
        else:
            try:
                self.cbutton_layout.remove_widget(self.ids.cbutton_layout_icon)
            except Exception:
                return

    def on_text(self, *args) -> None:

        def add_label(*args) -> None:
            self.cbutton_layout.add_widget(self.cbutton_layout_label, index=0)
            self.ids["cbutton_layout_label"] = self.cbutton_layout_label

        if self.text and (not "cbutton_layout_label" in self.ids):
            self.cbutton_layout_label = CButtonLabel(base_button=self)
            Clock.schedule_once(add_label)

    def update_specs(self, *args) -> None:
        self.height = get_button_size(self.role)

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


class CButtonDanger(CButton):

    variant = OptionProperty("Primary", options=["Ghost", "Primary", "Tertiary"])

    cstate = OptionProperty("normal", options=["normal"])

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
