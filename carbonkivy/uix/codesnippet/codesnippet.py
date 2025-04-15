from __future__ import annotations

__all__ = ("CodeSnippet",)

from pygments import styles
from pygments import lexers

from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.metrics import sp
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.codeinput import CodeInput

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
    HoverBehavior,
)
from carbonkivy.utils import get_font_name, get_font_style


class CodeSnippetInput(CodeInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_style_name(self, *args) -> None:
        super().on_style_name(*args)
        self.background_color = [1, 1, 1, 0]
        self.font_name = get_font_name("IBM Plex Mono", "SemiBold")
        self.line_height = get_font_style("code_02")["line_height"]


class CodeSnippet(
    AdaptiveBehavior,
    BackgroundColorBehavior,
    DeclarativeBehavior,
    RelativeLayout,
):
    """
    CodeSnippet class.

    For more information, see in the
    :class:`~carbonkivy.behaviors.declarative_behavior.DeclarativeBehavior`,
    :class:`~carbonkivy.behaviors.adaptive_behavior.AdaptiveBehavior`,
    :class:`~carbonkivy.behaviors.background_color_behavior.BackgroundColorBehavior`,
    :class:`~kivy.uix.relativelayout.RelativeLayout` and
    :class:`~kivy.uix.codeinput.CodeInput`
    classes documentation.
    """

    text = StringProperty()
    """
    Text of the CodeSnippet.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty(sp(16))
    """
    Font size of the text of the CodeSnippet.

    :attr:`font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `''`.
    """

    lexer = ObjectProperty(lexers.Python3Lexer())
    """
    This holds the selected Lexer used by pygments to highlight the code.


    :attr:`lexer` is an :class:`~kivy.properties.ObjectProperty` and
    defaults to `PythonLexer`.
    """

    style_name = OptionProperty("colorful", options=list(styles.get_all_styles()))
    """
    Name of the pygments style to use for formatting.

    :attr:`style_name` is an :class:`~kivy.properties.OptionProperty`
    and defaults to ``'default'``.
    """

    style = ObjectProperty(None)
    """
    The pygments style object to use for formatting.

    When ``style_name`` is set, this will be changed to the
    corresponding style object.

    :attr:`style` is a :class:`~kivy.properties.ObjectProperty` and
    defaults to ``None``
    """

    icon_color = ColorProperty()
    """
    Color of the copy button icon to use.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``None``.
    """

    icon_color_hover = ColorProperty()
    """
    Hover state color of the copy button icon to use.

    :attr:`icon_color_hover` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 0]`.
    """

    icon_color_active = ColorProperty()
    """
    Active state color of the copy button icon to use.

    :attr:`icon_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 0]`.
    """

    icon_bg_color = ColorProperty([1, 1, 1, 0])
    """
    Background Color of the copy button to use.

    :attr:`icon_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``[1, 1, 1, 0]``.
    """

    icon_bg_color_active = ColorProperty(None, allownone=True)
    """
    Active Background Color of the copy button to use.

    :attr:`icon_bg_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``None``.
    """

    _icon_bg_color_active = ColorProperty()

    def __init__(self, *args, **kwargs):
        super(CodeSnippet, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.set_colors, 1)

    def set_colors(self, *args) -> None:
        self._bg_color = self.bg_color
        self._line_color = self.line_color
        self._inset_color = self.inset_color

    def on_style(self, *args) -> None:
        def set_color(*args):
            self.ids.codesnippet_input.background_color = [1, 1, 1, 0]

        Clock.schedule_once(set_color, 2)

    def on_copy(self, text: str = "", *args) -> None:
        """
        Fired when the copy button is pressed.

        For more information, see in the
        :class:`~kivy.clipboard.Clipboard`
        class documentation.
        """
        def select(*args) -> None:
            self.ids.codesnippet_input.select_all()
        Clock.schedule_once(select, 0.5)
        Clipboard.copy(text)
