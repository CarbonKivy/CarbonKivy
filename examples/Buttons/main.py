from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 4))

appkv = """
CScreen:

    CButtonPrimary:
        text: "Primary Button"
        role: "Large Productive"
        icon: "add--large"
        pos_hint: {'center_y': 0.9, 'center_x': 0.35}

    CButtonPrimary:
        icon: "add--large"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.9, 'center_x': 0.8}

    CButtonSecondary:
        text: "Secondary Button"
        role: "Large Productive"
        icon: "add--large"
        pos_hint: {'center_y': 0.7, 'center_x': 0.35}

    CButtonSecondary:
        icon: "add--large"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.7, 'center_x': 0.8}

    CButtonTertiary:
        text: "Tertiary Button"
        role: "Large Productive"
        icon: "add--large"
        pos_hint: {'center_y': 0.5, 'center_x': 0.35}

    CButtonTertiary:
        icon: "add--large"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.5, 'center_x': 0.8}

    CButtonGhost:
        text: "Ghost Button"
        role: "Large Productive"
        icon: "add--large"
        pos_hint: {'center_y': 0.3,  'center_x': 0.35}

    CButtonGhost:
        icon: "add--large"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.3, 'center_x': 0.8}

    CButtonDanger:
        text: "Danger Button"
        role: "Large Productive"
        icon: "add--large"
        pos_hint: {'center_y': 0.1,  'center_x': 0.35}

    CButtonDanger:
        icon: "add--large"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.1, 'center_x': 0.8}
"""

from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.theme = "Gray100"

    def build(self, *args) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
