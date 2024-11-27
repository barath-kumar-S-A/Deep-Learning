import cv2
import random
img =cv2.imread("h.jpeg")

# for i in range(img.shape[0]):
#     for j in range(100,700,5):
#         img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
        
print(type(img))
cv2.waitKey(0)
cv2.destroyAllWindows()