import cv2 as cv
from matplotlib import pyplot as plt


imagen = cv.imread("../imagenes/lenna.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("Lenna", imagen)

hist = cv.calcHist(imagen, [0], None, [256], [0, 256])
plt.plot(hist, color="gray")

plt.xlabel("intensidad de ilumnación")
plt.ylabel("Cantidad de pixeles")
plt.show()

cv.destroyAllWindows()
