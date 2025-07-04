from __future__ import annotations

__all__ = ("TooltipBehavior",)

from kivy.properties import ObjectProperty

from .hover_behavior import HoverBehavior


class TooltipBehavior:

    tooltip = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(TooltipBehavior, self).__init__(**kwargs)

    def on_tooltip(self, *args) -> None:
        if hasattr(self.tooltip, "set_visibility") and hasattr(
            self.tooltip.set_visibility, "__call__"
        ):
            if isinstance(self, HoverBehavior):
                self.bind(hover=self.tooltip.set_visibility)
        else:
            self.unbind(hover=self.tooltip.set_visibility)
