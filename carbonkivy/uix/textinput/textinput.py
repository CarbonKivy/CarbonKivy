from __future__ import annotations

__all__ = (
    "CTextInput",
    "CTextInputLabel",
    "CTextInputLayout",
    "CTextInputLayoutBase",
    "CTextInputLayoutCircular",
    "CTextInputHelperText",
    "CTextInputTrailingIconButton",
)

from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.properties import ObjectProperty, ColorProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    BackgroundColorBehaviorCircular,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.button import CButtonCircular
from carbonkivy.uix.label import CLabel


class CTextInputHelperText(CLabel):
    pass


class CTextInputLabel(CLabel):
    pass


class CTextInputLayoutBase(
    AdaptiveBehavior,
    StateFocusBehavior,
    RelativeLayout,
    DeclarativeBehavior,
    HierarchicalLayerBehavior,
    HoverBehavior,
):

    ctextinput_area = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(CTextInputLayoutBase, self).__init__(**kwargs)

    def on_kv_post(self, *args):
        self.update_specs()
        return super().on_kv_post(*args)

    @mainthread
    def update_specs(self, *args) -> None:
        if self.ctextinput_area != None:
            self.height = self.ctextinput_area.height
        else:
            Logger.warning("CTextInputLayout must contain a single CTextInput widget.")

    def on_hover(self, *args) -> None:
        super(CTextInputLayoutBase, self).on_hover(*args)
        if self.hover:
            Window.set_system_cursor('ibeam')
        else:
            Window.set_system_cursor('arrow')


class CTextInputLayout(
    BackgroundColorBehaviorRectangular,
    CTextInputLayoutBase,
):
    pass


class CTextInputLayoutCircular(
    BackgroundColorBehaviorCircular,
    CTextInputLayoutBase,
):
    pass


class CTextInputTrailingIconButton(CButtonCircular):
    pass


class CTextInput(
    AdaptiveBehavior,
    TextInput,
    DeclarativeBehavior,
):

    baseline_color = ColorProperty()

    def __init__(self, **kwargs) -> None:
        super(CTextInput, self).__init__(**kwargs)

    def on_parent(self, *args) -> None:
        if isinstance(self.parent, CTextInputLayoutBase):
            self.parent.ctextinput_area = self
            self.bind(height=self.parent.update_specs)
        else:
            Logger.warning("CTextInput must be contained inside CTextInputLayoutBase.")

    def on_password(self, *args) -> None:
        self.cursor = (0, 0)
