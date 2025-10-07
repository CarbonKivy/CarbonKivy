from __future__ import annotations

__all__ = ("HoverBehavior",)

from kivy.core.window import Window
from kivy.properties import BooleanProperty, ColorProperty, ListProperty
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.utils import DEVICE_TYPE

from .background_color_behavior import BackgroundColorBehavior


class HoverBehavior:

    hover = BooleanProperty(False)

    hover_enabled = BooleanProperty(True)

    hover_color = ColorProperty([1, 1, 1, 0])

    def __init__(self, **kwargs) -> None:
        self.on_hover_enabled()
        super(HoverBehavior, self).__init__(**kwargs)

    def element_hover(self, instance: object, pos: list, *args) -> None:
        if not self.is_visible():
            self.hover = False
        if (
            (
                (hasattr(self, "cstate") and self.cstate != "disabled")
                or (not self.disabled)
            )
            and self.hover_enabled
            and self.is_visible()
        ):

            for widget in self.children:
                if hasattr(widget, "hover") and widget.hover:
                    self.hover = False
                    return

            self.hover = self.collide_point(
                *(
                    self.to_widget(*pos)
                    if not isinstance(self, RelativeLayout)
                    else self.to_parent(*self.to_widget(*pos))
                )
            )

    def is_visible(self, *args) -> bool:
        if not self.get_root_window() or self.disabled or self.opacity == 0:
            return False
        else:
            return True

    def on_hover_enabled(self, *args) -> None:
        if DEVICE_TYPE != "mobile":
            if self.hover_enabled:
                Window.bind(mouse_pos=self.element_hover)
            else:
                Window.unbind(mouse_pos=self.element_hover)

    def on_hover(self, *args) -> None:
        if isinstance(self, BackgroundColorBehavior):
            if self.hover:
                self._bg_color = self.hover_color
            else:
                self._bg_color = self.bg_color
