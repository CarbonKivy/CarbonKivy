from __future__ import annotations

__all__ = ("CScreenManager",)

from kivy.uix.screenmanager import ScreenManager

from carbonkivy.behaviors import BackgroundColorBehaviorRectangular, DeclarativeBehavior


class CScreenManager(
    BackgroundColorBehaviorRectangular, ScreenManager, DeclarativeBehavior
):
    pass
