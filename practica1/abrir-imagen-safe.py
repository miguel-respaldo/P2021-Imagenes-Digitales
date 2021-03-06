import cv2 as cv
import sys

img = cv.imread("../imagenes/lenna.jpg")

# cv.IMREAD_GRAYSCALE en escala de grises
# cv.IMREAD_COLOR en color (default) formato de 8-bits BGR
# cv.IMREAD_UNCHANGED lee con todo y alphas

if img is None:
    sys.exit("La imagen no existe")

cv.imshow("Lenna", img)

k = cv.waitKey(0)
