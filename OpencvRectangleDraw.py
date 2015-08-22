import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(img, (0,0), (300, 300), green, 5) #5 is thickness of line
# cv2.imshow("Slate", img)

red = (0, 0, 255)
cv2.line(img, (0,300), (300, 0), red)
# cv2.imshow("SlateNew", img)

cv2.rectangle(img, (10, 10), (60, 60), green)
#cv2.imshow("SlateNew", img)

cv2.rectangle(img, (10, 10), (60, 60), green)
cv2.imshow("SlateNew", img)
cv2.waitKey(0)

cv2.rectangle(img, (50, 200), (200, 225), red, 5)
cv2.imshow("SlateNew", img)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(img, (200, 50), (225, 125), blue, -1)
cv2.imshow("SlateNew", img)
cv2.waitKey(0)
