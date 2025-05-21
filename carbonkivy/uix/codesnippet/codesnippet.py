from __future__ import annotations

__all__ = ("CodeSnippetLayout", "CodeSnippet", "CodeSnippetCopyButton")

from kivy.clock import Clock, mainthread
from kivy.core.clipboard import Clipboard
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.uix.codeinput import CodeInput
from kivy.uix.relativelayout import RelativeLayout
from pygments import lexers

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    DeclarativeBehavior,
    HoverBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.button import CButtonGhost
from carbonkivy.utils import get_font_name, get_font_style


class CodeSnippet(AdaptiveBehavior, CodeInput, DeclarativeBehavior):

    lexer = ObjectProperty(lexers.Python3Lexer())
    """
    This holds the selected Lexer used by pygments to highlight the code.


    :attr:`lexer` is an :class:`~kivy.properties.ObjectProperty` and
    defaults to `PythonLexer`.
    """

    def __init__(self, **kwargs) -> None:
        super(CodeSnippet, self).__init__(**kwargs)

    def on_parent(self, *args) -> None:
        if isinstance(self.parent, CodeSnippetLayout):
            self.parent.codesnippet_area = self
            self.bind(height=self.parent.update_specs)
        else:
            Logger.error("CodeSnippet must be contained inside CodeSnippetLayout.")

    def on_style(self, *args) -> None:
        super().on_style(*args)

        def set_color(*args):
            self.background_color = [1, 1, 1, 0]

        Clock.schedule_once(set_color, 0.5)

    def on_style_name(self, *args) -> None:
        super().on_style_name(*args)
        self.background_color = [1, 1, 1, 0]
        self.font_name = get_font_name("IBM Plex Mono", "SemiBold")
        self.line_height = get_font_style("code_02")["line_height"]


class CodeSnippetLayout(
    AdaptiveBehavior,
    BackgroundColorBehaviorRectangular,
    StateFocusBehavior,
    DeclarativeBehavior,
    HoverBehavior,
    RelativeLayout,
):
    """
    CodeSnippetLayout class.

    For more information, see in the
    :class:`~carbonkivy.behaviors.adaptive_behavior.AdaptiveBehavior`,
    :class:`~carbonkivy.behaviors.background_color_behavior.BackgroundColorBehaviorRectangular`,
    :class:`~carbonkivy.behaviors.declarative_behavior.DeclarativeBehavior`,
    :class:`~carbonkivy.behaviors.hover_behavior.HoverBehavior`,
    :class:`~kivy.uix.relativelayout.RelativeLayout` and
    :class:`~carbonkivy.behaviors.state_focus_behavior.StateFocusBehavior`
    classes documentation.
    """

    codesnippet_area = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CodeSnippetLayout, self).__init__(**kwargs)
        Clock.schedule_once(self.set_colors, 1)

    def set_colors(self, *args) -> None:
        self._bg_color = self.bg_color
        self._line_color = self.line_color
        self._inset_color = self.inset_color

    def on_copy(self, text: str = "", *args) -> None:
        """
        Fired when the copy button is pressed.

        For more information, see in the
        :class:`~kivy.clipboard.Clipboard`
        class documentation.
        """

        def select(*args) -> None:
            self.codesnippet_area.select_all()
            Clock.schedule_once(lambda x: self.codesnippet_area.cancel_selection(), 2)
            self.codesnippet_area.focus = False

        Clock.schedule_once(select, 0.5)
        Clipboard.copy(text)

    def on_kv_post(self, *args):
        self.update_specs()
        return super().on_kv_post(*args)

    @mainthread
    def update_specs(self, *args) -> None:
        if self.codesnippet_area != None:
            self.height = self.codesnippet_area.height
        else:
            Logger.error("CodeSnippetLayout must contain a single CodeSnippet widget.")


class CodeSnippetCopyButton(CButtonGhost):
    pass
