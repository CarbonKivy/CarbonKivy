from __future__ import annotations

__all__ = ("HierarchicalLayerBehavior",)

from kivy.clock import mainthread
from kivy.properties import OptionProperty


class HierarchicalLayerBehavior:

    layer_code = OptionProperty(1, options=[1, 2])

    def __init__(self, *args, **kwargs) -> None:
        super(HierarchicalLayerBehavior, self).__init__(*args, **kwargs)

    def on_parent(self, *args) -> None:
        self.set_layer_code()

    @mainthread
    def set_layer_code(self, *args) -> None:
        if isinstance(self.parent, HierarchicalLayerBehavior):
            self.layer_code = 1 if (self.parent.layer_code == 2) else 2
        else:
            self.layer_code = 1
