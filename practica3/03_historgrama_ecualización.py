import cv2 as cv
from matplotlib import pyplot as plt


imagen = cv.imread("../imagenes/lenna.jpg", cv.IMREAD_GRAYSCALE)
img_ecualizada = cv.equalizeHist(imagen)

cv.imshow("Lenna", imagen)
cv.imshow("Lenna Ecualizada", img_ecualizada)

hist = cv.calcHist(img_ecualizada, [0], None, [256], [0, 256])
plt.plot(hist, color="gray")

plt.xlabel("intensidad de ilumnación")
plt.ylabel("Cantidad de pixeles")
plt.show()

cv.waitKey()
cv.destroyAllWindows()
