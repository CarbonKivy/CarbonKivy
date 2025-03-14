from __future__ import annotations

__all__ = ("CLabel",)

from kivy.clock import mainthread
from kivy.properties import NumericProperty, OptionProperty
from kivy.uix.label import Label

# from carbonkivy.behaviors import BackgroundColorBehavior # SelectionBehavior
from carbonkivy.theme.size_tokens import font_style_tokens
from carbonkivy.utils import get_font_name


class CLabel(Label):
    style = OptionProperty("body_compact_02", options=[font_style_tokens.keys()])

    typeface = OptionProperty(
        "IBM Plex Sans", options=["IBM Plex Sans", "IBM Plex Serif", "IBM Plex Mono"]
    )

    weight_style = OptionProperty(
        "Regular",
        options=[
            "Regular",
            "Bold",
            "SemiBold",
            "Italic",
            "Thin",
            "Light",
            "ExtraLight",
            "Medium",
            "BoldItalic",
            "SemiBoldItalic",
        ],
    )

    _font_size = NumericProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(CLabel, self).__init__(**kwargs)
        self.update_specs()

    def on_style(self, *args) -> None:
        self.update_specs()

    def on_typeface(self, *args) -> None:
        self.update_specs()

    def on_weight_style(self, *args) -> None:
        self.update_specs()

    @mainthread
    def update_specs(self, **kwargs):
        self.font_name = get_font_name(self.typeface, self.weight_style)
        self._font_size = font_style_tokens[self.style]["font_size"]
        self.line_height = font_style_tokens[self.style]["line_height"]
