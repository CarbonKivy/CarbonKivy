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
            pos: self.pos
            offset: self.shadow_offset
            blur_radius: self.shadow_blur_radius
"""
)


class ElevationBehavior(EventDispatcher):

    shadow_offset = VariableListProperty([dp(2), -dp(3)], length=2)

    shadow_blur_radius = NumericProperty(dp(0))
