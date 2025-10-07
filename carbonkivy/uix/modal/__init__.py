import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .modal import (
    CModal,
    CModalBody,
    CModalBodyContent,
    CModalCloseButton,
    CModalFooter,
    CModalHeader,
    CModalHeaderLabel,
    CModalHeaderTitle,
    CModalLayout,
)

filename = os.path.join(UIX, "modal", "modal.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
