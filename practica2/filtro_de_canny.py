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

    # Usamos el filtro de Canny
    canny = cv.Canny(imagen, 100, 200)

    cv.imshow("Camara", canny)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
