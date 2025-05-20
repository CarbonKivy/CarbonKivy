from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    CBoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(128)
        adaptive: [True, True]
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        CLink:
            url: "https://github.com/CarbonKivy/CarbonKivy"
            external: True
            pos_hint: {"center_y": 0.6}

            CLinkLabel:
                text: "Standalone Link"
            
            CLinkIcon:
                icon: "arrow--up-right"

        CLink:
            text: "Standalone Link Visited"
            url: "https://github.com/CarbonKivy/CarbonKivy"
            external: True
            cstate: "visited"
            pos_hint: {"center_y": 0.6}

            CLinkIcon:
                icon: "arrow--up-right"

        CLink:
            text: "Standalone Link Active"
            url: "https://github.com/CarbonKivy/CarbonKivy"
            external: True
            cstate: "active"
            pos_hint: {"center_y": 0.6}

            CLinkIcon:
                icon: "arrow--up-right"

        CLink:
            text: "Standalone Link Disabled"
            url: "https://github.com/CarbonKivy/CarbonKivy"
            external: True
            cstate: "disabled"
            pos_hint: {"center_y": 0.6}

            CLinkIcon:
                icon: "arrow--up-right"

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
