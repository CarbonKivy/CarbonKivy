from __future__ import annotations

__all__ = ("CIcon",)

import os

from kivy.properties import OptionProperty
from kivy.uix.label import Label

from carbonkivy.config import DATA
from carbonkivy.theme.icons import ibm_icons


class CIcon(Label):
    """
    The CIcon class inherits from Label to display icons from IBM's icon library using the generated icon font.
    """

    icon = OptionProperty("", options=ibm_icons.keys())

    font_name = os.path.join(DATA, "Icons", "carbondesignicons.ttf")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_style(self, *args) -> None:
        self.update_specs()

    def on_icon(self, *args) -> None:
        self.text = ibm_icons[self.icon]
