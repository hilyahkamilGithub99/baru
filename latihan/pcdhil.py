# Import library

import numpy as np
import cv2
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
#load citra 
img = cv2.imread('tokyo.jpg')
plt.imshow(img);
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); 
