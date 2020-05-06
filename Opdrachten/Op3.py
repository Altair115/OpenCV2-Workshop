import cv2
import numpy as np

#COLOR PICKER RANGE
green = np.uint8([[[40, 40, 255]]]) #here insert the bgr values which you want to convert to hsv
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsvGreen)

lowerLimit = hsvGreen[0][0][0] - 10, 150, 150
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

print(upperLimit)
print(lowerLimit)

img = cv2.imread('D:/HW/OpenCV Workshop - distro2/OpenCV Workshop/tek2.png')
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

lower_piece_red = np.array([170,50,50])
upper_piece_red = np.array([180,255,255])

lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])


# Threshold the HSV image to get only blue colors
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
red_mask  = cv2.inRange(hsv,lower_red,upper_red)
green_mask = cv2.inRange(hsv,lower_green,upper_green)
piece_red_mask = cv2.inRange(hsv,lower_piece_red,upper_piece_red)

# Bitwise-AND mask and original image

blue_res = cv2.bitwise_and(img,img, mask= blue_mask)
red_res = cv2.bitwise_and(img,img, mask=(red_mask | piece_red_mask))
green_res = cv2.bitwise_and(img,img, mask=green_mask)
cv2.imshow('img',img)
cv2.imshow('mask',blue_mask)
cv2.imshow('res_blue',blue_res)
cv2.imshow('res_red',red_res)
cv2.imshow('res_green',green_res)

cv2.waitKey(0) 
cv2.destroyAllWindows() 

