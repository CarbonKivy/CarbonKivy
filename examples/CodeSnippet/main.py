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

            CodeSnippetLayout:

                CodeSnippet:
                    text: "import os"

                CodeSnippetCopyButton:
"""


class MyApp(CarbonApp):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    MyApp().run()
