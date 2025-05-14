from __future__ import annotations

__all__ = (
    "CTextInput",
    "CTextInputLabel",
    "CTextInputLayout",
    "CTextInputHelperText",
    "CTextInputTrailingIconButton",
)

from kivy.clock import mainthread
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.button import CButtonGhost
from carbonkivy.uix.label import CLabel


class CTextInputHelperText(CLabel):
    pass


class CTextInputLabel(CLabel):
    pass


class CTextInputLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    RelativeLayout,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
):

    ctextinput_area = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(CTextInputLayout, self).__init__(**kwargs)

    def on_kv_post(self, *args):
        self.update_specs()
        return super().on_kv_post(*args)

    @mainthread
    def update_specs(self, *args) -> None:
        if self.ctextinput_area != None:
            self.height = self.ctextinput_area.height
        else:
            Logger.error("CTextInputLayout must contain a single CTextInput widget.")


class CTextInputTrailingIconButton(CButtonGhost):
    pass


class CTextInput(
    AdaptiveBehavior,
    TextInput,
    DeclarativeBehavior,
):

    def __init__(self, **kwargs) -> None:
        super(CTextInput, self).__init__(**kwargs)

    def on_parent(self, *args) -> None:
        if isinstance(self.parent, CTextInputLayout):
            self.parent.ctextinput_area = self
            self.bind(height=self.parent.update_specs)
        else:
            Logger.error("CTextInput must be contained inside CTextInputLayout.")

    def on_password(self, *args) -> None:
        self.cursor = (0, 0)
