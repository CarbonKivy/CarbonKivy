import os
from datetime import datetime
from typing import Literal, Any

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import DictProperty
from kivy.utils import get_hex_from_color, platform

from carbonkivy.config import IBMPlex
from carbonkivy.theme.size_tokens import (
    button_size_tokens,
    font_style_tokens,
    spacing_tokens,
)


def get_font_name(typeface: str, weight_style: str) -> str:
    font_dir = os.path.join(
        IBMPlex,
        typeface.replace(" ", "_"),
        "static",
        f"{typeface.replace(' ', '')}-{weight_style}.ttf",
    )
    return font_dir


def get_font_style(token: str) -> float:
    return font_style_tokens[token]


def get_spacing(token: str) -> float:
    return spacing_tokens[token]


def get_button_size(token: str) -> float:
    return button_size_tokens[token]


def get_latest_time(*args) -> str:
    return datetime.now().strftime("%I:%M:%S %p")


def update_system_ui(
    status_bar_color: list[float] | str,
    navigation_bar_color: list[float] | str,
    icon_style: Literal["Light", "Dark"],
) -> None:
    """
    Update the color system of the status and navigation bar.

    Currently supports Android only.

    The code is taken from AKivyMD project -
        https://github.com/kivymd-extensions/akivymd

    Source code -
        kivymd_extensions/akivymd/uix/statusbarcolor.py

    Author Sina Namadian -
        https://github.com/quitegreensky

    Author Kartavya Shukla (Bug Fix Related to Navigation Icon colors) -
        https://github.com/Novfensec
    """

    if platform == "android":
        from android.runnable import run_on_ui_thread  # type: ignore
        from jnius import autoclass

        Color = autoclass("android.graphics.Color")
        WindowManager = autoclass("android.view.WindowManager$LayoutParams")
        activity = autoclass("org.kivy.android.PythonActivity").mActivity
        View = autoclass("android.view.View")

        def statusbar(*args):
            status_color = None
            navigation_color = None
            visibility_flags = 0

            if status_bar_color:
                status_color = get_hex_from_color(status_bar_color)[:7]
            if navigation_bar_color:
                navigation_color = get_hex_from_color(navigation_bar_color)[:7]

            window = activity.getWindow()

            if icon_style == "Dark":
                visibility_flags = (
                    View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                    | View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
                )
            elif icon_style == "Light":
                visibility_flags = 0

            window.getDecorView().setSystemUiVisibility(visibility_flags)

            window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
            window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)

            if status_color:
                window.setStatusBarColor(Color.parseColor(status_color))
            if navigation_color:
                window.setNavigationBarColor(Color.parseColor(navigation_color))

        return run_on_ui_thread(statusbar)()


class _Dict(DictProperty):
    """Implements access to dictionary values via a dot."""

    def __getattr__(self, name) -> Any:
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
