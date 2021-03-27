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

    # Separar los canales en RGB
    b,g,r = cv.split(imagen)

    cv.imshow("Azul",b)
    cv.imshow("Verde",g)
    cv.imshow("Rojo",r)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()