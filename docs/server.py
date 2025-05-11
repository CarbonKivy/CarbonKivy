import os
import threading

from file_watcher import file_change_event, start_file_watcher
from flask import Flask, Response, send_from_directory
from utils import get_ip_address

app = Flask(__name__)


@app.route("/")
def serve_index():
    return send_from_directory("build", "index.html")


@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory("build", path)


@app.route("/events")
def events():
    def event_stream():
        while True:
            if file_change_event.is_set():
                yield "data: reload\n\n"
                file_change_event.clear()  # Reset the event after handling
                break  # Exit loop after handling to avoid redundant reloads

    return Response(event_stream(), mimetype="text/event-stream")


def run_flask():
    ip_address = get_ip_address()
    print(f"Server running on http://{ip_address}:8000")
    app.run(host="0.0.0.0", port=8000, debug=True)


def run_server():
    watcher_thread = threading.Thread(target=start_file_watcher)
    watcher_thread.daemon = True
    watcher_thread.start()

    run_flask()


if __name__ == "__main__":
    run_server()
