from __future__ import annotations

__all__ = ("CLoadingLayout", "CLoadingIndicator",)

from kivy.clock import Clock
from kivy.properties import ColorProperty, NumericProperty, OptionProperty
from kivy.uix.widget import Widget

from carbonkivy.behaviors import HierarchicalLayerBehavior
from carbonkivy.uix.anchorlayout import CAnchorLayout


class CLoadingLayout(CAnchorLayout, HierarchicalLayerBehavior):
    pass


class CLoadingIndicator(Widget, HierarchicalLayerBehavior):

    bg_color = ColorProperty([1, 1, 1, 0])

    stroke_color = ColorProperty()

    angle = NumericProperty(0)

    stroke_width = NumericProperty(5)

    role = OptionProperty("Small", options=["Large", "Small"])

    def __init__(self, **kwargs):
        super(CLoadingIndicator, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        self.angle = (self.angle + 6) % 360
