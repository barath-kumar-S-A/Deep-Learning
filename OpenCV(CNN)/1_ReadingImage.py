# import cv2

# img = cv2.imread("barath.jpg")
# rect = cv2.rectangle(img,(400,500),(400,600),(255,0,0),2)
# cv2.imshow("image",rect)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2

cap =cv2.VideoCapture(0)
while(1):
    ret ,frame = cap.read()
    w = cap.get(3)
    h = cap.get(4)
    # img = cv2.line(frame,(0,0),(w,h),(0,0,255),3)
    img = cv2.rectangle(frame,(100,400),(400,600),(0,0,255),3)

    cv2.imshow("frame",img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    
  
    
    
    
    