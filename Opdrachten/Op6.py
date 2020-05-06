import cv2
import numpy as np

image = cv2.imread("D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/auto.jpg")

# Select ROI
# (x, y, w, h) = cv2.selectROI("Image", imgorg, False, False)
# Crop image
img = image[103:178, 86:258]

gr = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (5, 5), 0)
ret, th = cv2.threshold(gr, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

nbp = 0
lz = 0
for cnr in range(len(contours)):
    cnt = contours[cnr]

    area = cv2.contourArea(cnt)
    if area > lz:
        lz = area
        nbp = [cnt]

cv2.drawContours(img, nbp, -1, (0, 0, 255), 3)
cv2.imshow("frame", image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 