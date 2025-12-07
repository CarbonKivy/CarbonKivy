from __future__ import annotations

__all__ = (
    "UIShell",
    "UIShellButton",
    "UIShellHeader",
    "UIShellHeaderMenuButton",
    "UIShellHeaderName",
    "UIShellLayout",
    "UIShellLeftPanel",
    "UIShellPanelLayout",
    "UIShellPanelSelectionItem",
    "UIShellPanelSelectionLayout",
    "UIShellRightPanel",
)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from carbonkivy.behaviors import (
    HoverBehavior,
    SelectableBehavior,
    SelectionBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.button import CButtonGhost
from carbonkivy.uix.icon import CIcon
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.relativelayout import CRelativeLayout
from carbonkivy.uix.stacklayout import CStackLayout


class UIShell(CStackLayout):
    pass


class UIShellHeader(CBoxLayout):
    pass


class UIShellHeaderName(
    CLabel,
    StateFocusBehavior,
):
    pass


class UIShellButton(CButtonGhost):

    active = BooleanProperty(False)


class UIShellHeaderMenuButton(UIShellButton):
    pass


class UIShellLeftPanel(CRelativeLayout):

    overlay = ColorProperty([1, 1, 1, 0])

    visibility = BooleanProperty(None, allownone=True)

    panel_shell = ObjectProperty(None, allownone=True)

    panel_width = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super(UIShellLeftPanel, self).__init__(**kwargs)
        self.animation = Animation()
        Window.bind(size=self.on_visibility)
        self.pos = (-self.panel_width, 0)

    def on_visibility(self, *args) -> None:
        self.animation.cancel_all(self)

        def set_visibility(*args) -> None:
            if self.visibility:
                self.animation = (
                    Animation(width=self.panel_width, d=0.015)
                    + Animation(opacity=1, d=0.015)
                    + Animation(x=0, d=0.015)
                )
                try:
                    self.panel_shell.bg_color = self.overlay
                except:
                    return
            else:
                self.animation = (
                    Animation(opacity=0, d=0.015)
                    + Animation(width=dp(0), d=0.015)
                    + Animation(x=0 - self.panel_width, d=0.015)
                )
                try:
                    self.panel_shell.bg_color = [1, 1, 1, 0]
                except:
                    return
            self.animation.start(self)

        Clock.schedule_once(set_visibility)


class UIShellRightPanel(CRelativeLayout):

    overlay = ColorProperty([1, 1, 1, 0])

    visibility = BooleanProperty(None, allownone=True)

    panel_shell = ObjectProperty(None, allownone=True)

    panel_width = NumericProperty()

    def __init__(self, **kwargs) -> None:
        super(UIShellRightPanel, self).__init__(**kwargs)
        self.animation = Animation()
        Window.bind(size=self.on_visibility)

    def on_visibility(self, *args) -> None:
        self.animation.cancel_all(self)

        def set_visibility(*args) -> None:
            if self.visibility:
                self.opacity = 1
                self.animation = Animation(x=Window.width - self.panel_width, d=0.05)
            else:
                self.animation = Animation(x=Window.width, d=0.05) + Animation(
                    opacity=0, d=0.05
                )
            self.animation.start(self)

        Clock.schedule_once(set_visibility)


class UIShellLayout(CStackLayout):
    pass


class UIShellPanelLayout(UIShellLayout):
    pass


class UIShellPanelSelectionLayout(SelectionBehavior, CBoxLayout):
    pass


class UIShellPanelSelectionItem(
    ButtonBehavior, CBoxLayout, StateFocusBehavior, HoverBehavior, SelectableBehavior
):

    text = StringProperty()

    left_icon = StringProperty("blank")

    right_icon = StringProperty("blank")

    def __init__(self, **kwargs) -> None:
        super(UIShellPanelSelectionItem, self).__init__(**kwargs)

    def on_touch_down(self, touch: MouseMotionEvent) -> bool:
        if self.collide_point(*touch.pos):
            self.selected = True
        return super().on_touch_down(touch)

    def on_left_icon(self, *args) -> None:
        try:
            self.ids.left_icon.icon = self.left_icon
        except:
            pass

        def add_left_icon(*args) -> None:
            self.add_widget(
                CIcon(
                    id="left_icon",
                    icon=self.left_icon,
                    font_size=sp(16),
                    pos_hint={"center_y": 0.5},
                ),
                index=2,
            )

        if not "left_icon" in self.ids:
            Clock.schedule_once(add_left_icon)

    def on_text(self, *args) -> None:
        try:
            self.ids.label.text = self.text
        except:
            pass

        def add_text(*args) -> None:
            self.add_widget(
                CLabel(
                    id="label",
                    text=self.text,
                    style="label_02",
                    font_size=sp(16),
                    pos_hint={"center_y": 0.5},
                ),
                index=1,
            )

        if not "label" in self.ids:
            Clock.schedule_once(add_text)

    def on_right_icon(self, *args) -> None:
        try:
            self.ids.right_icon.icon = self.right_icon
        except:
            pass

        def add_right_icon(*args) -> None:
            self.add_widget(
                CIcon(
                    id="right_icon",
                    icon=self.right_icon,
                    font_size=sp(16),
                    pos_hint={"center_y": 0.5},
                ),
                index=0,
            )

        if not "right_icon" in self.ids:
            Clock.schedule_once(add_right_icon)
