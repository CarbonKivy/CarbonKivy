from __future__ import annotations

__all__ = ("CStackLayout",)

from kivy.uix.stacklayout import StackLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CStackLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StackLayout,
    DeclarativeBehavior,
):
    pass
