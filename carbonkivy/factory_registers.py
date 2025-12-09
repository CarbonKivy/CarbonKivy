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
register("CCheckbox", module="carbonkivy.uix.checkbox")
register("CDatatable", module="carbonkivy.uix.datatable")
register("CDatePicker", module="carbonkivy.uix.datepicker")
register("CDatePickerCalendar", module="carbonkivy.uix.datepicker")
register("CDatePickerDayButton", module="carbonkivy.uix.datepicker")
register("CDatePickerHeader", module="carbonkivy.uix.datepicker")
register("CDivider", module="carbonkivy.uix.divider")
register("CDropdown", module="carbonkivy.uix.dropdown")
register("CFloatLayout", module="carbonkivy.uix.floatlayout")
register("CGridLayout", module="carbonkivy.uix.gridlayout")
register("CBaseIcon", module="carbonkivy.uix.icon")
register("CIcon", module="carbonkivy.uix.icon")
register("CIconCircular", module="carbonkivy.uix.icon")
register("CImage", module="carbonkivy.uix.image")
register("CBaseLabel", module="carbonkivy.uix.label")
register("CLabel", module="carbonkivy.uix.label")
register("CLabelCircular", module="carbonkivy.uix.label")
register("CLink", module="carbonkivy.uix.link")
register("CLinkIcon", module="carbonkivy.uix.link")
register("CLinkText", module="carbonkivy.uix.link")
register("CLoadingLayout", module="carbonkivy.uix.loading")
register("CLoadingIndicator", module="carbonkivy.uix.loading")
register("CModal", module="carbonkivy.uix.modal")
register("CModalBody", module="carbonkivy.uix.modal")
register("CModalBodyContent", module="carbonkivy.uix.modal")
register("CModalCloseButton", module="carbonkivy.uix.modal")
register("CModalFooter", module="carbonkivy.uix.modal")
register("CModalHeader", module="carbonkivy.uix.modal")
register("CModalHeaderLabel", module="carbonkivy.uix.modal")
register("CModalHeaderTitle", module="carbonkivy.uix.modal")
register("CModalLayout", module="carbonkivy.uix.modal")
register("CBaseNotification", module="carbonkivy.uix.notification")
register("CNotification", module="carbonkivy.uix.notification")
register("CNotificationInline", module="carbonkivy.uix.notification")
register("CNotificationToast", module="carbonkivy.uix.notification")
register("CNotificationCloseButton", module="carbonkivy.uix.notification")
register("CRelativeLayout", module="carbonkivy.uix.relativelayout")
register("CScreen", module="carbonkivy.uix.screen")
register("CScreenManager", module="carbonkivy.uix.screenmanager")
register("CScrollView", module="carbonkivy.uix.scrollview")
register("CStackLayout", module="carbonkivy.uix.stacklayout")
register("CTab", module="carbonkivy.uix.tab")
register("CTabHeader", module="carbonkivy.uix.tab")
register("CTabHeaderItem", module="carbonkivy.uix.tab")
register("CTabHeaderLayout", module="carbonkivy.uix.tab")
register("CTabHeaderItemLayout", module="carbonkivy.uix.tab")
register("CTabLayout", module="carbonkivy.uix.tab")
register("CTabManager", module="carbonkivy.uix.tab")
register("CTextInput", module="carbonkivy.uix.textinput")
register("CTextInputLayout", module="carbonkivy.uix.textinput")
register("CTextInputLabel", module="carbonkivy.uix.textinput")
register("CTextInputHelperText", module="carbonkivy.uix.textinput")
register("CTextInputTrailingIconButton", module="carbonkivy.uix.textinput")
register("CToggletip", module="carbonkivy.uix.toggletip")
register("CTooltip", module="carbonkivy.uix.tooltip")
register("FocusContainer", module="carbonkivy.uix.focuscontainer")
register("UIShell", module="carbonkivy.uix.shell")
register("UIShellButton", module="carbonkivy.uix.shell")
register("UIShellHeader", module="carbonkivy.uix.shell")
register("UIShellHeaderName", module="carbonkivy.uix.shell")
register("UIShellHeaderMenuButton", module="carbonkivy.uix.shell")
register("UIShellLeftPanel", module="carbonkivy.uix.shell")
register("UIShellLayout", module="carbonkivy.uix.shell")
register("UIShellPanelLayout", module="carbonkivy.uix.shell")
register("UIShellPanelSelectionLayout", module="carbonkivy.uix.shell")
register("UIShellRightPanel", module="carbonkivy.uix.shell")

# Register the behavior with Kivy's Factory
register("AdaptiveBehavior", module="carbonkivy.behaviors.adaptive_behavior")
register(
    "BackgroundColorBehaviorCircular",
    module="carbonkivy.behaviors.background_color_behavior",
)
register(
    "BackgroundColorBehaviorRectangular",
    module="carbonkivy.behaviors.background_color_behavior",
)
register("ElevationBehavior", module="carbonkivy.behaviors.elevation_behavior")
register(
    "HierarchicalLayerBehavior",
    module="carbonkivy.behaviors.hierarchical_layer_behavior",
)
register("HoverBehavior", module="carbonkivy.behaviors.hover_behavior")
register("StateFocusBehavior", module="carbonkivy.behaviors.state_focus_behavior")


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
