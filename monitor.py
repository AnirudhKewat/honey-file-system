from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

from face_auth import check_admin_face
import database
from email_alert import send_alert
from camera import capture_intruder

WATCH_FOLDER = "honeyfiles"


class HoneyFileHandler(FileSystemEventHandler):

    def on_modified(self, event):

        if event.is_directory:
            return

        print("Honeyfile accessed:", event.src_path)

        is_admin = check_admin_face()

        if is_admin:

            print("Admin detected ✅")

            database.insert_log(
                event.src_path,
                "Admin"
            )

        else:

            print("Intruder detected 🚨")

            database.insert_log(
                event.src_path,
                "Intruder"
            )
            image_path = capture_intruder()

            send_alert(
        "Intruder opened honeyfile!",
        image_path
    )


if __name__ == "__main__":

    if not os.path.exists(WATCH_FOLDER):

        print("Creating honeyfiles folder...")

        os.mkdir(WATCH_FOLDER)


    database.init_db()


    observer = Observer()

    observer.schedule(
        HoneyFileHandler(),
        WATCH_FOLDER,
        recursive=False
    )

    observer.start()

    print("Monitoring honeyfiles... system active ✅")

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()