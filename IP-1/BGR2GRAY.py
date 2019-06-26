import cv2
import numpy as np
img=cv2.imread('lena.jpg')

cv2.imshow('Origanal',img)
cv2.waitKey(0)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray img',gray_img)
cv2.waitKey(0)


hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV img',hsv_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
