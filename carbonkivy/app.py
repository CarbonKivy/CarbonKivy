from __future__ import annotations

__all__ = ("CarbonApp",)

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger

from carbonkivy.theme.theme import CarbonTheme
from carbonkivy.utils import update_system_ui


class CarbonApp(App, CarbonTheme):
    """
    The Main App class inherits from CarbonTheme to update the theme and appropriate colors based on the given theme.
    """

    def __init__(self, **kwargs) -> None:
        super(CarbonApp, self).__init__(**kwargs)
        if self.defaults:
            Clock.schedule_once(self.apply_system_bars, 0)

    def apply_system_bars(self, *args) -> None:
        icon_style = "Dark"
        if self.theme in ["Gray90", "Gray100"]:
            icon_style = "Light"
        update_system_ui(self.background, self.background, icon_style=icon_style)

    def on_theme(self, *args) -> None:
        super(CarbonApp, self).__init__(*args)
        if self.defaults:
            Clock.schedule_once(self.apply_system_bars, 0)

    def load_all_kv_files(self, directory: str, *args) -> None:
        """
        Recursively load all kv files from a given directory.
        """

        for root, dirs, files in os.walk(directory):
            if "carbonkivy" in directory:
                Logger.critical(
                    "CarbonKivy: "
                    "Do not use the word 'carbonkivy' in the name of the "
                    "directory from where you download KV files"
                )
            if (
                "venv" in root
                or ".buildozer" in root
                or os.path.join("carbonkivy") in root
            ):
                continue
            for file in files:
                if (
                    os.path.splitext(file)[1] == ".kv"
                    and file != "style.kv"  # if use PyInstaller
                    and "__MACOS" not in root  # if use Mac OS
                ):
                    path_to_kv_file = os.path.join(root, file)
                    Builder.load_file(path_to_kv_file)
