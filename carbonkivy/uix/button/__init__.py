import os

from kivy.lang import Builder

from .button import (
    CButton,
    CButtonDanger,
    CButtonGhost,
    CButtonPrimary,
    CButtonSecondary,
    CButtonTertiary,
)
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "button", "button.kv"))
