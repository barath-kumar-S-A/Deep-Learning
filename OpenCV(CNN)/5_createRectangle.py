import cv2 
import numpy as np



cap=cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # img = cv2.line(frame,(0,0),(width,height),(0,255,0),3 )# Draw the line toplef to bottom right
    # img = cv2.line(img,(0,height),(width,0),(255,0,0),2)# Draw the line topright to left bottom
    rect= cv2.rectangle(frame,(400,600),(0,0),(0,0,255),-1) #draw the rectanglr
    # img = cv2.circle(img,(100,100),60,(255,0,0),3)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # img = cv2.putText(img,"im barath",(width-600,200),font,2,(0,0,0),3,cv2.LINE_AA)
    cv2.imshow("barath",rect)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    