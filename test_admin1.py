import face_recognition
import os

path = "faces/admin.jpg"

print("File exists:", os.path.exists(path))

img = face_recognition.load_image_file(path)

print("Image shape:", img.shape)
print("Image dtype:", img.dtype)