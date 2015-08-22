import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(img, (0,0), (300, 300), green)
cv2.imshow("Slate", img)

red = (0, 0, 255)
cv2.line(img, (0,300), (300, 0), red)
cv2.imshow("SlateNew", img)

cv2.waitKey(0)
