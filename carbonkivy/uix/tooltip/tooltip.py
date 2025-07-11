from __future__ import annotations

__all__ = ("CTooltip",)

from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class CTooltip(BoxLayout):

    bg_color = ColorProperty()

    text_color = ColorProperty()

    element_x = NumericProperty(0)

    _pointer = OptionProperty("Upward", options=["Upward", "Downward"])

    text = StringProperty()

    radius = VariableListProperty(length=4)

    def __init__(self, **kwargs) -> None:
        super(CTooltip, self).__init__(**kwargs)

    @mainthread
    def update_pos(self, instance: Widget, *args) -> None:
        pos_x, pos_y = [instance.x + instance.width / 2 - self.width / 2, instance.y + instance.height + dp(12)]

        instance_center = instance.to_window(instance.center_x, instance.center_y)

        if ((Window.width - instance_center[0]) > self.width / 2) and (
            instance_center[0] > self.width / 2
        ):
            pos_x = instance.x + instance.width / 2 - self.width / 2
        elif instance_center[0] < self.width / 2:
            pos_x = instance.center_x - dp(16)
        elif (Window.width - instance_center[0]) < self.width / 2:
            pos_x = instance.center_x - self.width + dp(16)

        if (Window.height - instance_center[1]) > (
            instance.height / 2 + self.height + dp(12)
        ):
            pos_y = instance.y + instance.height + dp(12)
            self._pointer = "Downward"
        else:
            pos_y = instance.y - self.height - dp(12)
            self._pointer = "Upward"

        self.pos = instance.to_window(*[pos_x, pos_y])
        self.element_x = instance_center[0]

    def set_visibility(self, instance: Widget, visibility: bool, *args) -> None:
        if visibility:
            try:
                self.update_pos(instance)
                instance.bind(pos=self.update_pos)
                Window.add_widget(self)
            except Exception as e:
                print(e)
        else:
            try:
                instance.unbind(pos=self.update_pos)
                Window.remove_widget(self)
            except Exception:
                return
