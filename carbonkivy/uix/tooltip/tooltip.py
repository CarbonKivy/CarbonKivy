from __future__ import annotations

__all__ = ("CTooltip",)

from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class CTooltip(BoxLayout):

    visible = BooleanProperty(False)

    bg_color = ColorProperty()

    text_color = ColorProperty()

    text = StringProperty()

    def __init__(self, **kwargs) -> None:
        super(CTooltip, self).__init__(**kwargs)

    def update_pos(self, instance: Widget, *args) -> None:
        self.pos = instance.to_window(*[instance.x + instance.width/2 - self.width/2, instance.y + instance.height + dp(12)])

    @mainthread
    def set_visibility(self, instance: Widget, visibility: bool, *args) -> None:
        if visibility:
            try:
                self.update_pos(instance)
                Window.add_widget(self)
            except Exception as e:
                print(e)
        else:
            try:
                Window.remove_widget(self)
            except Exception:
                return
