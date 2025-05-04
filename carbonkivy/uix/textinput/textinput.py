from __future__ import annotations

__all__ = (
    "CTextInput",
    "CTextInputLabel",
    "CTextInputHelperText",
    "CTextInputTrailingIconButton",
)

from kivy.metrics import dp
from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
)
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.button import CButtonGhost


class CTextInputLabel(CLabel):
    pass


class CTextInputHelperText(CLabel):
    pass


class CTextInputTrailingIconButton(CButtonGhost):
    pass


class CTextInput(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    RelativeLayout,
    DeclarativeBehavior,
    HoverBehavior,
):

    password = BooleanProperty(False)

    readonly = BooleanProperty(False)

    focus = BooleanProperty(False)

    font_size = NumericProperty(dp(14))

    text = StringProperty()

    hint_text = StringProperty()

    password_mask = StringProperty("\u2022")

    def __init__(self, **kwargs):
        super(CTextInput, self).__init__(**kwargs)

    def on_touch_down(self, touch) -> bool | None:
        super().on_touch_down(touch)
        self.focus = self.collide_point(*touch.pos)
        if not self.focus:
            return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self._line_color = self.line_color
        else:
            self._line_color = self.bg_color

    def on_password(self, *args) -> None:
        self.ids.ctextinput_area.cursor = (0, 0)
