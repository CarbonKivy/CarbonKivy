import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .radio import (
    CRadioButton,
    CRadioButtonLabel,
    CRadioGroup,
    CRadioGroupHelperText,
    CRadioGroupLabel,
    CRadioGroupLayout,
    CRadioItem,
    CRadioItemLabelNeutral,
)

filename = os.path.join(UIX, "radio", "radio.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
