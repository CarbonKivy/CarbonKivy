from __future__ import annotations

__all__ = ("CBaseIcon", "CIcon", "CIconCircular")

import os

from kivy.properties import ColorProperty, OptionProperty
from kivy.uix.label import Label

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorCircular,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
)
from carbonkivy.config import DATA
from carbonkivy.theme.icons import ibm_icons


class CBaseIcon(AdaptiveBehavior, DeclarativeBehavior, Label):
    """
    The CBaseIcon class inherits from Label to display icons from IBM's icon library using the generated icon font.
    """

    icon = OptionProperty("", options=ibm_icons.keys())

    _color = ColorProperty(None, allownone=True)

    font_name = os.path.join(DATA, "Icons", "carbondesignicons.ttf")

    def __init__(self, **kwargs) -> None:
        super(CBaseIcon, self).__init__(**kwargs)

    def on_icon(self, *args) -> None:
        self.text = ibm_icons[self.icon]


class CIcon(BackgroundColorBehaviorRectangular, CBaseIcon):
    pass


class CIconCircular(BackgroundColorBehaviorCircular, CBaseIcon):
    pass
