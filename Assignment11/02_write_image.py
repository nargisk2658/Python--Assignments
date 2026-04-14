import cv2

img = cv2.imread('sample.jpg')
cv2.imwrite('output.jpg', img)

print("Image saved successfully")