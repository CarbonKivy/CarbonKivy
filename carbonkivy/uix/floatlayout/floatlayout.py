from __future__ import annotations

__all__ = ("CFloatLayout",)

from kivy.uix.floatlayout import FloatLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CFloatLayout(
    AdaptiveBehavior, BackgroundColorBehavior, FloatLayout, DeclarativeBehavior
):
    pass
