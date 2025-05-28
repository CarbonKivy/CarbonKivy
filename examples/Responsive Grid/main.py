from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    StackLayout:
        size_hint: 1, 1
        padding: dp(16)

        CGridLayout:
            responsive: True
            min_cols: 2
            cols: 2 # default number of columns on start
            max_cols: 4
            scale_width: dp(200)
            adaptive: [False, True]
            spacing: dp(8)

            CBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                bg_color: app.interactive

            CBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                bg_color: app.interactive

            CBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                bg_color: app.interactive

            CBoxLayout:
                orientation: 'vertical'
                size_hint: 1, None
                height: dp(200)
                bg_color: app.interactive

"""

from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
