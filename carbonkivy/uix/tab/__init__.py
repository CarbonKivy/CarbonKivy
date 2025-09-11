import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .tab import (
    CTab,
    CTabHeader,
    CTabHeaderItem,
    CTabHeaderItemLayout,
    CTabHeaderPrimaryText,
    CTabHeaderSecondaryText,
    CTabHeaderIcon,
    CTabLayout,
    CTabManager,
)

filename = os.path.join(UIX, "tab", "tab.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
