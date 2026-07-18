from __future__ import annotations

__all__ = ("CScrollView",)

from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.graphics import PopMatrix, PushMatrix, Scale

from carbonkivy.behaviors import BackgroundColorBehaviorRectangular, DeclarativeBehavior
from carbonkivy.effects import ElasticScrollEffect


class ElasticScrollView(ScrollView):

    effect_cls = ElasticScrollEffect
    _internal_scale = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            PushMatrix()
            self._internal_scale = Scale(1)
        with self.canvas.after:
            PopMatrix()

        self.effect_y.scale_axis = "y"
        self.effect_x.scale_axis = "x"

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.effect_x.last_touch_pos = touch.pos
            self.effect_y.last_touch_pos = touch.pos
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.effect_x.convert_overscroll(touch)
            self.effect_y.convert_overscroll(touch)
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.effect_x.reset_scale()
        self.effect_y.reset_scale()
        return super().on_touch_up(touch)


class CScrollView(
    BackgroundColorBehaviorRectangular, ElasticScrollView, DeclarativeBehavior
):
    pass
