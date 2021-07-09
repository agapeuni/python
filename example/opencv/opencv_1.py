import os
import cv2
from distutils.sysconfig import get_python_lib

cascade_file = get_python_lib() + "\\cv2\\data\\haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

image_file = os.getcwd() + "\\photo.png"
image = cv2.imread(image_file)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(
    image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100)
)

if len(face_list) > 0:
    color = (0, 0, 255)
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness=3)
    
    cv2.imshow("face_image", image)
    k = cv2.waitKey()
    if k == ord("s"):
        cv2.imwrite("photo_output.jpg", image)
else:
    print("no face")
