from __future__ import annotations

__all__ = ("CScrollView",)

from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView

from carbonkivy.behaviors import BackgroundColorBehaviorRectangular, DeclarativeBehavior


class CScrollView(BackgroundColorBehaviorRectangular, ScrollView, DeclarativeBehavior):

    effect_cls = OpacityScrollEffect
