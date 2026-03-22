import cv2
import os
from datetime import datetime


def capture_intruder():

    print("Opening camera...")

    if not os.path.exists("captured"):

        os.mkdir("captured")

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cam.isOpened():

        print("Camera error ❌")

        return False

    ret, frame = cam.read()

    cam.release()

    if not ret:

        print("Capture failed ❌")

        return False

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

    path = os.path.join("captured", filename)

    cv2.imwrite(path, frame)

    print("Intruder captured ✅")

    return True