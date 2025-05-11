import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .button import (
    CButton,
    CButtonDanger,
    CButtonGhost,
    CButtonPrimary,
    CButtonSecondary,
    CButtonTertiary,
)

Builder.load_file(os.path.join(UIX, "button", "button.kv"))
