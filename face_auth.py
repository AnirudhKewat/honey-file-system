import face_recognition
import cv2
import os
from camera import capture_intruder


def check_admin_face():

    print("Checking admin authentication...")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    admin_path = os.path.join(BASE_DIR, "faces", "admin.jpg")

    if not os.path.exists(admin_path):
        print("admin.jpg missing ❌")
        return False

    # ✅ Load admin image using OpenCV instead of face_recognition
    admin_image = cv2.imread(admin_path)

    if admin_image is None:
        print("Failed to load admin.jpg ❌")
        return False

    # Convert BGR → RGB
    admin_image = cv2.cvtColor(admin_image, cv2.COLOR_BGR2RGB)

    admin_encodings = face_recognition.face_encodings(admin_image)

    if len(admin_encodings) == 0:
        print("No face found inside admin.jpg ❌")
        return False

    admin_encoding = admin_encodings[0]

    # Start webcam
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, frame = cam.read()

    cam.release()

    if not ret:
        print("Camera failed ❌")
        return False

    # Convert camera frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)

    if len(face_locations) == 0:
        print("No face detected ❌")
        capture_intruder()
        return False

    encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding in encodings:

        match = face_recognition.compare_faces(
            [admin_encoding],
            encoding,
            tolerance=0.5
        )

        if match[0]:
            print("Admin verified ✅")
            return True

    print("Intruder detected 🚨")

    capture_intruder()

    return False


if __name__ == "__main__":
    check_admin_face()