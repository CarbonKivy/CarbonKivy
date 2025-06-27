from __future__ import annotations

__all__ = ("SelectiveBehavior",)

from kivy.properties import BooleanProperty


class SelectionBehavior:

    selected = BooleanProperty(False)

    def on_selection(self, *args) -> None:
        return
