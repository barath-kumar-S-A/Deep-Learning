import cv2
import numpy as np

cap =cv2.VideoCapture("video.mp4")
# cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    if not ret:
        break
    
    # cv2.imshow("barath",frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    

n=np.zeros(frame.shape,np.uint8)
print(n)