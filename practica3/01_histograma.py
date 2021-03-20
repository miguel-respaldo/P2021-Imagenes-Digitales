import cv2 as cv
from matplotlib import pyplot as plt


imagen = cv.imread("../imagenes/lenna.jpg")
cv.imshow("Lenna", imagen)

color = ("b", "g", "r")

#  int = 32 bits = 4 bytes = 11223344 -> AARRGGBB
#  byte[] =                           ->  4 3 2 1

for i, c in enumerate(color):
    hist = cv.calcHist([imagen], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show()
cv.destroyAllWindows()