from __future__ import annotations

__all__ = ("CAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CAnchorLayout(
    AdaptiveBehavior, BackgroundColorBehavior, AnchorLayout, DeclarativeBehavior
):
    pass
