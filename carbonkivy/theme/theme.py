from kivy.core.window import Window
from kivy.utils import colormap, get_color_from_hex
from kivy.event import EventDispatcher
from kivy.properties import OptionProperty, ListProperty

from carbonkivy.theme.color_tokens import thematic_tokens, static_tokens
from carbonkivy.theme.colors import ThematicColors, StaticColors


class CarbonTheme(EventDispatcher, ThematicColors, StaticColors):

    theme = OptionProperty("White", options=["White", "Gray10", "Gray90", "Gray100"])

    thematic_color_tokens = ListProperty(list(thematic_tokens.keys()))

    static_color_tokens = ListProperty(list(static_tokens.keys()))

    color_tokens = ListProperty(
        list(thematic_tokens.keys()) + list(static_tokens.keys())
    )

    def __init__(self) -> None:
        super().__init__()
        static_tokenmap = {
            token: get_color_from_hex(hex) for token, hex in static_tokens.items()
        }
        colormap.update(static_tokenmap)
        colormap.update(self.parse_thematic_tokens())
        Window.clearcolor = colormap["background"]
        self.update_thematic_colors()

    def on_theme(self, *args) -> None:
        colormap.update(self.parse_thematic_tokens())
        Window.clearcolor = colormap["background"]
        self.update_thematic_colors()

    def parse_thematic_tokens(self):
        tokenmap = {}
        for token, values in thematic_tokens.items():
            color_value = values[self.theme]
            if isinstance(color_value, tuple):  # Handle (hex, alpha)
                rgba = get_color_from_hex(color_value[0])
                rgba[3] = color_value[1]  # Set transparency
            else:
                rgba = get_color_from_hex(color_value)
            tokenmap[token] = rgba
        return tokenmap

    def update_thematic_colors(self, *args) -> None:
        for token in self.thematic_color_tokens:
            setattr(self, token, colormap[token])
