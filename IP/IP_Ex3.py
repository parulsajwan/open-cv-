import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('Orignal', img)
cv2.waitKey()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()