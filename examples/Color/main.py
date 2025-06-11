from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:
    ColorView:
        size_hint: 1, 1
        viewclass: "MyColor"
        bar_width: "20dp"
        do_scroll_x: False
        scroll_type: ['bars', 'content']

        RecycleGridLayout:
            cols: 2
            default_size: None, None
            default_size_hint: 1, None
            size_hint: 1, None
            height: self.minimum_height
            padding: [dp(16), dp(16), dp(16), dp(16)]
            spacing: dp(20)

<MyColor@CAnchorLayout>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    token: ""
    padding: dp(16)

    CLabel:
        text: root.token
        padding: dp(4)
        bg_color: [1, 1, 1, 0.6]
        color: app.text_primary
"""

from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

from carbonkivy.theme.color_tokens import thematic_tokens, static_tokens
from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen


class ColorView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = CarbonApp.get_running_app()
        self.data = []
        tokenl = {}
        tokenl.update(thematic_tokens)
        tokenl.update(static_tokens)
        for token in tokenl.keys():
            if hasattr(self.app, token):
                self.data.extend(
                    [
                        {
                            "bg_color": getattr(self.app, token),
                            "token": token,
                        }
                    ]
                )


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
