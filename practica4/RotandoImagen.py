import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

ret, imagen = camara.read()

fondo = cv.imread("../tarea/chapala.webp")
# Redimencionamos el fondo al tamañano de la imagen capturada

width  = imagen.shape[1]
height = imagen.shape[0]

dsize = (width, height)

fondo = cv.resize(fondo,dsize)

while ret:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    Rotar = cv.rotate(imagen, cv.ROTATE_90_COUNTERCLOCKWISE, dst=None)

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    suma = cv.addWeighted(imagen, 0.9, fondo, 0.2, 0)
    cv.imshow("Chapala", suma)
    cv.imshow("Rotando", Rotar)
    
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()