import face_recognition
import cv2
import os
from camera import capture_intruder


def check_admin_face():

    print("Checking admin authentication...")

    # Get correct path of admin image
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    admin_path = os.path.join(BASE_DIR, "faces", "admin.jpg")

    # Load admin image
    admin_image = face_recognition.load_image_file(admin_path)

    admin_encodings = face_recognition.face_encodings(admin_image)

    if len(admin_encodings) == 0:
        print("No face found in admin.jpg ❌")
        return False

    admin_encoding = admin_encodings[0]

    # Start camera
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    cam.release()

    if not ret:
        print("Camera not working ❌")
        return False

    try:
        # Convert BGR → RGB (VERY IMPORTANT FIX)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    except:
        print("Frame conversion failed ❌")
        return False

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)

    if len(face_locations) == 0:
        print("No face detected from camera ❌")
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


# Run standalone test
if __name__ == "__main__":
    check_admin_face()