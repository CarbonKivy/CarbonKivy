from __future__ import annotations

__all__ = ("CGridLayout",)

from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import BooleanProperty, NumericProperty, OptionProperty
from kivy.uix.gridlayout import GridLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)


class CGridLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    GridLayout,
):

    max_cols = NumericProperty(4)
    """
    Maximum number of columns in the grid.
    """

    min_cols = NumericProperty(1)
    """
    Minimum number of columns in the grid.
    """

    max_rows = NumericProperty(4)
    """
    Maximum number of rows in the grid.
    """

    min_rows = NumericProperty(1)
    """
    Minimum number of rows in the grid.
    """

    responsive = BooleanProperty(False)
    """
    Wether to show responsive behavior or not.
    """

    responsive_attr = OptionProperty("cols", options=["cols", "rows", "both"])
    """
    The attribute of the grid for responsive behavior.
    """

    scale_height = NumericProperty(dp(250))
    """
    Height of a single element.
    """

    scale_width = NumericProperty(dp(250))
    """
    Width of a single element.
    """

    def __init__(self, **kwargs) -> None:
        super(CGridLayout, self).__init__(**kwargs)

    def on_responsive(self, *args) -> None:
        if self.responsive:
            if self.responsive_attr == ("cols" or "both"):
                Window.bind(size=self.adjust_cols)
            if self.responsive_attr == ("rows" or "both"):
                Window.bind(size=self.adjust_rows)
        else:
            Window.unbind(size=self.adjust_cols)
            Window.unbind(size=self.adjust_rows)

    @mainthread
    def adjust_cols(self, *args) -> None:
        width = self.size[0]
        for x in range(self.min_cols, -~self.max_cols):
            if (self.scale_width * x) < width < (self.scale_width * (-~x)):
                self.cols = x
                break

    @mainthread
    def adjust_rows(self, *args) -> None:
        height = self.size[1]
        for x in range(self.min_rows, -~self.max_rows):
            if (self.scale_height * x) < height < (self.scale_height * (-~x)):
                self.rows = x
                break
