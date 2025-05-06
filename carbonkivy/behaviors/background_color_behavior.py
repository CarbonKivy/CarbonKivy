from __future__ import annotations

__all__ = ("BackgroundColorBehavior",)

from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.metrics import dp

Builder.load_string(
    """
#:import RelativeLayout kivy.uix.relativelayout.RelativeLayout

<BackgroundColorBehaviorRectangular>:

    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            group: "backgroundcolor-behavior-inset-color"
            rgba: self._inset_color
        SmoothRectangle:
            group: "Background_inset_instruction"
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
        Color:
            group: "backgroundcolor-behavior-bg-color"
            rgba: self._bg_color
        SmoothRectangle:
            group: "Background_instruction"
            size: [self.size[0] - self.inset_width, self.size[1] - self.inset_width]
            pos: (self.pos[0] + self.inset_width/2, self.pos[1] + self.inset_width/2) if not isinstance(self, RelativeLayout) else (self.inset_width/2, self.inset_width/2)
            source: self.bg_source
        Color:
            rgba: self._line_color
        SmoothLine:
            width: root.line_width
            rectangle:
                [ \
                0,
                0, \
                self.width, \
                self.height, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x,
                self.y, \
                self.width, \
                self.height, \
                ]
        PopMatrix

<BackgroundColorBehaviorCircular>:

    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            group: "backgroundcolor-behavior-inset-color"
            rgba: self._inset_color
        SmoothRoundedRectangle:
            group: "Background_inset_instruction"
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            radius: self.radius if self.radius else [0, 0, 0, 0]
        Color:
            group: "backgroundcolor-behavior-bg-color"
            rgba: self._bg_color
        SmoothRoundedRectangle:
            group: "Background_instruction"
            size: [self.size[0] - self.inset_width, self.size[1] - self.inset_width]
            pos: (self.pos[0] + self.inset_width/2, self.pos[1] + self.inset_width/2) if not isinstance(self, RelativeLayout) else (self.inset_width/2, self.inset_width/2)
            source: self.bg_source
            radius: self.radius if self.radius else [0, 0, 0, 0]
        Color:
            rgba: self._line_color
        SmoothLine:
            width: root.line_width
            rounded_rectangle:
                [ \
                0,
                0, \
                self.width, \
                self.height, \
                *self.radius, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x,
                self.y, \
                self.width, \
                self.height, \
                *self.radius, \
                ]
        PopMatrix
""",
    filename="BackgroundColorBehavior.kv",
)


class BackgroundColorBehavior:

    bg_source = StringProperty(None, allownone=True)
    """
    Background image path.
    """

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.
    """

    bg_color = ColorProperty([1, 1, 1, 0])
    """
    The background color of the widget.
    """

    active_color = ColorProperty([1, 1, 1, 0])
    """
    The background color of the widget if its touch state is down.
    """

    bg_color_disabled = ColorProperty([1, 1, 1, 0])
    """
    The background color of the widget if disabled.
    """

    bg_color_focus = ColorProperty([1, 1, 1, 0])
    """
    The background color of the widget if focused.
    """

    inset_color = ColorProperty([1, 1, 1, 0])
    """
    The color of border inset.
    """

    inset_color_disabled = ColorProperty([1, 1, 1, 0])
    """
    The color of border inset if disabled.
    """

    inset_color_focus = ColorProperty([1, 1, 1, 0])
    """
    The color of border inset if focused.
    """

    line_color = ColorProperty([1, 1, 1, 0])
    """
    The border of the specified color will be used to border the widget.
    """

    line_color_disabled = ColorProperty([1, 1, 1, 0])
    """
    The border of the specified color will be used to border the widget if disabled.
    """

    line_color_focus = ColorProperty([1, 1, 1, 0])
    """
    The border of the specified color will be used to border the widget if focused.
    """

    inset_width = NumericProperty(dp(5))
    """
    The width of border inset.
    """

    line_width = NumericProperty(dp(1.25))
    """
    Border of the specified width will be used to border the widget.
    """

    angle = NumericProperty(0)
    background_origin = ListProperty(None)

    cstate = OptionProperty("normal", options=["active", "disabled", "normal"])

    _bg_color = ColorProperty([1, 1, 1, 0])
    _inset_color = ColorProperty([1, 1, 1, 0])
    _line_color = ColorProperty([1, 1, 1, 0])

    _background_x = NumericProperty(0)
    _background_y = NumericProperty(0)
    _background_origin = ReferenceListProperty(_background_x, _background_y)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_background_origin)

    def on_bg_color(self, instance: object, color: list | str) -> None:
        """Fired when the values of :attr:`bg_color` change."""

        self._bg_color = color

    def on_inset_color(self, instance: object, color: list | str) -> None:
        """Fired when the values of :attr:`inset_color` change."""

        self._inset_color = color

    def on_line_color(self, instance: object, color: list | str) -> None:
        """Fired when the values of :attr:`line_color` change."""

        self._line_color = color

    def on_cstate(self, *args) -> None:
        if self.cstate == "disabled":
            self.disabled = True

    def update_background_origin(self, instance, pos: list) -> None:
        """Fired when the values of :attr:`pos` change."""

        if self.background_origin:
            self._background_origin = self.background_origin
        else:
            self._background_origin = self.center


class BackgroundColorBehaviorRectangular(BackgroundColorBehavior):
    pass


class BackgroundColorBehaviorCircular(BackgroundColorBehavior):

    radius = VariableListProperty([0], length=4)
