from kivy.core.window import Window
from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen


appkv = """
CScreen:
    CStackLayout:
        size_hint: 1, 1
        
        CBoxLayout:
            orientation: "vertical"
            adaptive: [False, True]
            padding: [dp(20), dp(20), dp(20), dp(20)]

            CodeSnippet:
                size_hint: 1, None
                text: "import os"
                # style_name: "monokai" # pygments builtin styles
                # bg_color: app.background_inverse
                # icon_color:
                # icon_color_hover:
                # icon_color_active
                # icon_bg_color:
                # icon_bg_color_active:
"""


class MyApp(CarbonApp):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    MyApp().run()
