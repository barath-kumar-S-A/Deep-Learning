import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()
    width = int(cap.get(3)) # its identify the width of the frame
    height = int(cap.get(4)) # its identify the height of  the frame
     
    image = np.zeros(frame.shape , np.uint8) #its give 0's value in array and frame length is array length its omly show the black screen
    small_frame = cv2.resize(frame , (0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2] = cv2.rotate(small_frame,cv2.ROTATE_180)
    image[:height//2 , width//2:] = cv2.rotate(small_frame,cv2.ROTATE_180)
    image[height//2: , :width//2] = small_frame
    image[height//2 : , width//2:]  = small_frame
    
    cv2.imshow("barath", image)
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()    