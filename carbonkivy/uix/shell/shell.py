from __future__ import annotations

__all__ = ("UIShell", "UIShellHeader", "UIShellHeaderName", "UIShellHeaderMenuButton",)

from kivy.animation import Animation
from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.properties import BooleanProperty, ColorProperty, ObjectProperty

from carbonkivy.behaviors import (
    StateFocusBehavior,
)
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.relativelayout import CRelativeLayout
from carbonkivy.uix.stacklayout import CStackLayout
from carbonkivy.uix.button import CButtonGhost


class UIShell(CStackLayout):
    pass


class UIShellHeader(CBoxLayout):
    pass


class UIShellHeaderName(
    CLabel,
    StateFocusBehavior,
):
    pass


class UIShellHeaderButton(CButtonGhost):

    active = BooleanProperty(False)


class UIShellHeaderMenuButton(UIShellHeaderButton):
    pass


class UIShellLeftPanel(CRelativeLayout):

    overlay = ColorProperty([1, 1, 1, 0])

    visibility = BooleanProperty(None, allownone=True)

    panel_shell = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(UIShellLeftPanel, self).__init__(**kwargs)

    def on_visibility(self, *args) -> None:

        def set_visibility(*args) -> None:
            if self.visibility:
                self.opacity = 1
                Animation(x = 0, d=0.25).start(self)
                try:
                    self.panel_shell.bg_color = self.overlay
                except:
                    return
            else:
                (Animation(x = 0 - self.width, d=0.25) +
                Animation(opacity = 0, d=0.25)).start(self)
                try:
                    self.panel_shell.bg_color = [1, 1, 1, 0]
                except:
                    return

        Clock.schedule_once(set_visibility)


class UIShellRightPanel(CRelativeLayout):

    overlay = ColorProperty([1, 1, 1, 0])

    visibility = BooleanProperty(None, allownone=True)

    panel_shell = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(UIShellRightPanel, self).__init__(**kwargs)
        Window.bind(size=self.on_visibility)

    def on_visibility(self, *args) -> None:

        def set_visibility(*args) -> None:
            if self.visibility:
                self.opacity = 1
                Animation(x = Window.width - self.width, d=0.25).start(self)
            else:
                (Animation(x = Window.width, d=0.25) +
                Animation(opacity = 0, d=0.25)).start(self)

        Clock.schedule_once(set_visibility)


class UIShellPanelLayout(CStackLayout):
    pass
