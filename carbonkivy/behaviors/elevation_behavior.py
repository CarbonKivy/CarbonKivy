from __future__ import annotations

__all__ = ("ElevationBehavior",)

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    VariableListProperty,
)

Builder.load_string(
"""
<ElevationBehavior>:
    canvas.before:
        Color:
            rgba: self.shadow_color
        BoxShadow:
            pos: self.pos
            size: self.size
            offset: self.shadow_offset
            blur_radius: self.shadow_blur_radius
    shadow_color: app.background_inverse_hover
"""
)


class ElevationBehavior:

    shadow_color = ColorProperty()

    shadow_offset = VariableListProperty([1, -1], length=2)

    shadow_blur_radius = NumericProperty(dp(5))
