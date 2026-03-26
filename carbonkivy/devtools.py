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

        clean_exc = exc[:1000].replace("\\n", "\n")
        clean_tb = (tb[:1000] or "").replace("\\n", "\n")
        output = "{}\n\n{}".format(clean_exc[:1000], clean_tb[:1000] or "")
        lbl = Factory.CLabel(
            markup=True,
            padding=16,
            typeface="IBM Plex Mono",
            text=f"{output}",
        )
        lbl.font_size = sp(12)
        lbl.texture_update()
        sv = Factory.ScrollView(
            size_hint=(1, 1), pos_hint={"x": 0, "y": 0}, do_scroll_x=False, scroll_y=0
        )
        sv.add_widget(lbl)
        self.set_widget(sv)
