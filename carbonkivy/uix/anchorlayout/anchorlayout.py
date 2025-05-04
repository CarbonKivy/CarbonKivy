from __future__ import annotations

__all__ = ("CAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CAnchorLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    AnchorLayout,
    DeclarativeBehavior,
):
    pass
