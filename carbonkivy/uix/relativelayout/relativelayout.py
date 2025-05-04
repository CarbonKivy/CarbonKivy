from __future__ import annotations

__all__ = ("CRelativeLayout",)

from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CRelativeLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    RelativeLayout,
    DeclarativeBehavior,
):
    pass
