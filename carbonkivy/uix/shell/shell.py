from __future__ import annotations

__all__ = ("UIShell", "UIShellHeader", "UIShellHeaderName", "UIShellHeaderMenuButton",)

from kivy.animation import Animation
from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.properties import BooleanProperty, ColorProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.relativelayout import CRelativeLayout
from carbonkivy.uix.stacklayout import CStackLayout
from carbonkivy.uix.button import CButtonGhost

class UIShell(CStackLayout):
    pass


class UIShellHeader(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    BoxLayout,
    DeclarativeBehavior,
):
    pass


class UIShellHeaderName(
    CLabel,
    StateFocusBehavior,
):
    pass


class UIShellHeaderMenuButton(CButtonGhost):

    active = BooleanProperty(False)


class UIShellLeftPanel(CRelativeLayout):

    overlay = ColorProperty([1, 1, 1, 0])

    visibility = BooleanProperty(None, allownone=True)

    panel_shell = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(UIShellLeftPanel, self).__init__(**kwargs)

    @mainthread
    def on_visibility(self, *args) -> None:
        if self.visibility:
            self.pos = [0, 0]
            self.panel_shell.bg_color = self.overlay
        else:
            self.pos = [0 - self.width, 0]
            self.panel_shell.bg_color = [1, 1, 1, 0]
