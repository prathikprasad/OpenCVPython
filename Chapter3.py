import cv2
import numpy as np

img = cv2.imread("Resources/prat.jpg")
print(img.shape)

imgResize = cv2.resize(img, (200,300))
print(imgResize.shape)

imgCropped = img[0:200,50:200]

cv2.imshow("Prathik P",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)


cv2.waitKey(0)