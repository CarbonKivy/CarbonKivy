import os

from kivy.lang import Builder

from .textinput import (
    CTextInput,
    CTextInputLabel,
    CTextInputHelperText,
    CTextInputTrailingIconButton,
)
from carbonkivy.config import UIX

Builder.load_file(os.path.join(UIX, "textinput", "textinput.kv"))
