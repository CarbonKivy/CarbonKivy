from kivy.core.window import Window
from kivy.properties import ColorProperty, BooleanProperty

from carbonkivy.utils import DEVICE_TYPE
from carbonkivy.behaviors import BackgroundColorBehavior


class HoverBehavior:

    hover = BooleanProperty(False)

    hover_color = ColorProperty([0, 0, 0, 0.1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEVICE_TYPE != "mobile":
            Window.bind(mouse_pos=self.element_hover)

    def element_hover(self, instance: object, pos: list, *args) -> None:
        if self.cstate != "disabled":
            self.hover = self.collide_point(pos[0], pos[1])

    def on_hover(self, *args) -> None:
        if isinstance(self, BackgroundColorBehavior):
            if self.hover:
                self._bg_color = self.hover_color
                if not self.focus:
                    self._line_color = self.hover_color
                    self.inset_color = self.hover_color
            else:
                self._bg_color = self.bg_color
                if not self.focus:
                    self._line_color = self.bg_color
                    self.inset_color = self.bg_color
