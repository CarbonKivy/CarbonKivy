import threading

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Global event to signal file change
file_change_event = threading.Event()


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"File modified: {event.src_path}")
        file_change_event.set()

    def on_created(self, event):
        print(f"File created: {event.src_path}")
        file_change_event.set()


def start_file_watcher():
    directory_to_watch = "build"
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=True)
    observer.start()
    print(f"Watching {directory_to_watch} for changes...")

    try:
        while True:
            observer.join(0.5)  # Check for events every 0.1 seconds
    except KeyboardInterrupt:
        observer.stop()
        print("File watcher stopped.")
    observer.join()
