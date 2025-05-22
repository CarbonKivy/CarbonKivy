from __future__ import annotations

__all__ = ("CImage",)

from kivy.clock import mainthread
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.image import AsyncImage

from carbonkivy.behaviors import DeclarativeBehavior


class CImage(AsyncImage, DeclarativeBehavior):

    ratio = ListProperty([4, 3])

    height_ratio = NumericProperty()

    width_ratio = NumericProperty()

    def __init__(self, *args, **kwargs) -> None:
        super(CImage, self).__init__(*args, **kwargs)
        self.on_ratio()
        self.bind(texture_size=self.adjust_image_size)

    @mainthread
    def on_ratio(self, *args) -> None:
        w_ratio, h_ratio = self.ratio
        self.height_ratio = h_ratio / w_ratio
        self.width_ratio = 1 / self.height_ratio

    @mainthread
    def adjust_image_size(self, *args) -> None:
        if self.size_hint_y == None:
            self.height = self.width * self.height_ratio
        elif self.size_hint_x == None:
            self.width *= self.height * self.width_ratio
