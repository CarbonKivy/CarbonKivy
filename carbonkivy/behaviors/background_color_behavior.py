from __future__ import annotations

__all__ = (
    "BackgroundColorBehavior",
    "BackgroundColorBehaviorCircular",
    "BackgroundColorBehaviorRectangular",
)

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
)

Builder.load_string(
    """
#:import RelativeLayout kivy.uix.relativelayout.RelativeLayout

<BackgroundColorBehaviorRectangular>:

    canvas:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            group: "backgroundcolor-behavior-bg-color"
            rgba: self._bg_color if not self.bg_source else [1, 1, 1, 1]
        Rectangle:
            group: "Background_instruction"
            size: [self.size[0], self.size[1]]
            pos: (self.pos[0], self.pos[1]) if not isinstance(self, RelativeLayout) else (0, 0)
            source: self.bg_source
    canvas.after:
        Color:
            rgba: self._inset_color
        Line:
            width: max(dp(0.5), self.inset_width)
            cap: "square"
            joint: "miter"
            rectangle:
                [ \
                self.inset_width/2,
                self.inset_width/2, \
                self.width - self.inset_width, \
                self.height - self.inset_width, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x + self.inset_width/2,
                self.y + self.inset_width/2, \
                self.width - self.inset_width, \
                self.height - self.inset_width, \
                ]
        Color:
            rgba: self._line_color
        Line:
            width: self.line_width
            cap: "square"
            joint: "miter"
            rectangle:
                [ \
                self.line_width/2,
                self.line_width/2, \
                self.width - self.line_width, \
                self.height - self.line_width, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x + self.line_width/2,
                self.y + self.line_width/2, \
                self.width - self.line_width, \
                self.height - self.line_width, \
                ]
        PopMatrix

<BackgroundColorBehaviorCircular>:
    canvas:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            group: "backgroundcolor-behavior-bg-color"
            rgba: self._bg_color if not self.bg_source else [1, 1, 1, 1]
        SmoothRoundedRectangle:
            group: "Background_instruction"
            size: [self.size[0], self.size[1]]
            pos: (self.x, self.y) if not isinstance(self, RelativeLayout) else (0, 0)
            source: self.bg_source
            radius: self.radius if self.radius else [0, 0, 0, 0]
    canvas.after:        
        Color:
            rgba: self._inset_color
        Line:
            width: max(dp(0.5), self.inset_width)
            cap: "square"
            joint: "round"
            rounded_rectangle:
                [ \
                self.inset_width/2,
                self.inset_width/2, \
                self.width - self.inset_width, \
                self.height - self.inset_width, \
                *self.radius, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x + self.inset_width/2,
                self.y + self.inset_width/2, \
                self.width - self.inset_width, \
                self.height - self.inset_width, \
                *self.radius, \
                ]
        Color:
            rgba: self._line_color
        Line:
            width: self.line_width
            cap: "square"
            joint: "round"
            rounded_rectangle:
                [ \
                self.line_width/2,
                self.line_width/2, \
                self.width - self.line_width, \
                self.height - self.line_width, \
                *self.radius, \
                ] \
                if isinstance(self, RelativeLayout) else \
                [ \
                self.x + self.line_width/2,
                self.y + self.line_width/2, \
                self.width - self.line_width, \
                self.height - self.line_width, \
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

    inset_width = NumericProperty(dp(2))
    """
    The width of border inset.
    """

    line_width = NumericProperty(dp(1))
    """
    Border of the specified width will be used to border the widget.
    """

    angle = NumericProperty(0)
    background_origin = ListProperty(None)

    cstate = OptionProperty("normal", options=["active", "disabled", "normal"])

    _cstate = StringProperty("normal")
    _bg_color = ColorProperty([1, 1, 1, 0])
    _inset_color = ColorProperty([1, 1, 1, 0])
    _line_color = ColorProperty([1, 1, 1, 0])

    _background_x = NumericProperty(0)
    _background_y = NumericProperty(0)
    _background_origin = ReferenceListProperty(_background_x, _background_y)

    def __init__(self, *args, **kwargs) -> None:
        super(BackgroundColorBehavior, self).__init__(**kwargs)
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
        else:
            self._cstate = self.cstate
            self.disabled = False
            for items in self.children:
                items.disabled = False

    def on_disabled(self, *args) -> None:
        if self.disabled == True:
            self.cstate = "disabled"
        else:
            self.cstate = self._cstate

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
