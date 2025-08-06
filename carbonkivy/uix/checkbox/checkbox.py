from __future__ import annotations

__all__ = ()

from kivy.input.providers.mouse import MouseMotionEvent
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, ColorProperty

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorCircular,
    DeclarativeBehavior,
    StateFocusBehavior,
    HoverBehavior
)
from carbonkivy.uix.icon import CIconCircular

class CCheckbox(
    CIconCircular,
    StateFocusBehavior, 
    ButtonBehavior,
):
    """
    CCheckbox is a custom checkbox widget that inherits from AdaptiveBehavior,
    DeclarativeBehavior, BackgroundColorBehaviorCircular, StateFocusBehavior, ButtonBehavior, and HoverBehavior.
    """

    active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(CCheckbox, self).__init__(**kwargs)

    def on_touch_down(self, touch: MouseMotionEvent) -> bool:
        if self.collide_point(*touch.pos):
            self.active = not self.active
        return super().on_touch_down(touch)