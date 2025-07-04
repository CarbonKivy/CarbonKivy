from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    TooltipButton:
        text: "Drag Me"
        icon: "add--large"
        pos: [30, 30]
"""

from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang import Builder
from kivy.metrics import dp

from carbonkivy.app import CarbonApp
from carbonkivy.behaviors import TooltipBehavior
from carbonkivy.uix.button import CButtonPrimary
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.tooltip import CTooltip


class TooltipButton(CButtonPrimary, TooltipBehavior):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tooltip = CTooltip(text="This is a large Tooltip text.", width=dp(200))

    def on_touch_move(self, touch: MouseMotionEvent, *args) -> bool | None:
        self.center_x, self.center_y = touch.pos
        return super().on_touch_move(touch)


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
