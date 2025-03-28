from kivy.core.window import Window
from kivy.clock import Clock


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager


class UI(CScreenManager):
    pass


class HomeScreen(CScreen):
    pass


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.load_all_kv_files(self.directory)

    def build(self) -> CScreenManager:
        self.manager_screens = CScreenManager()
        self.manager_screens.add_widget(HomeScreen(name="home"))
        return self.manager_screens


if __name__ == "__main__":
    myapp().run()
