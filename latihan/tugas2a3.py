import numpy as np
import cv2 as cv
img1 = cv.imread('haha.jpeg')
img2 = cv.imread('haha2.jpeg')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()