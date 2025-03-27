from __future__ import annotations

__all__ = ("CScreen",)

from kivy.uix.screenmanager import Screen

from carbonkivy.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CScreen(BackgroundColorBehavior, Screen, DeclarativeBehavior):
    pass
