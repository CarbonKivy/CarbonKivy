from kivy.core.window import Window
from kivy.clock import Clock


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))
Window.clearcolor = [1, 1, 1, 1]

appkv = """
Screen:
    Button:
        text: "White"
        background_color: app.layer_02
        size_hint: 0.5, 0.2
        size: self.size
        pos_hint: {'center_y': 0.9}
        on_touch_up:
            self.background_color = "interactive"

"""

from kivy.lang import Builder
from carbonkivy.app import CarbonApp


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self):
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
