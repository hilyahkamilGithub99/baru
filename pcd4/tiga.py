import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('C:\PCD\pcd4\Spiderman1.jpg') 
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2) 
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input') 
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()