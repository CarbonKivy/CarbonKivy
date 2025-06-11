from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

appkv = """
CScreen:

    StackLayout:
        size_hint: 1, 1
        padding: dp(16)

        CButtonPrimary:
            text: "Show notification"
            icon: "popup"
            on_press:
                app.notification.open()
"""

from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.notification import CNotificationInline


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.notification = CNotificationInline(
            title="Server Instance Created",
            subtitle="The server instance has been successfully created.",
        )

    def build(self) -> CScreen:
        screen = Builder.load_string(appkv)
        return screen


if __name__ == "__main__":
    myapp().run()
