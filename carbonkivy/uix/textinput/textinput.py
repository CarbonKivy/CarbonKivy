from __future__ import annotations

__all__ = (
    "CTextInput", 
    "CTextInputLabel",
    "CTextInputHelperText",
)

from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
    HoverBehavior,
)
from carbonkivy.uix.label import CLabel


class CTextInputLabel(CLabel):
    pass


class CTextInputHelperText(CLabel):
    pass


class CTextInput(
    AdaptiveBehavior,
    BackgroundColorBehavior,
    RelativeLayout,
    DeclarativeBehavior,
    HoverBehavior,
):
    hint_text = StringProperty()

    focus = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(CTextInput, self).__init__(**kwargs)

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        self.focus = self.collide_point(*touch.pos)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self._line_color = self.line_color
        else:
            self._line_color = self.bg_color
