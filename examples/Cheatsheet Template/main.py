"""
Author:
    Kartavya Shukla
        - Github: Novfensec (https://github.com/Novfensec)
"""

from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))


from carbonkivy.app import CarbonApp
from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.button import CButtonPrimary
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager
from carbonkivy.uix.notification import CNotificationInline, CNotificationToast


class Tile(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    BoxLayout,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
):

    header = StringProperty()

    description = StringProperty()


class UI(CScreenManager):
    pass


class CheatSheetScreen(CScreen):
    pass


from carbonkivy.devtools import LiveApp

class myapp(CarbonApp, LiveApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        # self.load_all_kv_files(self.directory)

    def build_app(self) -> CScreenManager:
        self.manager_screens = CScreenManager()
        self.manager_screens.add_widget(CheatSheetScreen(name="cheatsheet"))
        return self.manager_screens

    def notify_error(self, variant: str = "Inline", *args) -> None:
        self.notification = (
            CNotificationInline(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
            ).open()
            if variant == "Inline"
            else CNotificationToast(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
                time_caption_enabled=True,
            ).open()
        )

    def notify_success(self, variant: str = "Inline", *args) -> None:
        self.notification = (
            CNotificationInline(
                title="Server instance created",
                subtitle="The server instance has successfully been created.",
                status="Success",
            ).open()
            if variant == "Inline"
            else CNotificationToast(
                title="Server instance created",
                subtitle="The server instance has successfully been created.",
                status="Success",
                time_caption_enabled=True,
            ).open()
        )

    def notify_info(self, variant: str = "Inline", *args) -> None:
        self.notification = (
            CNotificationInline(
                title="Server instance updated",
                subtitle="The server instance location has been updated.",
                status="Info",
            ).open()
            if variant == "Inline"
            else CNotificationToast(
                title="Server instance updated",
                subtitle="The server instance location has been updated.",
                status="Info",
                # time_caption_enabled=True,
                action_button=CButtonPrimary(text="View Server"),
            ).open()
        )

    def notify_warning(self, variant: str = "Inline", *args) -> None:
        self.notification = (
            CNotificationInline(
                title="Server instance storage",
                subtitle="The server instance is reaching storage capacity.",
                status="Warning",
            ).open()
            if variant == "Inline"
            else CNotificationToast(
                title="Server instance storage",
                subtitle="The server instance is reaching storage capacity.",
                status="Warning",
                time_caption_enabled=True,
            ).open()
        )

    
if __name__ == "__main__":
    app = myapp()
    app.run()