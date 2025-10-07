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
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager
from carbonkivy.uix.dropdown import CDropdown


class CustomDropdown(CDropdown):

    def __init__(self, **kwargs) -> None:
        super(CustomDropdown, self).__init__(**kwargs)


class UI(CScreenManager):
    pass


class HomeScreen(CScreen):

    def on_kv_post(self, base_widget: object) -> None:
        self.filter_dropdown = CustomDropdown(master=self.ids.filter_btn)
        return super().on_kv_post(base_widget)


class myapp(CarbonApp):

    def __init__(self, *args, **kwargs) -> None:
        super(myapp, self).__init__(*args, **kwargs)
        self.load_all_kv_files(self.directory)

    def build(self) -> CScreenManager:
        self.manager_screens = CScreenManager()
        self.manager_screens.add_widget(HomeScreen(name="home"))
        return self.manager_screens


if __name__ == "__main__":
    myapp().run()
