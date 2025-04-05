from kivy.core.window import Window
from kivy.clock import Clock


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    CButtonPrimary:
        text: "Primary Button"
        role: "Large Productive"
        icon: "add"
        pos_hint: {'center_y': 0.8, 'center_x': 0.35}

    CButtonPrimary:
        icon: "add"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.8, 'center_x': 0.8}

    CButtonSecondary:
        text: "Secondary Button"
        role: "Large Productive"
        icon: "add"
        pos_hint: {'center_y': 0.6, 'center_x': 0.35}

    CButtonSecondary:
        icon: "add"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.6, 'center_x': 0.8}

    CButtonGhost:
        text: "Ghost Button"
        role: "Large Productive"
        pos_hint: {'center_y': 0.4,  'center_x': 0.35}
        on_press:
            self.icon = "add"

    CButtonGhost:
        icon: "add"
        role: "2XL"
        spacing: 0
        pos_hint: {'center_y': 0.4, 'center_x': 0.8}

    CButtonTertiary:
        text: "Tertiary Button"
        role: "Large Productive"
        pos_hint: {'center_y': 0.2, 'center_x': 0.5}
        on_press:
            self.icon = "add"

"""

from kivy.lang import Builder
from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self, *args) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
