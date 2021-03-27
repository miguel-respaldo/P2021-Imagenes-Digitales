import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    #Separar los canales en RGB
    b,g,r = cv.split(imagen)

    #Crear mascara en ceros
    zeros = np.zeros(r.shape, dtype = np.uint8)

    Rojo = cv.merge((zeros, zeros, r))
    Verde = cv.merge((zeros, g, zeros))
    Azul = cv.merge((b, zeros, zeros))

    cv.imshow("Camara", imagen)
    cv.imshow("Rojo", Rojo)
    cv.imshow("Verde", Verde)
    cv.imshow("Azul", Azul)

    if cv.waitKey(1) == 27:
        break

print(imagen.shape, r.shape, g.shape, b.shape,)
camara.release()
cv.destroyAllWindows()
