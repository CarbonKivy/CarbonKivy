from __future__ import annotations

__all__ = ("CRelativeLayout",)

from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CRelativeLayout(
    AdaptiveBehavior, BackgroundColorBehavior, RelativeLayout, DeclarativeBehavior
):
    pass
