from __future__ import annotations

__all__ = ("CBoxLayout",)

from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CBoxLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    BoxLayout,
    DeclarativeBehavior,
):
    pass
