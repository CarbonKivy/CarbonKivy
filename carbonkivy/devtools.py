import glob
import os

from kaki.app import App
from kivy.clock import mainthread
from kivy.factory import Factory


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

        lbl = Factory.CLabel(
            padding=16,
            text="{}\n\n{}".format(exc, tb or ""),
        )
        lbl.texture_update()
        sv = Factory.ScrollView(
            size_hint=(1, 1), pos_hint={"x": 0, "y": 0}, do_scroll_x=False, scroll_y=0
        )
        sv.add_widget(lbl)
        self.set_widget(sv)
