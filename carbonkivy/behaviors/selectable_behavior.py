from __future__ import annotations

__all__ = ("SelectableBehavior",)

from kivy.properties import BooleanProperty


class SelectableBehavior:

    selected = BooleanProperty(False)

    def on_selection(self, *args) -> None:
        return
