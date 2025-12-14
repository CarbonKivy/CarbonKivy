import os
import sys

from kivy.resources import resource_add_path

sys.path.insert(0, os.path.dirname(__file__))
resource_add_path(os.path.dirname(__file__))

from kivy.clock import Clock
from kivy.core.window import Window


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

from carbonkivy.app import CarbonApp
from carbonkivy.uix.modal import CModal
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager


class DomainModal(CModal):
    pass


class UI(CScreenManager):
    pass


class HomeScreen(CScreen):
    pass


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.load_all_kv_files(self.directory)
        self.modal = DomainModal()

    def build(self) -> CScreenManager:
        self.manager_screens = CScreenManager()
        self.manager_screens.add_widget(HomeScreen(name="home"))
        return self.manager_screens


if __name__ == "__main__":
    myapp().run()
