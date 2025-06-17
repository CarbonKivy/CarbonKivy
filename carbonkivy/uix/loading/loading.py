from __future__ import annotations

__all__ = (
    "CLoadingLayout",
    "CLoadingIndicator",
)

from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.uix.widget import Widget

from carbonkivy.behaviors import HierarchicalLayerBehavior
from carbonkivy.uix.anchorlayout import CAnchorLayout


class CLoadingLayout(CAnchorLayout, HierarchicalLayerBehavior):
    pass


class CLoadingIndicator(Widget, HierarchicalLayerBehavior):

    active = BooleanProperty(True)

    bg_color = ColorProperty([1, 1, 1, 0])

    stroke_color = ColorProperty()

    angle = NumericProperty(0)

    stroke_width = NumericProperty(5)

    role = OptionProperty("Small", options=["Large", "Small"])

    def __init__(self, **kwargs) -> None:
        super(CLoadingIndicator, self).__init__(**kwargs)
        self.on_active()

    def rotate(self, *args) -> None:
        self.angle = (self.angle + 6) % 360

    def on_active(self, *args) -> None:
        if self.active:
            Clock.schedule_interval(self.rotate, 1 / 60)
        elif not self.active:
            Clock.unschedule(self.update)
