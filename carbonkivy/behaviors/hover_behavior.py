from __future__ import annotations

__all__ = ("HoverBehavior",)

from kivy.core.window import Window
from kivy.properties import ColorProperty, BooleanProperty
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import DEVICE_TYPE
from .background_color_behavior import BackgroundColorBehavior


class HoverBehavior:

    hover = BooleanProperty(False)

    hover_color = ColorProperty([0, 0, 0, 0.1])

    def __init__(self, **kwargs):
        if DEVICE_TYPE != "mobile":
            Window.bind(mouse_pos=self.element_hover)
        super().__init__(**kwargs)

    def element_hover(self, instance: object, pos: list, *args) -> None:
        if self.cstate != "disabled":
            self.hover = self.collide_point(*self.to_widget(*pos) if not isinstance(self, RelativeLayout) else (pos[0], pos[1]))

    def on_hover(self, *args) -> None:
        if isinstance(self, BackgroundColorBehavior):
            if self.hover:
                self._bg_color = self.hover_color
                if not self.focus:
                    self._line_color = self.hover_color
                    self.inset_color = self.hover_color
            else:
                self._bg_color = self.bg_color
                if not self.focus:
                    self._line_color = self.bg_color
                    self.inset_color = self.bg_color
