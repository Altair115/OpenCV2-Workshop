import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    img = cv2.imread('D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/tek1.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
