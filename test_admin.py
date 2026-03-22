import face_recognition

image = face_recognition.load_image_file("faces/admin.jpeg")

enc = face_recognition.face_encodings(image)

print(len(enc))