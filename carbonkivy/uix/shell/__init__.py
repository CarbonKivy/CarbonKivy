import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .shell import (
    UIShell,
    UIShellHeader,
    UIShellHeaderName,
    UIShellHeaderMenuButton,
    UIShellLeftPanel,
)

filename = os.path.join(UIX, "shell", "shell.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
