from __future__ import annotations

__all__ = ("StateFocusBehavior",)

from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty

from carbonkivy.behaviors import BackgroundColorBehavior

class StateFocusBehavior(Widget):

    focus = BooleanProperty(False)

    focus_enabled = BooleanProperty(True)

    def on_touch_down(self, touch) -> bool:
        super().on_touch_down(touch)
        if self.cstate != "disabled" and self.focus_enabled:
            self.focus = self.collide_point(*touch.pos)
        return super().on_touch_down(touch)

    def on_focus(self, *args) -> None:
        if issubclass(self.__class__, BackgroundColorBehavior):
            if self.focus:
                self._inset_color = self.inset_color_focus
                self._line_color = self.line_color_focus
            else:
                self._bg_color = self.bg_color
                self._inset_color = self.bg_color
                self._line_color = self.line_color
