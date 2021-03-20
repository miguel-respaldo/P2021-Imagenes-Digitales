import cv2 as cv

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

#capture = cv.VideoCapture("/dev/video2")
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

    # Volteamos la imagen para que se vea como espejo
    frame = cv.flip(frame, 1)

    if ret == True:        # Convert image to grayscale
        image_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)        # Apply Canny Edge Dection
        edges = cv.Canny(image_gray, canny_low, canny_high)

   cv.imshow('Original', frame)
   cv.imshow('Procesada', edges)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
