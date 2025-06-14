from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

from kivy.lang import Builder

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.notification import CNotificationInline, CNotificationToast


class myapp(CarbonApp):

    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)

    def build(self) -> CScreen:
        screen = Builder.load_file("main.kv")
        return screen

    def notify_error(self, variant: str = "Inline", *args) -> None:
        self.notification = CNotificationInline(
            title="Server instance unavailable",
            subtitle="The server instance is no longer running because of an error.",
            status="Error",
        ).open() if variant=="Inline" else CNotificationToast(
            title="Server instance unavailable",
            subtitle="The server instance is no longer running because of an error.",
            status="Error",
            time_caption_enabled=True,
        ).open()

    def notify_success(self, variant: str = "Inline", *args) -> None:
        self.notification = CNotificationInline(
            title="Server instance created",
            subtitle="The server instance has successfully been created.",
            status="Success",
        ).open() if variant=="Inline" else CNotificationToast(
            title="Server instance created",
            subtitle="The server instance has successfully been created.",
            status="Success",
            time_caption_enabled=True,
        ).open()

    def notify_info(self, variant: str = "Inline", *args) -> None:
        self.notification = CNotificationInline(
            title="Server instance updated",
            subtitle="The server instance location has been updated.",
            status="Info",
        ).open() if variant=="Inline" else CNotificationToast(
            title="Server instance updated",
            subtitle="The server instance location has been updated.",
            status="Info",
            time_caption_enabled=True,
        ).open()

    def notify_warning(self, variant: str = "Inline", *args) -> None:
        self.notification = CNotificationInline(
            title="Server instance storage",
            subtitle="The server instance is reaching storage capacity.",
            status="Warning",
        ).open() if variant=="Inline" else CNotificationToast(
            title="Server instance storage",
            subtitle="The server instance is reaching storage capacity.",
            status="Warning",
            time_caption_enabled=True,
        ).open()


if __name__ == "__main__":
    myapp().run()
