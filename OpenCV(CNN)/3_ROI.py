import cv2 
img = cv2.imread("h.jpeg",1)
re = cv2.resize(img,(0,0),fx=2,fy=2)

cv2.imshow("baratjh",re)
cv2.waitKey(0)
cv2.destroyAllWindows()

