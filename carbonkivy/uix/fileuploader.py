from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty

from tkinter.filedialog import askopenfiles, askopenfile


class CFileUploader(EventDispatcher):

    files = ListProperty()

    file = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CFileUploader, self).__init__(**kwargs)

    def upload_files(self, *args) -> list[object]:
        """Open a file dialog to select multiple files."""
        files = askopenfiles(*args)
        self.files = files
        return self.files

    def upload_file(self, *args) -> object:
        """Open a file dialog to select a single file."""
        file = askopenfile(*args)
        self.file = file
        return self.file
