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

Builder.load_file(os.path.join(UIX, "textinput", "textinput.kv"))
