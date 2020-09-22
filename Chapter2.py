import cv2
import numpy as np

img = cv2.imread("Resources/prat.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDia = cv2.dilate(imgCanny, kernel, iterations=1)
imgEro = cv2.erode(imgDia, kernel, iterations=1)
cv2.imshow("Grey Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dia Image", imgDia)
cv2.imshow("Ero Image", imgEro)

cv2.waitKey(0)