import cv2 as cv
import numpy as np
import time

# membaca gambar
img1 = cv.imread('haha.jpeg')

# mengambil waktu sebelum proses
start_time = time.time()

# melakukan operasi pada gambar
img1 = cv.imread('logo.png')
for i in range(5,49,2):
  img1 = cv.medianBlur(img1,i)

# mengambil waktu setelah proses
end_time = time.time()

#mencetak waktu eksekusi
print ("Waktu: ", end_time - start_time)


