import cv2
import numpy as np

img = cv2.imread("download.png")
img = cv2.resize(img,(0,0),fx=3.5,fy=3.5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

coner = cv2.goodFeaturesToTrack(gray,100,0.01,10)
coner = np.int0(coner)
for co in coner:
    x,y = co.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)
#     for i in range(len(coner)):
#         for j in range(i+1,len(coner)):
#             c1=tuple(coner[i][0])
#             c2=tuple(coner[j][0])
#             colour = tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
#             cv2.line(img,c1,c2,colour,1)
cv2.imshow("barath",img)
cv2.waitKey(0)
cv2.destroyAllWindows()