import numpy as np
import cv2 as cv


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
    gray = cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
    corners= cv.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv.circle(imagen,(x,y),3,255,-1)
    cv.imshow("Camara", imagen)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()