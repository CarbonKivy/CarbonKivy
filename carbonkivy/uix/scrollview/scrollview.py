from __future__ import annotations

__all__ = ("CScrollView",)

from kivy.uix.scrollview import ScrollView

from carbonkivy.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CScrollView(BackgroundColorBehavior, ScrollView, DeclarativeBehavior):
    pass
