from __future__ import annotations

__all__ = ("CStackLayout",)

from kivy.uix.stacklayout import StackLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CStackLayout(
    AdaptiveBehavior, BackgroundColorBehavior, StackLayout, DeclarativeBehavior
):
    pass
