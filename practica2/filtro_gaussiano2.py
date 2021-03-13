import cv2 as cv

def main():
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

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

        imagen1 = cv.GaussianBlur(imagen, (3, 3), 0)

        cv.imshow('normal', imagen)
        cv.imshow(window_name, imagen1)

        if cv.waitKey(1) == 27:
            break

    camara.release()
    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":
    main()