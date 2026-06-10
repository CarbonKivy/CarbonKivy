from carbonkivy.app import CarbonApp
from carbonkivy.effects import ShimmerEffect
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty, ColorProperty
from kivy.graphics import RenderContext
from kivy.core.window import Window

class ShimmerLabel(ShimmerEffect, Label):
    pass

class ShimmerImage(ShimmerEffect, AsyncImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_load(self):
        self.shimmering = False

Builder.load_string('''
<MainScreen>:
    orientation: 'vertical'
    padding: 50
    spacing: 20
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    ShimmerImage:
        source: ""
        shimmering: True
        size_hint: None, None
        size: dp(576), dp(576)
        fit_mode: "contain"
        pos_hint: {'center_x': .5}
''')

class MainScreen(BoxLayout):
    pass

class TestApp(CarbonApp):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    TestApp().run()