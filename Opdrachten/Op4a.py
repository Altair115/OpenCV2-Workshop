import numpy as np
import cv2

#load a image & Gray it then blur it
image = cv2.imread('D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/bouten_moeren.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(25,25),0)

ret,th= cv2.threshold(blur,180,255,cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,-1, (0, 255, 255),4,8)

# display the image
cv2.imshow("Image", image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 