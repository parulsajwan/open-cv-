# Img read
import  cv2
img=cv2.imread('lena.jpg')
cv2.imshow('Orignal',img)
cv2.waitKey(0)
cv2.destroyAllwindows()