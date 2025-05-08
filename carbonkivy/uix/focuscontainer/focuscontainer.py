from __future__ import annotations

__all__ = ("FocusContainer",)

from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
    StateFocusBehavior,
)


class FocusContainer(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    BoxLayout,
    DeclarativeBehavior,
    HoverBehavior,
):
    focus = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(FocusContainer, self).__init__(**kwargs)

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        if self.cstate != "disabled":
            self.focus = self.collide_point(*touch.pos)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if self.focus:
            self._bg_color = self.bg_color_focus
        elif not self.hover:
            self._bg_color = self.bg_color
