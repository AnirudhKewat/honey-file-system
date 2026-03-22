import face_recognition
import cv2
import os
from datetime import datetime
from camera import capture_intruder


ADMIN_IMAGE = "captured/ad.jpg"


def check_admin_face():

    print("Checking face authentication...")

    admin_image = face_recognition.load_image_file(ADMIN_IMAGE)

    admin_encoding = face_recognition.face_encodings(admin_image)

    if len(admin_encoding) == 0:
        print("No face found in admin image ❌")
        return False

    admin_encoding = admin_encoding[0]

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, frame = camera.read()

    camera.release()

    if not ret:
        print("Camera capture failed ❌")
        return False

    rgb_frame = frame[:, :, ::-1]

    unknown_faces = face_recognition.face_encodings(rgb_frame)

    if len(unknown_faces) == 0:

        print("No face detected 🚨")

        capture_intruder()

        return False


    match = face_recognition.compare_faces(
        [admin_encoding],
        unknown_faces[0]
    )[0]


    if match:

        print("Admin verified ✅")

        return True


    else:

        print("Intruder detected 🚨")

        capture_intruder()

        return False


if __name__ == "__main__":
    check_admin_face()