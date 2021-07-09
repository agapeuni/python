import os
import cv2
from distutils.sysconfig import get_python_lib

face_xml = get_python_lib() + "\\cv2\\data\\haarcascade_frontalface_default.xml"
eye_xml = get_python_lib() + "\\cv2\\data\\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(face_xml)
eye_cascade = cv2.CascadeClassifier(eye_xml)

image_file = os.getcwd() + "\\mei.png"
image = cv2.imread(image_file)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image_gray, 1.1, 3)
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (100, 150, 100), 2)
    face = image[y: y + h, x: x + w]
    face_gray = image_gray[y: y + h, x: x + w]

    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

cv2.imshow("face_image", image)
cv2.waitKey()
