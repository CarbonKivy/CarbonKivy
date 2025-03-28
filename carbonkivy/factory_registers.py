import os

from kivy.factory import Factory
from kivy.core.text import LabelBase

from carbonkivy.config import DATA

# Alias for the register function from Factory
register = Factory.register

"""
Registers custom components to the Kivy Factory.

This code registers each component within the "uix" directory to the Kivy Factory. 
Once registered, the components can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the component with Kivy's Factory
register("CAnchorLayout", module="carbonkivy.uix.anchorlayout")
register("CBoxLayout", module="carbonkivy.uix.boxlayout")
register("CButton", module="carbonkivy.uix.button")
register("CButtonGhost", module="carbonkivy.uix.button")
register("CButtonPrimary", module="carbonkivy.uix.button")
register("CButtonSecondary", module="carbonkivy.uix.button")
register("CDivider", module="carbonkivy.uix.divider")
register("CFloatLayout", module="carbonkivy.uix.floatlayout")
register("CIcon", module="carbonkivy.uix.icon")
register("CImage", module="carbonkivy.uix.image")
register("CLabel", module="carbonkivy.uix.label")
register("CLink", module="carbonkivy.uix.link")
register("CRelativeLayout", module="carbonkivy.uix.relativelayout")
register("CScreen", module="carbonkivy.uix.screen")
register("CScreenManager", module="carbonkivy.uix.screenmanager")
register("CScrollView", module="carbonkivy.uix.scrollview")
register("CStackLayout", module="carbonkivy.uix.stacklayout")

# Alias for the register function from Factory
font_register = LabelBase.register

"""
Registers custom fonts to the Kivy LabelBase.

Once registered, the fonts can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the font with the LabelBase
font_register("cicon", os.path.join(DATA, "Icons", "carbondesignicons.ttf"))
