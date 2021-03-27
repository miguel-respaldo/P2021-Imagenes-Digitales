import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

fondo = cv.imread("../tarea/chapala.webp")
# Redimencionamos el fondo al tamañano de la imagen capturada
width  = frame.shape[1]
height = frame.shape[0]

dsize = (width, height)

fondo = cv.resize(fondo,dsize)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    suma = cv.addWeighted(imagen, 0.7, fondo,0.3, 0)

    cv.imshow("Chapala", suma)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()