import cv2 as cv
import numpy as np

img1 = cv.imread('D:\PCD\pcd4\skala_fuzzy1.jpeg')
img2 = cv.imread('D:\PCD\pcd4\Spiderman.jpg')
dst123 = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst123)
cv.waitKey(0)
cv.destroyAllWindows()