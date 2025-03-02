from __future__ import annotations

__all__ = ("BackgroundColorBehavior",)

from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
)

Builder.load_string(
    """
#:import RelativeLayout kivy.uix.relativelayout.RelativeLayout


<BackgroundColorBehavior>
    canvas:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            group: "backgroundcolor-behavior-inset-color"
            rgba: self.inset_color
        SmoothRectangle:
            group: "Background_inset_instruction"
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
        Color:
            group: "backgroundcolor-behavior-bg-color"
            rgba: self.bg_color
        SmoothRectangle:
            group: "Background_instruction"
            size: [self.size[0] - dp(self.inset_width), self.size[1] - dp(self.inset_width)]
            pos: self.pos if not isinstance(self, RelativeLayout) else (dp(self.inset_width/2), dp(self.inset_width/2))
            source: root.bg_source
        Color:
            rgba: self.line_color if self.line_color else (0, 0, 0, 0)
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
""",
    filename="BackgroundColorBehavior.kv",
)


class BackgroundColorBehavior:
    bg_source = StringProperty()
    """
    Background image path.
    """

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.
    """

    bg_color = ColorProperty([0, 0, 0, 0])
    """
    The background color of the widget.
    """

    inset_color = ColorProperty([1, 1, 1, 1])
    """
    The color of border inset.
    """

    line_color = ColorProperty([0, 0, 0, 0])
    """
    The border of the specified color will be used to border the widget.
    """

    inset_width = NumericProperty(4)
    """
    The width of border inset.
    """

    line_width = NumericProperty(1)
    """
    Border of the specified width will be used to border the widget.
    """

    angle = NumericProperty(0)
    background_origin = ListProperty(None)

    _background_x = NumericProperty(0)
    _background_y = NumericProperty(0)
    _background_origin = ReferenceListProperty(_background_x, _background_y)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_background_origin)

    # def on_bg_color(self, instance: object, color: list | str) -> None:
    #     """Fired when the values of :attr:`bg_color` change."""

    #     self.bg_color = color

    def update_background_origin(self, instance, pos: list) -> None:
        """Fired when the values of :attr:`pos` change."""

        if self.background_origin:
            self._background_origin = self.background_origin
        else:
            self._background_origin = self.center
