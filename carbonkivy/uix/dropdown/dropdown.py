from __future__ import annotations

__all__ = ("CDropdown",)

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
)
from kivy.uix.widget import Widget

from carbonkivy.behaviors import ElevationBehavior
from carbonkivy.uix.boxlayout import CBoxLayout


class CDropdown(CBoxLayout, ElevationBehavior):

    visibility = BooleanProperty(False, allownone=True)

    master = ObjectProperty()

    margin = NumericProperty(None, allownone=True)

    pointer = OptionProperty("Upward", options=["Upward", "Downward"])

    _pointer = OptionProperty("Upward", options=["Upward", "Downward"])

    def __init__(self, **kwargs) -> None:
        super(CDropdown, self).__init__(**kwargs)

    def update_pos(self, instance: Widget, *args) -> None:
        pos_x, pos_y = [
            instance.center_x - self.width / 2,
            (
                instance.top + dp(12)
                if (self.pointer == "Downward")
                else instance.y - self.height - dp(12)
            ),
        ]

        instance_center = instance.to_window(instance.center_x, instance.center_y)

        if instance_center[0] < self.width / 2:
            pos_x = instance.center_x - dp(16) if (not self.margin) else self.margin
        elif (Window.width - instance_center[0]) < self.width / 2:
            pos_x = (
                instance.center_x - self.width + dp(16)
                if (not self.margin)
                else Window.width - self.width - self.margin
            )

        if (Window.height - instance_center[1]) < (
            instance.height / 2 + self.height + dp(12)
        ):
            pos_y = instance.y - self.height - dp(12)
            self._pointer = "Upward"
        elif (instance_center[1]) < (instance.height / 2 + self.height + dp(12)):
            pos_y = instance.top + dp(12)
            self._pointer = "Downward"
        else:
            self._pointer = self.pointer

        self.pos = instance.to_window(*[pos_x, pos_y])

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) and not self.master.collide_point(
            *self.master.to_parent(*self.master.to_widget(*touch.pos))
        ):
            self.visibility = False
        return super().on_touch_down(touch)

    def on_visibility(self, *args) -> None:

        def set_visibility(*args) -> None:
            if self.visibility:
                try:
                    self.update_pos(self.master)
                    self.master.bind(pos=self.update_pos)
                    Window.add_widget(self)
                except Exception as e:
                    print(e)
            else:
                try:
                    self.master.unbind(pos=self.update_pos)
                    Window.remove_widget(self)
                except Exception:
                    return

        Clock.schedule_once(set_visibility)
