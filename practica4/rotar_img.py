import cv2 as cv
import numpy as np


camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

angle=60
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

    image_center = tuple(np.array(imagen.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    imagen_rotada = cv.warpAffine(imagen, rot_mat, imagen.shape[1::-1], flags=cv.INTER_LINEAR)


    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    suma = cv.addWeighted(imagen_rotada, 0.7, fondo,0.3, 0)

    cv.imshow("Chapala", suma)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()