import numpy as np
import cv2

# read image through command line
img = cv2.imread('D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/tek2.png')

# convert the image to grayscale
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([-10,150,150])
upper_red = np.array([10,255,255])

lower_piece_red = np.array([160,150,150])
upper_piece_red = np.array([180,255,255])

piece_red_mask = cv2.inRange(hsv,lower_piece_red,upper_piece_red)
red_mask  = cv2.inRange(hsv,lower_red,upper_red)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold((red_mask+piece_red_mask),127,255,0)

# find contours in the binary image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#*

hull=[]
cnt = contours[0]
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

cv2.circle(img, (cX, cY), 5, (0, 255, 255), -1)

for i in range(len(contours)):
  hull.append(cv2.convexHull(contours[i], False))
  cv2.drawContours(img,hull,-1, (0, 255, 255),5,8)
# display the image
cv2.imshow("Image", img)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
