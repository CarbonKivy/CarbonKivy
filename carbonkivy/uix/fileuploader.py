from kivy.event import EventDispatcher

from tkinter.filedialog import askopenfiles, askopenfile

class FileUploader(EventDispatcher):

    def __init__(self, **kwargs) -> None:
        super(FileUploader, self).__init__(**kwargs)

    def upload_files(self, *args) -> list[object]:
        """Open a file dialog to select multiple files."""
        files = askopenfiles(*args)
        return files

    def upload_file(self, *args) -> object:
        """Open a file dialog to select a single file."""
        file = askopenfile(*args)
        return file