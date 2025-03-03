from kivy.core.window import Window
from kivy.properties import ColorProperty, BooleanProperty

from carbonkivy.utils import DEVICE_TYPE


class HoverBehavior:

    hover = BooleanProperty(False)

    hover_color = ColorProperty([0, 0, 0, 0.1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEVICE_TYPE != "mobile":
            Window.bind(mouse_pos=self.element_hover)

    def element_hover(self, instance: object, pos: list, *args) -> None:
        self.hover = self.collide_point(pos[0], pos[1])
