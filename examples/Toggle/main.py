import os
import sys

from kivy.resources import resource_add_path

sys.path.insert(0, os.path.dirname(__file__))
resource_add_path(os.path.dirname(__file__))

from kivy.clock import Clock
from kivy.core.window import Window

def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    CToggle:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press:
            print("toggle")
        on_active:
            print(self.active)
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
