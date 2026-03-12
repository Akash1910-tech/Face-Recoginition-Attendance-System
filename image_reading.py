import cv2
import mediapipe as mp   # ✅ This line is MANDATORY
import os
import numpy as np
from datetime import datetime


name = 'Anusha'
file_path = f'known_faces/{name}.jpg'
os.makedirs('known_faces',exist_ok=True)

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if ret:
    cv2.imwrite(file_path, frame)
    cv2.imshow("Captured",frame)
    cv2.waitKey(1000) #show image for 1 second
cam.release()
cv2.destroyAllWindows()

