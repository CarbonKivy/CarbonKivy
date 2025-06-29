from __future__ import annotations

__all__ = ("FocusContainer",)

from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
    StateFocusBehavior,
)


class FocusContainer(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    BoxLayout,
    DeclarativeBehavior,
    HoverBehavior,
):
    focus = BooleanProperty(False)

    def __init__(self, **kwargs) -> None:
        super(FocusContainer, self).__init__(**kwargs)
