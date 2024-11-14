import cv2
img =cv2.imread("barath.jpg")
h,w=img.shape[:2]
ratio = 1800/w
dim =(1800,int(h*ratio))
re=cv2.resize(img,dim)
cv2.imshow("flip",re)
cv2.waitKey(0)
cv2.destroyAllWindows()

