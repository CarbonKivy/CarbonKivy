from __future__ import annotations

__all__ = ("CToggle",)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ListProperty, VariableListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import (
    BackgroundColorBehaviorCircular,
    StateFocusBehavior,
    DeclarativeBehavior,
)


class CToggle(
    BackgroundColorBehaviorCircular,
    StateFocusBehavior,
    ButtonBehavior,
    DeclarativeBehavior,
    RelativeLayout,
):

    active = BooleanProperty(False)

    handle_size = VariableListProperty([dp(64), dp(64)], length=2)

    handle_pos = ListProperty()

    def __init__(self, **kwargs) -> None:
        self.handle_pos = (0, 0)
        super(CToggle, self).__init__(**kwargs)
        self.animation = None

    def on_pos(self, *args) -> None:
        self.handle_pos = (
            (
                self.pos[0] + dp(8)
                if not self.active
                else self.pos[0] + self.width - self.handle_size[0] - dp(8)
            ),
            self.pos[1] + self.height / 2 - self.handle_size[1] / 2,
        )

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)

    def on_active(self, *args) -> None:
        if self.animation:
            self.animation.cancel_all(self)
        if self.active:
            self.animation = Animation(
                handle_pos=[
                    self.pos[0] + self.width - self.handle_size[0] - dp(8),
                    self.pos[1] + self.height / 2 - self.handle_size[1] / 2,
                ],
                d=0.095,
            )
        else:
            self.animation = Animation(
                handle_pos=[
                    self.pos[0] + dp(8),
                    self.pos[1] + self.height / 2 - self.handle_size[1] / 2,
                ],
                d=0.095,
            )
        self.animation.start(self)

    def on_touch_down(self, touch: MouseMotionEvent) -> bool | None:
        if self.collide_point(*touch.pos) and self.focus:
            self.active = not self.active
        return super().on_touch_down(touch)
