import glob
import os

from kaki.app import App
from kivy.clock import mainthread
from kivy.factory import Factory
from kivy.metrics import sp


class LiveApp(App):

    def __init__(self, **kwargs) -> None:
        super(LiveApp, self).__init__(**kwargs)
        self.DEBUG = True
        self.RAISE_ERROR = False

        self.CLASSES = {self.root: "main"}  # main file name or root file name

        self.AUTORELOADER_PATHS = [
            (self.directory, {"recursive": True}),
        ]
        for file in glob.glob(
            os.path.join(self.directory, "**", "*.kv"), recursive=True
        ):
            self.KV_FILES.append(file)

    @mainthread
    def set_error(self, exc, tb=None):
        from kivy.core.window import Window

        clean_exc = str(exc)[:2500].replace("\\n", "\n")
        clean_tb = (str(tb)[:2500] or "").replace("\\n", "\n")
        output = "{}...\n\n{}...".format(clean_exc, clean_tb or "")
        lbl = Factory.CLabel(
            padding=16,
            typeface="IBM Plex Mono",
            color=App.get_running_app().text_primary,
        )
        lbl.text = f"{output}"
        lbl.font_size = sp(12)
        lbl.texture_update()
        sv = Factory.CScrollView(
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
            do_scroll_x=False,
            scroll_y=0,
            bg_color=App.get_running_app().layer_01,
        )
        sv.add_widget(lbl)
        self.set_widget(sv)
