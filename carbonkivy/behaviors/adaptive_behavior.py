from __future__ import annotations

__all__ = ("AdaptiveBehavior",)

from kivy.properties import VariableListProperty


class AdaptiveBehavior:

    adaptive = VariableListProperty([False, False], max_length=2)

    def on_adaptive(self, *args) -> None:
        if self.adaptive[0]:
            self.size_hint_x = None
            self.width = self.minimum_width
        if self.adaptive[1]:
            self.size_hint_y = None
            self.height = self.minimum_width
