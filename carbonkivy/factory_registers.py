from kivy.factory import Factory

# Alias for the register function from Factory
register = Factory.register

"""
Registers custom components to the Kivy Factory.

This code registers each component within the "ui" directory to the Kivy Factory. 
Once registered, the components can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the component with Kivy's Factory
register("CAnchorLayout", module="carbonkivy.uix.anchorlyout")
register("CBoxLayout", module="carbonkivy.uix.boxlayout")
register("CButton", module="carbonkivy.uix.button")
register("CButtonGhost", module="carbonkivy.uix.button")
register("CButtonPrimary", module="carbonkivy.uix.button")
register("CButtonSecondary", module="carbonkivy.uix.button")
register("CFloatLayout", module="carbonkivy.uix.floatlayout")
register("CIcon", module="carbonkivy.uix.icon")
register("CLabel", module="carbonkivy.uix.label")
register("CRelativeLayout", module="carbonkivy.uix.relativelayout")
register("CScreen", module="carbonkivy.uix.screen")
register("CScreenManager", module="carbonkivy.uix.screenmanager")
register("CStackLayout", module="carbonkivy.uix.stacklayout")
