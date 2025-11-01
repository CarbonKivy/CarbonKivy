from __future__ import annotations

__all__ = ("ElevationBehavior",)

from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, VariableListProperty

Builder.load_string(
    """
<ElevationBehavior>:
    canvas.before:
        Color:
            rgba: app.notification_action_tertiary_inverse_hover
        BoxShadow:
            size: self.size
            pos: (self.pos[0] + self.shadow_offset[0], self.pos[1] + self.shadow_offset[1]) if not isinstance(self, RelativeLayout) else (self.shadow_offset[0], self.shadow_offset[1])
            offset: self.shadow_offset
            blur_radius: self.shadow_blur_radius
"""
)


class ElevationBehavior(EventDispatcher):

    shadow_offset = VariableListProperty([dp(1), -dp(1.5)], length=2)

    shadow_blur_radius = NumericProperty(0)

    def __init__(self, **kwargs) -> None:
        super(ElevationBehavior, self).__init__(**kwargs)
