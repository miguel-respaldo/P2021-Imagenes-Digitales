import cv2 as cv
import numpy as np

#img = cv.imread("../imagenes/lenna.jpg")
img = cv.imread("../imagenes/rgb.png")

# Separar los canales en RGB
b,g,r = cv.split(img)
zeros = np.zeros(b.shape, dtype=np.uint8)

cv.imshow("Lenna", img)
cv.imshow("Zeros", zeros)
cv.imshow("Rojo", r)
cv.imshow("Verde", g)
cv.imshow("Azul", b)

while True:
    k = cv.waitKey(0)
    if k == 27: # 27 es el escape (ESC)
        break
cv.destroyAllWindows()
