import numpy as np
import cv2 as cv

filename = 'catur.jpeg'
img = cv.imread(filename)

# Mengubah gambar menjadi grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Mencari titik sudut dengan metode Harris
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)

# Mengaplikasikan threshold dan konversi tipe data
ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

# Mencari centroid
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# Membuat kriteria untuk pengembangan titik sudut
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

# Menampilkan titik sudut pada gambar
for i in range(len(corners)):
    x, y = corners[i]
    cv.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

# Menampilkan gambar hasil
cv.imshow('corners', img)

# Menunggu input keyboard
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()