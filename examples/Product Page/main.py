from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))


from carbonkivy.app import CarbonApp
from carbonkivy.uix.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager
from carbonkivy.utils import update_system_ui
from carbonkivy.uix.icon import CIconCircular
from carbonkivy.behaviors import StateFocusBehavior


class SelectableIcon(CIconCircular, StateFocusBehavior, ButtonBehavior):
    def on_focus(self, *args) -> None:
        super().on_focus(*args)
        if self.focus:
            for child in self.parent.children:
                if child != self:
                    child.focus = not self.focus


class UI(CScreenManager):
    pass


class ProductScreen(CScreen):
    pass


class myapp(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.load_all_kv_files(self.directory)

    def build(self) -> CScreenManager:
        update_system_ui(get_color_from_hex("#B3E140"), self.background, "Dark")
        self.manager_screens = CScreenManager()
        self.manager_screens.add_widget(ProductScreen(name="product"))
        return self.manager_screens

    
if __name__ == "__main__":
    app = myapp()
    app.run()