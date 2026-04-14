import cv2

img = cv2.imread('sample.jpg')

flip = cv2.flip(img, 1)   # 1 = horizontal flip

cv2.imshow('Flipped Image', flip)
cv2.waitKey(0)
cv2.destroyAllWindows()