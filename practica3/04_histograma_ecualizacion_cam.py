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

    src_gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    img_ecualizada = cv.equalizeHist(src_gray)

    cv.imshow("Gray", src_gray)

    cv.imshow("Gray_Equilizada", img_ecualizada)

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
