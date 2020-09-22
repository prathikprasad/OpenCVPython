import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")


cv2.imshow("image", img)

cv2.waitKey(0)