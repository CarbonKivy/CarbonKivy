from kivy.app import App

from carbonkivy.theme import CarbonTheme


class CarbonApp(App, CarbonTheme):
    def __init__(self, **kwargs):
        super(CarbonApp, self).__init__(**kwargs)
