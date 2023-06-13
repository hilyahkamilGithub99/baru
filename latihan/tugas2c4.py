import cv2 as cv
import numpy as np

img = cv.imread('logo3.png', 1)
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
type(img)
x = 5
y = x**2
y1 = x*x
z = np.uint8([5])
y2 = z*z
y3 = np.square(z)
z1 = cv.countNonZero(img)
z2 = np.count_nonzero(img)

print('x = ', x)
print('y = ', y)
print('y1 = ', y1)
print('z = ', z)
print('y2 = ', y2)
print('y3 = ', y3)
print('z1 = ', z1)
print('z2 = ', z2)