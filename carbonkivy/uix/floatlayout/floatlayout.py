from __future__ import annotations

__all__ = ("CFloatLayout",)

from kivy.uix.floatlayout import FloatLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CFloatLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    FloatLayout,
    DeclarativeBehavior,
):
    pass
