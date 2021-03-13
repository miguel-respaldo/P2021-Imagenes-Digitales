import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()
    # ret --> confirmacion de leer la camara
    # imagen --> los datos de imagen

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    flip = cv.flip(imagen, 1)
    # Usamos el filtro de Canny
    canny = cv.Canny(flip, 100, 200)

    cv.imshow("Camara", flip)
    cv.imshow("Canny", canny)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
