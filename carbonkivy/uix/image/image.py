from __future__ import annotations

__all__ = ("CImage",)

from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.image import AsyncImage

from carbonkivy.behaviors import (
    DeclarativeBehavior,
)


class CImage(
    AsyncImage, DeclarativeBehavior
):

    ratio = ListProperty([4, 3])

    def __init__(self, *args, **kwargs):
        super(CImage, self).__init__(*args, **kwargs)
        self.size_hint = (1, None)
        self.bind(texture_size=self.adjust_image_size)
        Window.bind(size=self.adjust_image_size)

    def adjust_image_size(self, *args) -> None:
        w_ratio, h_ratio = self.ratio
        self.height = h_ratio / w_ratio * self.width
