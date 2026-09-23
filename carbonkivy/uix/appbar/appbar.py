from __future__ import annotations

__all__ = ('CAppBar',)

from kivy.metrics import dp, sp
from kivy.properties import ListProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from carbonkivy.uix.icon import CBaseIcon


class _CAppBarIconBtn(ButtonBehavior, CBaseIcon):
    pass


class CAppBar(BoxLayout):
    left_icon = StringProperty('')
    title = StringProperty('')
    right_icons = ListProperty([])

    __events__ = ('on_left_action', 'on_right_action')

    def on_left_action(self): pass
    def on_right_action(self, icon_name): pass

    def on_kv_post(self, base_widget):
        self._build()
        self.bind(left_icon=self._build, title=self._build, right_icons=self._build)

    def _build(self, *_):
        from kivy.uix.label import Label
        self.clear_widgets()

        if self.left_icon:
            btn = _CAppBarIconBtn(icon=self.left_icon)
            btn.size_hint_x = None
            btn.width = dp(44)
            btn.font_size = sp(20)
            btn.bind(on_release=lambda *a: self.dispatch('on_left_action'))
            self.add_widget(btn)

        lbl = Label(
            text=self.title,
            halign='left',
            valign='middle',
            font_size=sp(18),
            bold=True,
        )
        lbl.bind(size=lbl.setter('text_size'))
        self.add_widget(lbl)

        for icon_name in self.right_icons:
            btn = _CAppBarIconBtn(icon=icon_name)
            btn.size_hint_x = None
            btn.width = dp(44)
            btn.font_size = sp(20)
            name = icon_name
            btn.bind(on_release=lambda *a, n=name: self.dispatch('on_right_action', n))
            self.add_widget(btn)
