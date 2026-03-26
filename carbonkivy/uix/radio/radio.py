from __future__ import annotations

__all__ = (
    "CRadioButton",
    "CRadioButtonLabel",
    "CRadioGroup",
    "CRadioGroupHelperText",
    "CRadioGroupLabel",
    "CRadioGroupLayout",
    "CRadioItem",
    "CRadioItemLabelNeutral",
)

from kivy.input.providers.mouse import MouseMotionEvent
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from carbonkivy.behaviors import SelectableBehavior, StateFocusBehavior
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.icon import CIconCircular
from carbonkivy.uix.label import CLabel, CLabelNeutral
from carbonkivy.uix.selectionlayout import CSelectionLayout


class CRadioButton(
    CIconCircular,
    StateFocusBehavior,
    ButtonBehavior,
    SelectableBehavior,
):
    """
    CRadioButton is a custom checkbox widget that inherits from AdaptiveBehavior,
    CIconCircular, BackgroundColorBehaviorCircular, StateFocusBehavior and ButtonBehavior.
    """

    active = BooleanProperty(False)

    group_master = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(CRadioButton, self).__init__(**kwargs)

    def on_group_master(self, *args):
        self.group_master.selection_items.append(self)
        self.bind(selected=self.group_master.update_selection)

    def on_touch_down(self, touch: MouseMotionEvent) -> bool:
        if self.collide_point(*touch.pos):
            self.selected = not self.selected
        return super().on_touch_down(touch)


class CRadioItem(CBoxLayout):

    def __init__(self, *args, **kwargs):
        super(CRadioItem, self).__init__(*args, **kwargs)


class CRadioButtonLabel(CLabel):
    pass


class CRadioItemLabelNeutral(CLabelNeutral):
    pass


class CRadioGroupHelperText(CLabel):
    pass


class CRadioGroupLabel(CLabel):
    pass


class CRadioGroup(CSelectionLayout):

    def __init__(self, **kwargs):
        super(CRadioGroup, self).__init__(**kwargs)

    def on_parent(self, *args) -> None:
        if self.parent:
            self.bind(size=self.parent.setter("size"))


class CRadioGroupLayout(RelativeLayout):
    pass
