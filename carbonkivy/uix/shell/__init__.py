import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .shell import (
    UIShell,
    UIShellButton,
    UIShellHeader,
    UIShellHeaderMenuButton,
    UIShellHeaderName,
    UIShellLayout,
    UIShellLeftPanel,
    UIShellPanelLayout,
    UIShellPanelSelectionItem,
    UIShellPanelSelectionLayout,
    UIShellRightPanel,
)

filename = os.path.join(UIX, "shell", "shell.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
