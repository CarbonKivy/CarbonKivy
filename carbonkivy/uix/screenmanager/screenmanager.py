from __future__ import annotations

__all__ = ("CScreenManager",)

from kivy.uix.screenmanager import FadeTransition, ScreenManager

from carbonkivy.behaviors import BackgroundColorBehaviorRectangular, DeclarativeBehavior


class CScreenManager(
    BackgroundColorBehaviorRectangular, ScreenManager, DeclarativeBehavior
):

    def __init__(self, **kwargs):
        super(CScreenManager, self).__init__(**kwargs)
        self.transition = FadeTransition(duration=0.05, clearcolor=[1, 1, 1, 0])
