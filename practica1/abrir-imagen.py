import cv2 as cv

img = cv.imread("../imagenes/lenna.jpg")

cv.imshow("Lenna", img)

while True:
    k = cv.waitKey(0)
    if k == 27: # 27 es el escape (ESC)
        break

cv.destroyAllWindows()
