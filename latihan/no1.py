import cv2

img = cv2.imread("spiderman.jpg", 1)
resize = cv2.resize(img, (800, 400))
cv2.imshow("Spiderman", resize)
cv2.imwrite("Spiderman_resize.jpg", resize) # menyimpan citra baru yang sudah diperbesar 2x
cv2.waitKey(0)
cv2.destroyAllWindows()