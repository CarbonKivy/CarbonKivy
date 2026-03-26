from __future__ import annotations

__all__ = ("CSelectionLayout",)

from carbonkivy.behaviors import SelectionBehavior
from carbonkivy.uix.boxlayout import CBoxLayout


class CSelectionLayout(SelectionBehavior, CBoxLayout):
    pass
