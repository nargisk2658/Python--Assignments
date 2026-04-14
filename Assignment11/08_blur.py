import cv2

img = cv2.imread('sample.jpg')

blur = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Blur Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()