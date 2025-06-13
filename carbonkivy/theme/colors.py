from kivy.properties import ColorProperty
from kivy.utils import colormap, get_color_from_hex

from carbonkivy.theme.color_tokens import static_tokens


class ComponentColors:

    button_primary = ColorProperty()
    button_primary_hover = ColorProperty()
    button_primary_active = ColorProperty()
    button_secondary = ColorProperty()
    button_secondary_hover = ColorProperty()
    button_secondary_active = ColorProperty()
    button_tertiary = ColorProperty()
    button_tertiary_hover = ColorProperty()
    button_tertiary_active = ColorProperty()
    button_danger_primary = ColorProperty()
    button_danger_secondary = ColorProperty()
    button_dnager_hover = ColorProperty()
    button_danger_active = ColorProperty()
    button_separator = ColorProperty()
    button_disabled = ColorProperty()

    notification_background_error = ColorProperty()
    notification_background_success = ColorProperty()
    notification_background_info = ColorProperty()
    notification_background_warning = ColorProperty()
    notification_action_hover = ColorProperty()
    notification_action_tertiary_inverse = ColorProperty()
    notification_action_tertiary_inverse_active = ColorProperty()
    notification_action_tertiary_inverse_hover = ColorProperty()
    notification_action_tertiary_inverse_text = ColorProperty()
    notification_action_tertiary_inverse_text_on_color_disabled = ColorProperty()


class ThematicColors(ComponentColors):

    background = ColorProperty()
    background_hover = ColorProperty()
    background_active = ColorProperty()
    background_selected = ColorProperty()
    background_selected_hover = ColorProperty()
    background_inverse = ColorProperty()
    background_inverse_hover = ColorProperty()
    background_brand = ColorProperty()

    layer_01 = ColorProperty()
    layer_02 = ColorProperty()
    layer_03 = ColorProperty()
    layer_hover_01 = ColorProperty()
    layer_hover_02 = ColorProperty()
    layer_hover_03 = ColorProperty()
    layer_active_01 = ColorProperty()
    layer_active_02 = ColorProperty()
    layer_active_03 = ColorProperty()
    layer_selected_01 = ColorProperty()
    layer_selected_02 = ColorProperty()
    layer_selected_03 = ColorProperty()
    layer_selected_hover_01 = ColorProperty()
    layer_selected_hover_02 = ColorProperty()
    layer_selected_hover_03 = ColorProperty()
    layer_selected_inverse = ColorProperty()
    layer_selected_disabled = ColorProperty()
    layer_accent_01 = ColorProperty()
    layer_accent_02 = ColorProperty()
    layer_accent_03 = ColorProperty()
    layer_accent_hover_01 = ColorProperty()
    layer_accent_hover_02 = ColorProperty()
    layer_accent_hover_03 = ColorProperty()
    layer_accent_active_01 = ColorProperty()
    layer_accent_active_02 = ColorProperty()
    layer_accent_active_03 = ColorProperty()

    field_01 = ColorProperty()
    field_02 = ColorProperty()
    field_03 = ColorProperty()
    field_hover_01 = ColorProperty()
    field_hover_02 = ColorProperty()
    field_hover_03 = ColorProperty()

    border_interactive = ColorProperty()
    border_subtle_00 = ColorProperty()
    border_subtle_01 = ColorProperty()
    border_subtle_02 = ColorProperty()
    border_subtle_03 = ColorProperty()
    border_subtle_selected_01 = ColorProperty()
    border_subtle_selected_02 = ColorProperty()
    border_subtle_selected_03 = ColorProperty()
    border_strong_01 = ColorProperty()
    border_strong_02 = ColorProperty()
    border_strong_03 = ColorProperty()
    border_tile_01 = ColorProperty()
    border_tile_02 = ColorProperty()
    border_tile_03 = ColorProperty()
    border_inverse = ColorProperty()
    border_disabled = ColorProperty()

    text_primary = ColorProperty()
    text_secondary = ColorProperty()
    text_placeholder = ColorProperty()
    text_on_color = ColorProperty()
    text_on_color_disabled = ColorProperty()
    text_helper = ColorProperty()
    text_error = ColorProperty()
    text_inverse = ColorProperty()
    text_disabled = ColorProperty()

    link_primary = ColorProperty()
    link_primary_hover = ColorProperty()
    link_secondary = ColorProperty()
    link_inverse = ColorProperty()
    link_inverse_hover = ColorProperty()
    link_inverse_active = ColorProperty()
    link_inverse_visited = ColorProperty()
    link_visited = ColorProperty()

    icon_primary = ColorProperty()
    icon_secondary = ColorProperty()
    icon_on_color = ColorProperty()
    icon_on_color_disabled = ColorProperty()
    icon_interactive = ColorProperty()
    icon_inverse = ColorProperty()
    icon_disabled = ColorProperty()

    support_error = ColorProperty()
    support_success = ColorProperty()
    support_warning = ColorProperty()
    support_info = ColorProperty()
    support_error_inverse = ColorProperty()
    support_success_inverse = ColorProperty()
    support_warning_inverse = ColorProperty()
    support_info_inverse = ColorProperty()
    support_caution_minor = ColorProperty()
    support_caution_major = ColorProperty()
    support_caution_undefined = ColorProperty()

    focus = ColorProperty()
    focus_inset = ColorProperty()
    focus_inverse = ColorProperty()

    interactive = ColorProperty()

    overlay = ColorProperty()

    skeleton_element = ColorProperty()

    skeleton_background = ColorProperty()


class StaticColors:

    transparent = ColorProperty([1, 1, 1, 0])

    def __init__(self) -> None:
        super().__init__()
        static_tokenmap = {
            token: get_color_from_hex(hex) for token, hex in static_tokens.items()
        }
        colormap.update(static_tokenmap)
        for token in static_tokenmap:
            setattr(self.__class__, token, colormap[token])
