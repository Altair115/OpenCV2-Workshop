import numpy as np
import cv2 
import math

#load a image & Gray it then blur it
image = cv2.imread('D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/bouten_moeren2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(25,25),0)

ret,th = cv2.threshold(blur,180,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hierarchy = hierarchy[0]
for cnr in range(len(contours)):
    cnt = contours[cnr]
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    perimeter = cv2.arcLength(cnt, True)
    factor = 4 * np.pi * area / perimeter ** 2
    holes = 0
    child = hierarchy[cnr][2]
    while child >= 0:
        holes += cv2.contourArea(contours[child])
        child = hierarchy[child][0]

    if 1000 < area < 1800:
            cv2.drawContours(image, [cnt], -1, (255, 0, 0), 3)
    elif 2000 < area < 3000 and holes > 300:
            cv2.drawContours(image, [cnt], -1, (0, 255, 255), 3)
    elif 2000 < area < 3000 and holes < 15:
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)
    elif  area > 3000:
            cv2.drawContours(image, [cnt], -1, (0,0,255), 3)

#cv2.drawContours(image,contours,-1, (255, 0, 238),5,8)
print(hierarchy)
# display the image
cv2.imshow("Image", image)
cv2.waitKey(0) 
cv2.destroyAllWindows()