import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .textinput import (
    CTextInput,
    CTextInputHelperText,
    CTextInputLabel,
    CTextInputLayout,
    CTextInputTrailingIconButton,
)

filename = os.path.join(UIX, "textinput", "textinput.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
