import cv2

capture = cv2.VideoCapture()

while True:
    isTrue, frame = capture.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(20) & 0xFF == "d":
        break

capture.release()
cv2.destroyAllWindows()

