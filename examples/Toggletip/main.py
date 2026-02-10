from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    TooltipButton:
        text: "Drag Me"
        icon: "add--large"
        pos: [dp(30), dp(30)]
    
    CCheckbox:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

<MToggletip>:
    CLabel:
        text: root.text
        color: app.text_inverse
    
    CButtonPrimary:
        text: "View more"
        role: "Large Productive"
"""

from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from carbonkivy.app import CarbonApp
from carbonkivy.behaviors import ElevationBehavior, TooltipBehavior
from carbonkivy.uix.button import CButtonPrimary
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.toggletip import CToggletip
from carbonkivy.uix.tooltip import CTooltip


class MToggletip(CToggletip):

    text = StringProperty()


class TooltipButton(CButtonPrimary, ElevationBehavior, TooltipBehavior):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tooltip = MToggletip(
            text="This is a large Toggletip text.",
            width=dp(288),
            margin=dp(2),
            pointer="Upward",
        )

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
