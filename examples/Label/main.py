from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    CLabel:
        text: "IBM Plex Sans"
        style: "heading_04"
        typeface: "IBM Plex Sans"
        weight_style: "Medium"
        halign: "center"
        pos_hint: {"center_y": 0.8}

    CLabel:
        text: "IBM Plex Serif"
        style: "heading_04"
        typeface: "IBM Plex Serif"
        weight_style: "Medium"
        halign: "center"
        pos_hint: {"center_y": 0.5}

    CLabel:
        text: "IBM Plex Mono"
        style: "heading_04"
        typeface: "IBM Plex Mono"
        weight_style: "Medium"
        halign: "center"
        pos_hint: {"center_y": 0.2}
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
