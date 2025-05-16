from __future__ import annotations

__all__ = ("CDatatable",)

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
    StateFocusBehavior,
)


class CDatatable(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
    StateFocusBehavior,
    BoxLayout,
):
    pass
