from __future__ import annotations

__all__ = ("StateFocusBehavior",)

from kivy.core.window import Window
from kivy.properties import BooleanProperty

from .background_color_behavior import BackgroundColorBehavior


class StateFocusBehavior:

    focus = BooleanProperty(False)

    focus_enabled = BooleanProperty(True)

    def __init__(self, **kwargs) -> None:
        self.on_focus_enabled()
        super(StateFocusBehavior, self).__init__(**kwargs)

    def on_focus_enabled(self, *args) -> None:
        if self.focus_enabled:
            Window.bind(on_touch_down=self.on_touch)
        else:
            Window.unbind(on_touch_down=self.on_touch)

    def on_touch(self, instance: object, touch: list[float, float], *args) -> None:
        if issubclass(self.__class__, BackgroundColorBehavior):
            if self.cstate != "disabled" and self.get_root_window():
                self.focus = self.collide_point(
                    *self.to_parent(*self.to_widget(*touch.pos))
                )
            else:
                return
        else:
            self.focus = self.collide_point(
                *self.to_parent(*self.to_widget(*touch.pos))
            )

    def on_focus(self, *args) -> None:
        if issubclass(self.__class__, BackgroundColorBehavior):
            if self.focus:
                if hasattr(self, "hover") and self.hover:
                    pass
                else:
                    self._bg_color = self.bg_color_focus
                self._inset_color = self.inset_color_focus
                self._line_color = self.line_color_focus
            else:
                self._bg_color = self.bg_color
                self._inset_color = self.inset_color
                self._line_color = self.line_color
