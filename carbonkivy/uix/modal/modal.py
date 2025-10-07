from __future__ import annotations

__all__ = (
    "CModal",
    "CModalLayout",
    "CModalHeader",
    "CModalHeaderLabel",
    "CModalHeaderTitle",
    "CModalBody",
    "CModalBodyContent",
    "CModalFooter",
    "CModalCloseButton",
)

from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget

from carbonkivy.behaviors import AdaptiveBehavior, DeclarativeBehavior
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.shell import UIShellButton
from carbonkivy.uix.stacklayout import CStackLayout


class CModal(AdaptiveBehavior, DeclarativeBehavior, ModalView):

    def __init__(self, **kwargs):
        super(CModal, self).__init__(**kwargs)

    def add_widget(self, widget: Widget, *args, **kwargs):
        if isinstance(widget, CModalLayout) and (not "cmodal_layout" in self.ids):
            self.size_hint_y = None
            self.ids["cmodal_layout"] = widget
            widget.bind(height=self.setter("height"))
        return super().add_widget(widget, *args, **kwargs)


class CModalLayout(CBoxLayout):
    pass


class CModalHeader(CStackLayout):
    pass


class CModalHeaderLabel(CLabel):
    pass


class CModalHeaderTitle(CLabel):
    pass


class CModalBody(CStackLayout):
    pass


class CModalBodyContent(CLabel):
    pass


class CModalFooter(CStackLayout):
    pass


class CModalCloseButton(UIShellButton):
    pass
