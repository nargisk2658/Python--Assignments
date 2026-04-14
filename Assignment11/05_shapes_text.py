import cv2

img = cv2.imread('sample.jpg')

# Rectangle
cv2.rectangle(img, (50,50), (200,200), (255,0,0), 2)

# Text
cv2.putText(img, "Hello", (60, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,255,0), 2)

cv2.imshow('Shapes & Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()