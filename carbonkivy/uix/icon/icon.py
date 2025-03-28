from __future__ import annotations

__all__ = ("CIcon",)

import os

from kivy.properties import ColorProperty, OptionProperty
from kivy.uix.label import Label

from carbonkivy.behaviors import BackgroundColorBehavior, DeclarativeBehavior
from carbonkivy.config import DATA
from carbonkivy.theme.icons import ibm_icons


class CIcon(BackgroundColorBehavior, DeclarativeBehavior, Label):
    """
    The CIcon class inherits from Label to display icons from IBM's icon library using the generated icon font.
    """

    icon = OptionProperty("", options=ibm_icons.keys())

    _color = ColorProperty(None, allownone=True)

    font_name = os.path.join(DATA, "Icons", "carbondesignicons.ttf")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_icon(self, *args) -> None:
        self.text = ibm_icons[self.icon]
