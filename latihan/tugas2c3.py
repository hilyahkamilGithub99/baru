import cv2 as cv
import numpy as np

cv.useOptimized()
True
img = cv.imread('logo2.png')
res = cv.medianBlur(img, 49)
print (res)
cv.setUseOptimized(False)
cv.useOptimized()
False
res = cv.medianBlur(img,49)
print(res)
# cv.imshow("Display window", img)
# if cv.waitKey(0) & 0xff == 27:
#     cv.destroyAllWindows()

