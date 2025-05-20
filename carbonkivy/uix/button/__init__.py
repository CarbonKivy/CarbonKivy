import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .button import (
    CButton,
    CButtonDanger,
    CButtonGhost,
    CButtonIcon,
    CButtonLabel,
    CButtonPrimary,
    CButtonSecondary,
    CButtonTertiary,
)

filename = os.path.join(UIX, "button", "button.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
