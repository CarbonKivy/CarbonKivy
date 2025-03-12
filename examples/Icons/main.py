from kivy.core.window import Window
from kivy.clock import Clock


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
Screen:
    IconView:
        size_hint: 1, 1
        viewclass: "MyIcon"
        do_scroll_x: False
        RecycleGridLayout:
            cols: 3
            default_size_hint: 1, None
            default_size: "32dp", "32dp"
            size_hint: 1, None
            height: self.minimum_height
            padding: [dp(16), dp(16), dp(16), dp(16)]
            spacing: dp(20)

<MyIcon@CIcon>:
    font_size: plex_32
    pos_hint: {'center_x': 0.5}
"""

from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from carbonkivy.app import CarbonApp
from carbonkivy.theme.icons import ibm_icons

class IconView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        for icons in ibm_icons.keys():
            self.data.extend([{"icon":icons}])


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self):
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
