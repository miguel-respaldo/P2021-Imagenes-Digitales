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

        imagen = cv.GaussianBlur(imagen, (3, 3), 0)

        gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)

        grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        # Gradient-Y
        # grad_y = cv.Scharr(gray,ddepth,0,1)
        grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        cv.imshow(window_name, grad)
        cv.imshow("sovel x", abs_grad_x)
        cv.imshow("sovel y", abs_grad_y)

        if cv.waitKey(1) == 27:
            break

    camara.release()
    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":
    main()