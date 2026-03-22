import cv2
import os


def capture_intruder():

    if not os.path.exists("captured"):

        os.mkdir("captured")


    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    cam.release()


    if ret:

        cv2.imwrite("captured/intruder.jpg", frame)