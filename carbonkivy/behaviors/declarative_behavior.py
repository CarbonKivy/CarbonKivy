# Follows the same declarative pattern as KivyMD's Declarative Behavior.
# See more at: https://github.com/kivymd/KivyMD/blob/master/kivymd/uix/behaviors/declarative_behavior.py
# Documentation at: https://kivymd.readthedocs.io/en/latest/behaviors/declarative/

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
        super().__init__(**kwargs)

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
