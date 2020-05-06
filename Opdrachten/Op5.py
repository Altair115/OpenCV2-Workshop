import numpy as np
import cv2
import math

def getEyes(num, img, orgimg, tx, ty):
    ret, th = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for cnr in range(len(contours)):
        cnt = contours[cnr]
        perimeter = cv2.arcLength(cnt, True)
        area = cv2.contourArea(cnt)
        if perimeter == 0 or area == 0:
            continue
        factor = 4 * np.pi * area / perimeter ** 2
        if factor > 0.5 and area > 10:
            count += 1
    cv2.putText(orgimg, '%s' % count, (tx, ty), cv2.QT_FONT_NORMAL, 1, (255, 255, 255), 2, cv2.LINE_AA)
    eyes.append(count)

img = cv2.imread("D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/dobbelstenen.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayBlur = cv2.GaussianBlur(gray, (3, 3), 0)
ret, th = cv2.threshold(grayBlur, 5, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
eyes = []

num = 0
for cnr in range(len(contours)):
    cnt = contours[cnr]

    num += 1
    x, y, w, h = cv2.boundingRect(cnt)
    die = grayBlur[y:y + h, x:x + w]
    getEyes(num, die, img, x, y)

eyes.sort()
print('Sorted:', eyes)
cv2.imshow('dobbelstenen', img)

cv2.waitKey(0) 
cv2.destroyAllWindows() 