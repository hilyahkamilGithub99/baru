import cv2 as cv
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]
print( x+y ) # 250+10 = 260 % 256 = 4
[4]
