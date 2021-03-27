import cv2 as cv
import numpy as np

verde = np.uint8([[[0,255,0]]])

verde_hsv = cv.cvtColor(verde,cv.COLOR_BGR2HSV)

print("El color verde en HSV es: ", verde_hsv)