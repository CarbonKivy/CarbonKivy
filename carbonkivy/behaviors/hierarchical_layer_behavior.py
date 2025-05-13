from __future__ import annotations

__all__ = ("HierarchicalLayerBehavior",)

import asyncgui

from kivy.properties import OptionProperty

class HierarchicalLayerBehavior:

    layer_code = OptionProperty(1, options=[1, 2])

    def __init__(self) -> None:
        super(HierarchicalLayerBehavior, self).__init__()

    def on_parent(self, *args) -> None:
        asyncgui.start(self.set_layer_code())

    async def set_layer_code(self, *args) -> None:
        if isinstance(self.parent, HierarchicalLayerBehavior):
            self.layer_code = 1 if (self.parent.layer_code == 2) else 2
        else:
            self.layer_code = 1