import sys
import cv2 as cv

def main():
    # [variables]
    # Declare the variables we are going to use
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace Demo"
    # [variables]
    # [load]

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

        # [reduce_noise]
        # Remove noise by blurring with a Gaussian filter
        imagen = cv.GaussianBlur(imagen, (3, 3), 0)
        # [reduce_noise]

        # [convert_to_gray]
        # Convert the image to grayscale
        src_gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        # [convert_to_gray]

        # Create Window
        cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

        # [laplacian]
        # Apply Laplace function
        dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
        # [laplacian]

        # [convert]
        # converting back to uint8
        abs_dst = cv.convertScaleAbs(dst)
        # [convert]

        # [display]
        cv.imshow(window_name, abs_dst)
        # [display]

        if cv.waitKey(1) == 27:
            break

    camara.release()
    cv.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()