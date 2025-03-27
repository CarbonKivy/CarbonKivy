from __future__ import annotations

__all__ = ("CBoxLayout",)

from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CBoxLayout(
    AdaptiveBehavior, BackgroundColorBehavior, BoxLayout, DeclarativeBehavior
):
    pass
