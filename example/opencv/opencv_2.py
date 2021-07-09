import os
import cv2
from distutils.sysconfig import get_python_lib

cascade_file = get_python_lib() + "\\cv2\\data\\haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

image_file = os.getcwd() + "\\photo.png"
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(
    image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100)
)

if len(face_list) > 0:
    for (x, y, w, h) in face_list:
        face_img = image[y: y + h, x: x + w]
        face_img = cv2.resize(face_img, (w // 30, h // 30))
        face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
        image[y: y + h, x: x + w] = face_img
    cv2.imshow("face_image", image)

    k = cv2.waitKey()
    if k == ord("s"):
        cv2.imwrite("photo_output.png", image)
else:
    print("no face")
