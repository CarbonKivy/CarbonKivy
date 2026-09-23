from __future__ import annotations

__all__ = ('CSearchBar',)

from kivy.metrics import dp, sp
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.uix.icon import CBaseIcon


class CSearchBarClearBtn(ButtonBehavior, CBaseIcon):
    pass


class CSearchBar(BoxLayout):
    search_text = StringProperty('')

    def on_kv_post(self, base_widget):
        self._clear_btn = CSearchBarClearBtn(
            icon='close',
            font_size=sp(18),
            size_hint_x=None,
            width=0,
            opacity=0,
        )
        self._clear_btn.halign = 'center'
        self._clear_btn.valign = 'middle'
        self._clear_btn.bind(on_release=self._clear)
        self.add_widget(self._clear_btn)

    def _on_text_change(self, text):
        self.search_text = text
        has_text = bool(text)
        self._clear_btn.width = dp(36) if has_text else 0
        self._clear_btn.opacity = 1 if has_text else 0

    def _clear(self, *_):
        self.ids.text_input.text = ''
