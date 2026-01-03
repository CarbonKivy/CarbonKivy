from __future__ import annotations

__all__ = ("SelectionBehavior",)

from kivy.event import EventDispatcher
from kivy.properties import DictProperty, OptionProperty, StringProperty


class SelectionBehavior(EventDispatcher):

    selected_items = DictProperty()

    selection_attr = StringProperty("selected")

    selection_type = OptionProperty("Single", options=["Multiple", "Single"])

    def __init__(self, **kwargs) -> None:
        super(SelectionBehavior, self).__init__(**kwargs)

    def add_widget(self, widget, *args, **kwargs):
        if hasattr(widget, self.selection_attr):
            widget.bind(**{self.selection_attr: self.update_selection})
        return super().add_widget(widget, *args, **kwargs)

    def update_selection(self, instance: object, value: bool, *args) -> None:
        if self.selection_type == "Single":
            selected_items = {}
            if value:
                for items in self.children:
                    if (
                        items != instance
                        and hasattr(items, self.selection_attr)
                        and getattr(items, self.selection_attr, False)
                    ):
                        setattr(items, self.selection_attr, False)

                selected_items[instance] = value
                self.selected_items = selected_items
            else:
                if all(
                    not getattr(items, self.selection_attr, False)
                    for items in self.children
                    if hasattr(items, self.selection_attr)
                ):
                    setattr(instance, self.selection_attr, True)
                    self.selected_items = {instance: True}
        elif self.selection_type == "Multiple":
            new_dict = dict(self.selected_items)
            if value:
                new_dict[instance] = True
            else:
                new_dict.pop(instance, None)
            self.selected_items = new_dict
