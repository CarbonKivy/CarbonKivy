from __future__ import annotations

__all__ = (
    "CTab",
    "CTabLayout",
    "CTabManager",
    "CTabHeader",
    "CTabHeaderIcon",
    "CTabHeaderItem",
    "CTabHeaderItemLayout",
    "CTabHeaderPrimaryText",
    "CTabHeaderSecondaryText",
)

from typing import Any

from kivy.clock import Clock
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior

from carbonkivy.behaviors import (
    SelectableBehavior,
    SelectionBehavior,
    StateFocusBehavior,
)
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.gridlayout import CGridLayout
from carbonkivy.uix.icon import CIcon
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.relativelayout.relativelayout import CRelativeLayout
from carbonkivy.uix.screen.screen import CScreen
from carbonkivy.uix.screenmanager import CScreenManager
from carbonkivy.uix.stacklayout import CStackLayout


class CTabLayout(CStackLayout):
    pass


class CTabHeader(SelectionBehavior, CBoxLayout):

    tab_manager = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CTabHeader, self).__init__(**kwargs)

    def on_tab_manager(self, *args) -> None:
        for widgets in self.children:
            widgets.tab_manager = self.tab_manager

    def add_widget(self, widget, *args, **kwargs) -> Any:
        if hasattr(widget, "tab_manager"):
            widget.tab_manager = self.tab_manager
        return super().add_widget(widget, *args, **kwargs)


class CTabHeaderItem(
    ButtonBehavior, CBoxLayout, StateFocusBehavior, SelectableBehavior
):

    primary_text = StringProperty()

    secondary_text = StringProperty()

    icon = StringProperty()

    name_tab = StringProperty()

    tab_manager = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CTabHeaderItem, self).__init__(**kwargs)

    def on_selected(self, *args) -> None:
        if self.selected and self.tab_manager is not None:
            self.tab_manager.current = self.name_tab

    def on_touch_down(self, touch: MouseMotionEvent) -> bool:
        if self.collide_point(*touch.pos):
            self.selected = True
        else:
            self.selected = False
        return super().on_touch_down(touch)

    def on_primary_text(self, *args) -> None:
        try:
            self.ids.primary_text_label.text = self.primary_text
        except:
            pass

        def add_primary_text(*args) -> None:
            plabel = CTabHeaderPrimaryText(text=self.primary_text)
            self.ids.header_box_layout.add_widget(plabel, index=1)
            self.ids["primary_text_label"] = plabel
            self.ids.header_box_layout.width += self.ids.primary_text_label.width

        if not "primary_text_label" in self.ids:
            Clock.schedule_once(add_primary_text)

    # def on_secondary_text(self, *args) -> None:
    #     try:
    #         self.ids.secondary_text_label.text = self.secondary_text
    #     except:
    #         pass

    #     def add_secondary_text(*args) -> None:
    #         self.add_widget(CLabel(id="secondary_text_label", text=self.secondary_text, font_size=sp(16)), index=1)

    #     if not "secondary_text_label" in self.ids:
    #         Clock.schedule_once(add_secondary_text)

    def on_icon(self, *args) -> None:
        try:
            self.ids.icon.icon = self.icon
        except:
            pass

        def add_icon(*args) -> None:
            icon = CTabHeaderIcon(icon=self.icon)
            self.ids.header_box_layout.add_widget(icon, index=0)
            self.ids["icon"] = icon
            self.ids.header_box_layout.width += self.ids.icon.width

        if not "icon" in self.ids:
            Clock.schedule_once(add_icon)


class CTabHeaderItemLayout(CBoxLayout):
    pass


class CTabHeaderPrimaryText(CLabel):
    pass


class CTabHeaderSecondaryText(CLabel):
    pass


class CTabHeaderIcon(CIcon):
    pass


class CTabManager(CScreenManager):
    pass


class CTab(CScreen):
    pass
