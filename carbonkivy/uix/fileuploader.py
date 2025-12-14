"""
Native file uploader for Kivy applications across multiple platforms: Windows, macOS, Linux, and Android.
"""

import os, sys

from kivy.event import EventDispatcher
from kivy.properties import ListProperty, StringProperty
from kivy.utils import platform

# --- Platform specific imports ---
# Windows
if sys.platform.startswith("win"):
    import ctypes
    from ctypes import wintypes

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ctypes.windll.user32.SetProcessDPIAware()

    OFN_EXPLORER = 0x00000008
    OFN_ALLOWMULTISELECT = 0x00000200
    OFN_FILEMUSTEXIST = 0x00001000
    OFN_PATHMUSTEXIST = 0x00000800

    class OPENFILENAMEW(ctypes.Structure):
        _fields_ = [
            ("lStructSize", wintypes.DWORD),
            ("hwndOwner", wintypes.HWND),
            ("hInstance", wintypes.HINSTANCE),
            ("lpstrFilter", wintypes.LPCWSTR),
            ("lpstrCustomFilter", wintypes.LPWSTR),
            ("nMaxCustFilter", wintypes.DWORD),
            ("nFilterIndex", wintypes.DWORD),
            ("lpstrFile", wintypes.LPWSTR),
            ("nMaxFile", wintypes.DWORD),
            ("lpstrFileTitle", wintypes.LPWSTR),
            ("nMaxFileTitle", wintypes.DWORD),
            ("lpstrInitialDir", wintypes.LPCWSTR),
            ("lpstrTitle", wintypes.LPCWSTR),
            ("Flags", wintypes.DWORD),
            ("nFileOffset", wintypes.WORD),
            ("nFileExtension", wintypes.WORD),
            ("lpstrDefExt", wintypes.LPCWSTR),
            ("lCustData", wintypes.LPARAM),
            ("lpfnHook", wintypes.LPVOID),
            ("lpTemplateName", wintypes.LPCWSTR),
            ("pvReserved", wintypes.LPVOID),
            ("dwReserved", wintypes.DWORD),
            ("FlagsEx", wintypes.DWORD),
        ]


# Android
elif platform == "android":
    from android import activity  # type: ignore
    from android.runnable import Runnable  # type: ignore
    from jnius import autoclass, cast  # type: ignore

    Uri = autoclass("android.net.Uri")
    Intent = autoclass("android.content.Intent")
    ClipData = autoclass("android.content.ClipData")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")

# macOS
elif sys.platform == "darwin":
    import objc
    from Cocoa import NSOpenPanel

# Linux
elif sys.platform.startswith("linux"):
    import gi  # type: ignore

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk  # type: ignore


class CFileUploader(EventDispatcher):
    files = ListProperty(None, allownone=True)
    file = StringProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(CFileUploader, self).__init__(**kwargs)

    # --- Platform-specific implementations ---
    def _open_file_windows(self, multiple: bool = False) -> str | list[str] | None:
        # Minimal WinAPI dialog
        buffer = ctypes.create_unicode_buffer(65536)
        ofn = OPENFILENAMEW()
        ofn.lStructSize = ctypes.sizeof(OPENFILENAMEW)
        ofn.lpstrFile = ctypes.cast(buffer, wintypes.LPWSTR)
        ofn.nMaxFile = len(buffer)
        ofn.lpstrFilter = "All Files\0*.*\0"
        ofn.nFilterIndex = 1
        ofn.Flags = OFN_EXPLORER | OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST
        if multiple:
            ofn.Flags |= OFN_ALLOWMULTISELECT

        if ctypes.windll.comdlg32.GetOpenFileNameW(ctypes.byref(ofn)):

            parts = buffer.value.split("\0")
            if len(parts) == 1:  # fallback if Explorer-style failed
                parts = buffer.value.split(" ")

            if len(parts) > 1:
                # First part is directory, rest are filenames
                directory = parts[0]
                files = [os.path.join(directory, f) for f in parts[1:] if f]
                return files
            else:
                # Single file selected → already absolute path
                file = parts[0]
                return file if not multiple else [file]
        return

    def _open_file_macos(self, multiple: bool = False) -> str | list[str] | None:
        # Needs testing
        panel = NSOpenPanel.openPanel()  # type: ignore
        panel.setAllowsMultipleSelection_(multiple)
        if panel.runModal():
            urls = [str(url.path()) for url in panel.URLs()]
            return urls if multiple else urls[0]
        return

    def _open_file_linux(self, multiple: bool = False) -> str | list[str] | None:
        action = Gtk.FileChooserAction.OPEN
        dialog = Gtk.FileChooserDialog(
            title="Select File",
            action=action,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        dialog.set_select_multiple(multiple)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if multiple:
                files = dialog.get_filenames()
                dialog.destroy()
                return files
            else:
                filename = dialog.get_filename()
                dialog.destroy()
                return filename
        dialog.destroy()
        return None

    def on_activity_result(self, requestCode: int, resultCode: int, intent) -> None:
        if requestCode == 1 and resultCode == PythonActivity.RESULT_OK:  # type: ignore
            selected_files = []
            if intent is not None:
                if intent.getData() is not None:
                    # Single file
                    uri = intent.getData()
                    selected_files.append(uri.toString())
                elif intent.getClipData() is not None:
                    # Multiple files
                    clipData = intent.getClipData()
                    for i in range(clipData.getItemCount()):
                        uri = clipData.getItemAt(i).getUri()
                        selected_files.append(uri.toString())

            self.files = selected_files
            self.file = selected_files[0] if selected_files else None
            return

    def _open_file_android(self, multiple: bool = False) -> None:
        intent = Intent(Intent.ACTION_GET_CONTENT)  # type: ignore
        intent.setType("*/*")
        intent.addCategory(Intent.CATEGORY_OPENABLE)  # type: ignore
        if multiple:
            intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, True)  # type: ignore
        activity.bind(on_activity_result=self.on_activity_result)  # type: ignore
        PythonActivity.mActivity.startActivityForResult(intent, 1)  # type: ignore
        return

    def upload_files(self):
        """Open a file dialog to select multiple files."""
        if platform == "android":
            Runnable(self._open_file_android)(multiple=True)
        elif sys.platform.startswith("win"):
            self.files = self._open_file_windows(multiple=True) or []
        elif sys.platform == "darwin":
            self.files = self._open_file_macos(multiple=True) or []
        elif sys.platform.startswith("linux"):
            self.files = self._open_file_linux(multiple=True) or []
        return self.files

    def upload_file(self):
        """Open a file dialog to select a single file."""
        if platform == "android":
            Runnable(self._open_file_android)(multiple=False)
        elif sys.platform.startswith("win"):
            self.file = self._open_file_windows(multiple=False)
        elif sys.platform == "darwin":
            self.file = self._open_file_macos(multiple=False)
        elif sys.platform.startswith("linux"):
            self.file = self._open_file_linux(multiple=False)
        return self.file


if __name__ == "__main__":
    uploader = CFileUploader()
    uploader.upload_files()
    print("Selected files:", uploader.files)
    uploader.upload_file()
    print("Selected file:", uploader.file)
