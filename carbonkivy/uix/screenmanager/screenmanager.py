from __future__ import annotations

__all__ = ("CScreenManager",)

from kivy.uix.screenmanager import ScreenManager

from carbonkivy.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
)


class CScreenManager(BackgroundColorBehavior, ScreenManager, DeclarativeBehavior):
    pass
