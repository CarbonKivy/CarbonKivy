import os
from typing import List

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform
from kivy.app import App

from carbonkivy.theme.size_tokens import (
    font_size_tokens,
    spacing_tokens,
    button_size_tokens,
)

APP = App.get_running_app()


def get_font_size(token: str) -> float:
    return font_size_tokens[token]["font_size"]


def get_spacing(token: str) -> float:
    return spacing_tokens[token]


def get_button_size(token: str) -> float:
    return button_size_tokens[token]


button_background_tokens = {
    "active": {
        "Primary": "button_primary_active",
        "Secondary": "button_secondary_active",
        "Tertiary": "button_tertiary_active",
        "Ghost": "background_hover",
        "Danger Primary": "button_danger_active",
        "Danger Tertiary": "button_danger_active",
        "Danger Ghost": "button_danger_active",
    },
    "normal": {
        "Primary": "button_primary",
        "Secondary": "button_secondary",
        "Tertiary": "button_tertiary",
        "Ghost": "background_hover",
        "Danger Primary": "button_danger_primary",
        "Danger Tertiary": "transparent",
        "Danger Ghost": "button_danger_active",
    },
    "disabled": {
        "Primary": "button_disabled",
        "Secondary": "button_disabled",
        "Tertiary": "transparent",
        "Ghost": "transparent",
        "Danger Primary": "button_disabled",
        "Danger Tertiary": "transparent",
        "Danger Ghost": "transparent",
    },
}


def get_button_token(state: str, type: str) -> str:
    return button_background_tokens[state][type]


class _Dict(dict):
    """Implements access to dictionary values via a dot."""

    def __getattr__(self, name):
        return self[name]


# Feel free to override this const if you're designing for a device such as
# a GNU/Linux tablet.
DEVICE_IOS = platform == "ios" or platform == "macosx"
if platform != "android" and platform != "ios":
    DEVICE_TYPE = "desktop"
elif Window.width >= dp(738) and Window.height >= dp(738):
    DEVICE_TYPE = "tablet"
else:
    DEVICE_TYPE = "mobile"
