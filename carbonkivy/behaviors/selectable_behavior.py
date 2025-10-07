from __future__ import annotations

__all__ = ("SelectableBehavior",)

from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty


class SelectableBehavior(EventDispatcher):

    selected = BooleanProperty(False)

    default = BooleanProperty(False)

    def __init__(self, **kwargs) -> None:
        super(SelectableBehavior, self).__init__(**kwargs)

    def on_default(self, instance: object, value: bool, *args) -> None:
        if value:
            self.selected = True
