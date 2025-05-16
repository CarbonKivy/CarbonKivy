"""
Follows the same declarative pattern as KivyMD's Declarative Behavior.

See more at: `KivyMD's Declarative Behavior Github <https://github.com/kivymd/KivyMD/blob/master/kivymd/uix/behaviors/declarative_behavior.py>`_

Documentation at: https://kivymd.readthedocs.io/en/latest/behaviors/declarative/
"""

from __future__ import annotations

__all__ = ("DeclarativeBehavior",)

from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from carbonkivy.utils import _Dict


# TODO: Add cleaning of the `__ids` collection when removing child widgets
#  from the parent.
class DeclarativeBehavior:
    """
    Implements the creation and addition of child widgets as declarative
    programming style.
    """

    id = StringProperty()
    """
    Widget ID.

    :attr:`id` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    __ids = _Dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """
        Bug Fix for updating colors defined in python.
        Author:
            Ansh Dadwal (https://github.com/T-Dynamos)
        """
        for key, value in kwargs.items():
            if (
                value.__class__.__module__ == "kivy.properties"
                and value.__class__.__name__ == "ObservableList"
            ):
                value.obj().bind(
                    **{value.prop.name: lambda *args, k=key: setattr(self, k, args[-1])}
                )

        for child in args:
            if issubclass(child.__class__, Widget):
                self.add_widget(child)
                if hasattr(child, "id") and child.id:
                    self.__ids[child.id] = child

    def get_ids(self) -> dict:
        """
        Returns a dictionary of widget IDs defined in Python
        code that is written in a declarative style.
        """

        return self.__ids
