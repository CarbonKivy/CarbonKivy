import os
from datetime import datetime
from typing import Any, Literal

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import DictProperty
from kivy.utils import platform

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
    icon_style: Literal["Light", "Dark"] = "Dark",
    pad_status: bool = True,
    pad_nav: bool = False,
) -> None:
    """
    Update the color system of the status and navigation bar.

    Currently supports Android only.

    Author Kartavya Shukla -
        https://github.com/Novfensec
    """
    if platform == "android":
        from android.runnable import Runnable  # type: ignore
        from jnius import PythonJavaClass, autoclass, java_method  # type: ignore

        Color = autoclass("android.graphics.Color")
        Build_VERSION = autoclass("android.os.Build$VERSION")
        WindowInsetsType = autoclass("android.view.WindowInsets$Type")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        View = autoclass("android.view.View")

        activity = PythonActivity.mActivity
        window = activity.getWindow()
        decor_view = window.getDecorView()
        content_view = window.findViewById(autoclass("android.R$id").content)

        try:
            WindowCompat = autoclass("androidx.core.view.WindowCompat")
            inset_controller = WindowCompat.getInsetsController(window, decor_view)
        except Exception as e:
            inset_controller = None

        def parse_color(value):
            if isinstance(value, str):
                return Color.parseColor(value)
            elif isinstance(value, (list, tuple)) and len(value) == 4:
                r, g, b, a = value
                return Color.argb(a, r, g, b)
            else:
                raise ValueError("Color must be hex string or RGBA tuple")

        def apply_system_bars():
            status_color_int = parse_color(status_bar_color)
            navigation_color_int = parse_color(navigation_bar_color)

            if (Build_VERSION.SDK_INT >= 30):
                # API 30+ (Android 10+)
                if inset_controller and "WindowInsetsControllerCompat" in str(type(inset_controller)):
                    # Compat wrapper (AndroidX)
                    if icon_style == "Light":
                        inset_controller.setAppearanceLightStatusBars(False)
                        inset_controller.setAppearanceLightNavigationBars(False)
                    else:
                        inset_controller.setAppearanceLightStatusBars(True)
                        inset_controller.setAppearanceLightNavigationBars(True)
                else:
                    # Platform controller (API 30+)
                    controller = window.getInsetsController()
                    WindowInsetsController = autoclass("android.view.WindowInsetsController")
                    if icon_style == "Light":
                        controller.setSystemBarsAppearance(
                            0,
                            WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                            | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                        )
                    else:
                        controller.setSystemBarsAppearance(
                            WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                            | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                            WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                            | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                        )

            else:
                # Legacy flags for API 23–29
                visibility_flags = decor_view.getSystemUiVisibility()

                if icon_style == "Light":
                    visibility_flags &= ~View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                    if Build_VERSION.SDK_INT >= 26:
                        visibility_flags &= ~View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
                else:
                    visibility_flags |= View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                    if Build_VERSION.SDK_INT >= 26:
                        visibility_flags |= View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR

                decor_view.setSystemUiVisibility(visibility_flags)

            if Build_VERSION.SDK_INT >= 35:

                class InsetsListener(PythonJavaClass):
                    __javainterfaces__ = [
                        "android/view/View$OnApplyWindowInsetsListener"
                    ]
                    __javacontext__ = "app"

                    def __init__(self, status_color, navigation_color):
                        super().__init__()
                        self.status_color = status_color
                        self.navigation_color = navigation_color

                    @java_method(
                        "(Landroid/view/View;Landroid/view/WindowInsets;)Landroid/view/WindowInsets;"
                    )
                    def onApplyWindowInsets(self, view, insets):
                        try:
                            status_insets = insets.getInsets(
                                WindowInsetsType.statusBars()
                            )
                            nav_insets = insets.getInsets(
                                WindowInsetsType.navigationBars()
                            )

                            top_pad = status_insets.top if pad_status else 0
                            bottom_pad = nav_insets.bottom if pad_nav else 0

                            content_view.setPadding(0, top_pad, 0, bottom_pad)
                            content_view.setBackgroundColor(self.status_color)

                            window.setNavigationBarColor(self.navigation_color)
                        except Exception as e:
                            print("Insets error:", e)
                            import traceback
                            traceback.print_exc()
                        return insets

                listener = InsetsListener(status_color_int, navigation_color_int)
                activity._system_ui_listener = listener
                decor_view.setOnApplyWindowInsetsListener(listener)
                decor_view.requestApplyInsets()
            else:
                window.setStatusBarColor(status_color_int)
                window.setNavigationBarColor(navigation_color_int)

        Runnable(apply_system_bars)()

def get_display_cutout_insets():
    if platform == "android":
        from jnius import autoclass  # type: ignore

        activity = autoclass("org.kivy.android.PythonActivity").mActivity
        decor_view = activity.getWindow().getDecorView()
        insets = decor_view.getRootWindowInsets()

        if insets is not None:
            cutout = insets.getDisplayCutout()
            if cutout is not None:
                top = cutout.getSafeInsetTop()
                bottom = cutout.getSafeInsetBottom()
                return top, bottom
        return 0, 0


class _Dict(DictProperty):
    """Implements access to dictionary values via a dot."""

    def __getattr__(self, name) -> Any:
        return self[name]


# Feel free to override this const if you're designing for a device such as
# a GNU/Linux tablet.
DEVICE_TYPE = os.environ.get("devicetype", None)

if not DEVICE_TYPE:
    DEVICE_IOS = platform == "ios" or platform == "macosx"
    if platform != "android" and platform != "ios":
        DEVICE_TYPE = "desktop"
    elif Window.width >= dp(738) and Window.height >= dp(738):
        DEVICE_TYPE = "tablet"
    else:
        DEVICE_TYPE = "mobile"
