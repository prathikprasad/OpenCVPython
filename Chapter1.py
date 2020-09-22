import cv2

'''img = cv2.imread("Resources/prat.jpeg")
cv2.imshow("Prathik P",img)
cv2.waitKey(0)'''

'''cap = cv2.VideoCapture("Resources/manojaaa.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break'''

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break