import cv2
img = cv2.imread("h.jpeg")
ro=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("barath",ro)
cv2.waitKey(0)
cv2.destroyAllWindows()