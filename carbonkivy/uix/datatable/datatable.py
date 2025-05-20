from __future__ import annotations

__all__ = ("CDatatable",)

from kivy.properties import DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

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

    widget_matrix = DictProperty()

    def add_widget(self, widget, *args, **kwargs):
        self.widget_matrix[widget.row][widget.column] = widget
        return super().add_widget(widget, *args, **kwargs)


class CDataRow(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    GridLayout,
):
    pass
