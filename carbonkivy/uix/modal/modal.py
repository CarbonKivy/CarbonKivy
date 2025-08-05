from __future__ import annotations

from kivy.clock import Clock, mainthread
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from carbonkivy.behaviors import (
    AdaptiveBehavior,
    DeclarativeBehavior,
    ElevationBehavior,
)
from carbonkivy.uix.button import CButton
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.relativelayout import CRelativeLayout
from carbonkivy.uix.stacklayout import CStackLayout
from carbonkivy.uix.label import CLabel
from carbonkivy.uix.shell import UIShellButton


class CModal(
    AdaptiveBehavior, DeclarativeBehavior, ModalView
):
    pass


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
