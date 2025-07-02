from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    TooltipButton:
        icon: "add--large"
        pos_hint: {"center_x": 0.8, "center_y": 0.8}
"""

from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.behaviors import TooltipBehavior
from carbonkivy.uix.button import CButtonPrimary
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.tooltip import CTooltip


class TooltipButton(CButtonPrimary, TooltipBehavior):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tooltip = CTooltip(text="This is a tooltip.")


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
