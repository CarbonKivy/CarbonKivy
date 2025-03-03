from kivy.core.window import Window
from kivy.clock import Clock


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
Screen:
    CButtonPrimary:
        text: "Primary Large"
        role: "Extra Large"
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}

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
