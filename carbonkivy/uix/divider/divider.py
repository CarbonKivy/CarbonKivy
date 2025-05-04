from __future__ import annotations

__all__ = ("CDivider",)

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty, OptionProperty
from kivy.uix.boxlayout import BoxLayout


class CDivider(BoxLayout):

    color = ColorProperty()

    orientation = OptionProperty("horizontal", options=["horizontal", "vertical"])

    divider_width = NumericProperty(dp(1))

    def __init__(self, **kwargs):
        super(CDivider, self).__init__(**kwargs)
        Clock.schedule_once(self.on_orientation)

    def on_orientation(self, *args) -> None:
        if self.orientation == "vertical":
            self.size_hint_x = None
            self.width = self.divider_width
        elif self.orientation == "horizontal":
            self.size_hint_y = None
            self.height = self.divider_width
