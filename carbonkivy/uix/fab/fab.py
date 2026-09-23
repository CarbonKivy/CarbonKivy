from __future__ import annotations

__all__ = ('CFAB',)

from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior

from carbonkivy.uix.icon import CBaseIcon


class CFAB(ButtonBehavior, CBaseIcon):
    icon = StringProperty('add')

    __events__ = ('on_tap',)

    def on_tap(self): pass

    def on_release(self):
        self.dispatch('on_tap')
