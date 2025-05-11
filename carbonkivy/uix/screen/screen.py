from __future__ import annotations

__all__ = ("CScreen",)

from kivy.uix.screenmanager import Screen

from carbonkivy.behaviors import BackgroundColorBehaviorRectangular, DeclarativeBehavior


class CScreen(BackgroundColorBehaviorRectangular, Screen, DeclarativeBehavior):
    pass
