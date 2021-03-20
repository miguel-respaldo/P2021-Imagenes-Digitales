import cv2 as cv
import numpy as np

#backSub = cv.createBackgroundSubtractorMOG2()
#backSub = cv.createBackgroundSubtractorKNN()

# Parameters
blur = 21
canny_low = 15
canny_high = 150
min_area = 0.0005
max_area = 0.95
dilate_iter = 10
erode_iter = 10
mask_color = (0.0,0.0,0.0)

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("No puedo abrir la camara")
    exit(1)

fondo = cv.imread("chapala.webp")

ret, frame = capture.read()

if frame is None:
    exit()

# Redimencionamos el fondo al tamañano de la imagen capturada
width  = frame.shape[1]
height = frame.shape[0]

dsize = (width, height)

fondo = cv.resize(fondo,dsize)

while ret:
    ret, frame = capture.read()

    if ret != True:        # Convert image to grayscale
        break

    # Volteamos la imagen para que se vea como espejo
    frame = cv.flip(frame, 1)

    image_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)        # Apply Canny Edge Dection
    edges = cv.Canny(image_gray, canny_low, canny_high)

    edges = cv.dilate(edges, None)
    edges = cv.erode(edges, None)

    contour_info = [(c, cv.contourArea(c),) for c in cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)[1]]

    # Get the area of the image as a comparison
    image_area = frame.shape[0] * frame.shape[1]

    # calculate max and min areas in terms of pixels
    max_area = max_area * image_area
    min_area = min_area * image_area

    # Set up mask with a matrix of 0's
    mask = np.zeros(edges.shape, dtype = np.uint8)

    cv.imshow('Original', frame)
    cv.imshow('Procesada', edges)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

# Release the VideoCapture object
# Shut down
cv.destroyAllWindows()
capture.release()