import cv2
# import matplotlib
import numpy as np

from matplotlib import pyplot as plt
img = cv2.imread('C:/PCD/latihan/subpixel4.png' , 0)
hist , bins = np.histogram(img.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / hist.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
