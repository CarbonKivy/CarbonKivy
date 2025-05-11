from __future__ import annotations

__all__ = ("HoverBehavior",)

from kivy.core.window import Window
from kivy.properties import BooleanProperty, ColorProperty
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import DEVICE_TYPE

from .background_color_behavior import BackgroundColorBehavior


class HoverBehavior:

    hover = BooleanProperty(False)

    hover_enabled = BooleanProperty(True)

    hover_color = ColorProperty([1, 1, 1, 0])

    def __init__(self, **kwargs):
        if DEVICE_TYPE != "mobile":
            Window.bind(mouse_pos=self.element_hover)
        super().__init__(**kwargs)

    def element_hover(self, instance: object, pos: list, *args) -> None:
        if self.cstate != "disabled" and self.hover_enabled:
            self.hover = self.collide_point(
                *(
                    self.to_widget(*pos)
                    if not isinstance(self, RelativeLayout)
                    else self.to_parent(*self.to_widget(*pos))
                )
            )

    def on_hover(self, *args) -> None:
        if isinstance(self, BackgroundColorBehavior):
            if self.hover:
                self._bg_color = self.hover_color
                if not self.focus:
                    self._line_color = self.hover_color
                    self._inset_color = self.hover_color
            else:
                self._bg_color = self.bg_color
                if not self.focus:
                    self._line_color = self.line_color
                    self._inset_color = self.bg_color
