from __future__ import annotations

__all__ = ("CLabel",)

from kivy.clock import mainthread
from kivy.properties import NumericProperty, OptionProperty
from kivy.uix.label import Label

from carbonkivy.behaviors import AdaptiveBehavior  # SelectionBehavior
from carbonkivy.behaviors import BackgroundColorBehaviorRectangular
from carbonkivy.theme.size_tokens import font_style_tokens
from carbonkivy.utils import get_font_name


class CLabel(AdaptiveBehavior, BackgroundColorBehaviorRectangular, Label):

    style = OptionProperty("body_compact_02", options=font_style_tokens.keys())

    typeface = OptionProperty(
        "IBM Plex Sans", options=["IBM Plex Sans", "IBM Plex Serif", "IBM Plex Mono"]
    )

    weight_style = OptionProperty(
        "Regular",
        options=[
            "Bold",
            "BoldItalic",
            "ExtraLight",
            "ExtraLightItalic",
            "Italic",
            "Light",
            "LightItalic",
            "Medium",
            "MediumItalic",
            "Regular",
            "SemiBold",
            "SemiBoldItalic",
            "Thin",
            "ThinItalic",
        ],
    )

    _font_size = NumericProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(CLabel, self).__init__(**kwargs)
        self.update_specs()

    def on_style(self, *args) -> None:
        self.update_specs()

    def on_typeface(self, *args) -> None:
        self.update_specs()

    def on_weight_style(self, *args) -> None:
        self.update_specs()

    @mainthread
    def update_specs(self, *args):
        try:
            self.weight_style = font_style_tokens[self.style]["weight_style"]
        except Exception as e:  # nosec
            pass
        self.font_name = get_font_name(self.typeface, self.weight_style)
