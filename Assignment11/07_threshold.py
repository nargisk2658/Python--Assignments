import cv2

img = cv2.imread('sample.jpg', 0)  # 0 = grayscale

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()