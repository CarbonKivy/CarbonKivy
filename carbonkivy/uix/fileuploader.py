"""
Native file uploader for Kivy applications across multiple platforms: Windows, macOS, Linux, and Android.
"""

import os, sys

from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ListProperty, StringProperty, DictProperty
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
    ContentResolver = PythonActivity.mActivity.getContentResolver()
    FileOutputStream = autoclass('java.io.FileOutputStream')

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

    title = StringProperty("Open")

    filters = DictProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(CFileUploader, self).__init__(**kwargs)

    # --- Platform-specific implementations ---
    def _open_file_windows(self, multiple: bool = False, *args) -> str | list[str] | None:
        # Minimal WinAPI dialog
        buffer = ctypes.create_unicode_buffer(65536)
        ofn = OPENFILENAMEW()
        ofn.lStructSize = ctypes.sizeof(OPENFILENAMEW)
        ofn.lpstrFile = ctypes.cast(buffer, wintypes.LPWSTR)
        ofn.nMaxFile = len(buffer)
        if self.filters:
            parts = []
            for label, exts in self.filters.items():
                parts.append(label)
                parts.append(";".join(exts))

            filter_str = "\0".join(parts) + "\0\0"
            ofn.lpstrFilter = filter_str
        else:
            ofn.lpstrFilter = "All Files\0*.*\0"

        ofn.nFilterIndex = 1
        ofn.Flags = OFN_EXPLORER | OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST
        if multiple:
            ofn.Flags |= OFN_ALLOWMULTISELECT

        if ctypes.windll.comdlg32.GetOpenFileNameW(ctypes.byref(ofn)):

            parts = buffer.value.split("\0")
            if multiple:
                if len(parts) == 1:  # fallback if Explorer-style failed
                    parts = buffer.value.split(" ")

                if len(parts) > 1:
                    # First part is directory, rest are filenames
                    directory = parts[0]
                    files = [os.path.join(directory, f) for f in parts[1:] if f]
                    return files
            else:
                # Single file selected → already absolute path
                file = str(parts[0])
                print(file)
                return file if not multiple else [file]
        return

    def _open_file_macos(self, multiple=False, *args) -> str | list[str] | None:
        # needs testing
        panel = NSOpenPanel.openPanel() # type: ignore
        panel.setAllowsMultipleSelection_(multiple)
        if self.filters:
            all_exts = [ext.replace("*.", "") for exts in self.filters.values() for ext in exts]
            panel.setAllowedFileTypes_(all_exts)
        if panel.runModal():
            urls = [str(url.path()) for url in panel.URLs()]
            return urls if multiple else urls[0]
        return

    def _open_file_linux(self, multiple: bool = False, *args) -> str | list[str] | None:
        action = Gtk.FileChooserAction.OPEN
        dialog = Gtk.FileChooserDialog(
            title="Select File",
            action=action,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
        )
        dialog.set_select_multiple(multiple)

        if self.filters:
            for label, exts in self.filters.items():
                f = Gtk.FileFilter()
                f.set_name(label)
                for ext in exts:
                    f.add_pattern(ext)
                dialog.add_filter(f)

        files = []
        def on_response(dlg, response):
            if response == Gtk.ResponseType.OK:
                if multiple:
                    files = dlg.get_filenames()
                    dlg.destroy()
                else:
                    files = [dlg.get_filename()]
                    dlg.destroy()
            else:
                dlg.destroy()

            Gtk.main_quit() # Exit the GTK main loop and return control to Kivy
            self.file = files[0] if files else None
            self.files = files

        dialog.connect("response", on_response)

        # Non-blocking: show the dialog
        dialog.show()
        Gtk.main()

    def on_activity_result(self, requestCode: int, resultCode: int, intent) -> None:
        if requestCode == 1 and resultCode == PythonActivity.RESULT_OK:  # type: ignore
            selected_files = []
            if intent is not None:
                if intent.getData() is not None:
                    # Single file
                    uri = intent.getData()
                    filename = self.copy_content_uri(uri.toString(), 0)
                    selected_files.append(filename)
                elif intent.getClipData() is not None:
                    # Multiple files
                    clipData = intent.getClipData()
                    for i in range(clipData.getItemCount()):
                        uri = clipData.getItemAt(i).getUri()
                        try:
                            filename = self.copy_content_uri(uri.toString(), i)
                            selected_files.append(filename)
                        except Exception as e:
                            print(e)

            def _apply(_dt):
                self.files = selected_files
                self.file = self.files[0] if self.files else None

            Clock.schedule_once(_apply)
        return

    def copy_content_uri(self, uri_string, index=0):
        """Resolve a content:// URI into a local temp file path."""
        uri = Uri.parse(uri_string)
        inputStream = ContentResolver.openInputStream(uri)

        temp_path = os.path.join(
            PythonActivity.mActivity.getFilesDir().getAbsolutePath(),
            f"picked_{os.path.basename(uri.getPath())}"   # unique filename per file
        )
        fos = FileOutputStream(temp_path)
        buf = bytearray(1024)
        while True:
            read = inputStream.read(buf)
            if read == -1:
                break
            fos.write(buf, 0, read)
        fos.close()
        inputStream.close()
        return temp_path

    def _open_file_android(self, multiple: bool = False, mime_type: str = "*/*", *args) -> None:
        intent = Intent(Intent.ACTION_GET_CONTENT)  # type: ignore
        intent.setType(mime_type)
        intent.addCategory(Intent.CATEGORY_OPENABLE)  # type: ignore
        if multiple:
            intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, True)  # type: ignore
        activity.bind(on_activity_result=self.on_activity_result)  # type: ignore
        PythonActivity.mActivity.startActivityForResult(intent, 1)  # type: ignore
        return

    def upload_files(self, filters: list | None = None, mime_type: str = "*/*", *args) -> list:
        """Open a file dialog to select multiple files.

        filters = {
            "JPEG Files": ["*.jpg", "*.jpeg"],
            "PNG Files": ["*.png"],
            "All Images": ["*.jpg", "*.jpeg", "*.png"]
        }

        """
        if filters:
            self.filters = filters
        if platform == "android":
            Runnable(self._open_file_android)(multiple=True, mime_type=mime_type)
        elif sys.platform.startswith("win"):
            self.files = self._open_file_windows(multiple=True) or []
        elif sys.platform == "darwin":
            self.files = self._open_file_macos(multiple=True) or []
        elif sys.platform.startswith("linux"):
            self._open_file_linux(multiple=True)
        return self.files

    def upload_file(self, filters: list | None = None, mime_type: str = "*/*", *args) -> str:
        """Open a file dialog to select a single file.

        filters = {
            "JPEG Files": ["*.jpg", "*.jpeg"],
            "PNG Files": ["*.png"],
            "All Images": ["*.jpg", "*.jpeg", "*.png"]
        }

        """
        if filters:
            self.filters = filters
        if platform == "android":
            Runnable(self._open_file_android)(multiple=False, mime_type=mime_type)
        elif sys.platform.startswith("win"):
            self.file = self._open_file_windows(multiple=False)
        elif sys.platform == "darwin":
            self.file = self._open_file_macos(multiple=False)
        elif sys.platform.startswith("linux"):
            self._open_file_linux(multiple=False)
        return self.file


if __name__ == "__main__":
    uploader = CFileUploader()
    uploader.upload_files()
    print("Selected files:", uploader.files)
    uploader.upload_file()
    print("Selected file:", uploader.file)
