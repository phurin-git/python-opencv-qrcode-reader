# Realtime Decode QR
import cv2
import numpy as np
video = cv2.VideoCapture(0)
QR = cv2.QRCodeDetector()
while(True):
    ret, frame = video.read()
    frame2 = np.copy(frame)
    try:
        val, _, _ = QR.detectAndDecode(frame2)
    except:
        print("QR Error")
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.putText(frame2, val, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    cv2.imshow("my image", frame2)
video.release() 
cv2.destroyAllWindows()
