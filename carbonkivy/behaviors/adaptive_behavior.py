from __future__ import annotations

__all__ = ("AdaptiveBehavior",)

from kivy.properties import ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class AdaptiveBehavior:

    adaptive = ListProperty([False, False], length=2)

    def on_adaptive(self, *args) -> None:

        if self.adaptive[0] and self.adaptive[1]:
            self.size_hint = (None, None)
            if issubclass(self.__class__, Label):
                self.text_size = (None, None)
                self.bind(
                    texture_size=lambda *x: self.setter("size")(self, self.texture_size)
                )
            else:
                if not isinstance(self, (FloatLayout, Screen)):
                    self.bind(minimum_size=self.setter("size"))
                    if not self.children:
                        self.size = (0, 0)

        elif self.adaptive[0]:
            self.size_hint_x = None
            if issubclass(self.__class__, Label):
                self.bind(
                    texture_size=lambda *x: self.setter("width")(
                        self, self.texture_size[0]
                    )
                )
            else:
                if not isinstance(self, (FloatLayout, Screen)):
                    self.bind(minimum_width=self.setter("width"))
                    if not self.children:
                        self.width = 0

        elif self.adaptive[1]:
            self.size_hint_y = None
            if issubclass(self.__class__, Label):
                self.bind(
                    texture_size=lambda *x: self.setter("height")(
                        self, self.texture_size[1]
                    )
                )
            else:
                if not isinstance(self, (FloatLayout, Screen)):
                    self.bind(minimum_height=self.setter("height"))
                    if not self.children:
                        self.height = 0
