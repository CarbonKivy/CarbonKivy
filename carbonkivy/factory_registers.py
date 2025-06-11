import os

from kivy.core.text import LabelBase
from kivy.factory import Factory

from carbonkivy.config import DATA

# Alias for the register function from Factory
register = Factory.register

"""
Registers custom components to the Kivy Factory.

This code registers each component within the "uix" directory to the Kivy Factory. 
Once registered, the components can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the component with Kivy's Factory
register("CodeSnippet", module="carbonkivy.uix.codesnippet")
register("CodeSnippetCopyButton", module="carbonkivy.uix.codesnippet")
register("CodeSnippetLayout", module="carbonkivy.uix.codesnippet")
register("CAnchorLayout", module="carbonkivy.uix.anchorlayout")
register("CBoxLayout", module="carbonkivy.uix.boxlayout")
register("CBaseButton", module="carbonkivy.uix.button")
register("CButton", module="carbonkivy.uix.button")
register("CButtonCircular", module="carbonkivy.uix.button")
register("CButtonDanger", module="carbonkivy.uix.button")
register("CButtonGhost", module="carbonkivy.uix.button")
register("CButtonIcon", module="carbonkivy.uix.button")
register("CButtonLabel", module="carbonkivy.uix.button")
register("CButtonPrimary", module="carbonkivy.uix.button")
register("CButtonSecondary", module="carbonkivy.uix.button")
register("CButtonTertiary", module="carbonkivy.uix.button")
register("CDatatable", module="carbonkivy.uix.datatable")
register("CDivider", module="carbonkivy.uix.divider")
register("CFloatLayout", module="carbonkivy.uix.floatlayout")
register("CGridLayout", module="carbonkivy.uix.gridlayout")
register("CBaseIcon", module="carbonkivy.uix.icon")
register("CIcon", module="carbonkivy.uix.icon")
register("CIconCircular", module="carbonkivy.uix.icon")
register("CImage", module="carbonkivy.uix.image")
register("CLabel", module="carbonkivy.uix.label")
register("CLink", module="carbonkivy.uix.link")
register("CLinkIcon", module="carbonkivy.uix.link")
register("CLinkText", module="carbonkivy.uix.link")
register("CBaseNotification", module="carbonkivy.uix.notification")
register("CNotificationInline", module="carbonkivy.uix.notification")
register("CNotificationToast", module="carbonkivy.uix.notification")
register("CRelativeLayout", module="carbonkivy.uix.relativelayout")
register("CScreen", module="carbonkivy.uix.screen")
register("CScreenManager", module="carbonkivy.uix.screenmanager")
register("CScrollView", module="carbonkivy.uix.scrollview")
register("CStackLayout", module="carbonkivy.uix.stacklayout")
register("CTextInput", module="carbonkivy.uix.textinput")
register("CTextInputLayout", module="carbonkivy.uix.textinput")
register("CTextInputLabel", module="carbonkivy.uix.textinput")
register("CTextInputHelperText", module="carbonkivy.uix.textinput")
register("CTextInputTrailingIconButton", module="carbonkivy.uix.textinput")
register("FocusContainer", module="carbonkivy.uix.focuscontainer")

# Alias for the register function from Factory
font_register = LabelBase.register

"""
Registers custom fonts to the Kivy LabelBase.

Once registered, the fonts can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the font with the LabelBase
font_register("cicon", os.path.join(DATA, "Icons", "carbondesignicons.ttf"))

ibmplexsansregular = os.path.join(
    DATA, "IBMPlex", "IBM_Plex_Sans", "static", "IBMPlexSans-Regular.ttf"
)
ibmplexsansbold = os.path.join(
    DATA, "IBMPlex", "IBM_Plex_Sans", "static", "IBMPlexSans-Bold.ttf"
)
ibmplexsansitalic = os.path.join(
    DATA, "IBMPlex", "IBM_Plex_Sans", "static", "IBMPlexSans-Italic.ttf"
)
ibmplexsansbolditalic = os.path.join(
    DATA, "IBMPlex", "IBM_Plex_Sans", "static", "IBMPlexSans-BoldItalic.ttf"
)

font_register(
    "ibmplexsans",
    fn_regular=ibmplexsansregular,
    fn_bold=ibmplexsansbold,
    fn_italic=ibmplexsansitalic,
    fn_bolditalic=ibmplexsansbolditalic,
)
