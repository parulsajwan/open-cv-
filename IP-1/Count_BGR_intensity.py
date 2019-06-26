# Intensity of BGR
import cv2
import numpy as np

img= cv2.imread('lena.jpg')
cv2.imshow('Orignal',img)

B,G,R= img[0,0]

print(B,G,R)
print(img.shape)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray shape',gray_img)

print(gray_img.shape)
print(gray_img[0,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

