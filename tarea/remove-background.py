import cv2 as cv

#backSub = cv.createBackgroundSubtractorMOG2()
backSub = cv.createBackgroundSubtractorKNN()

#capture = cv.VideoCapture("/dev/video2")
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("No puedo abrir la camara")
    exit(1)

fondo = cv.imread("chapala.webp")

ret, frame = capture.read()

# Redimencionamos el fondo al tamañano de la imagen capturada
width  = frame.shape[1]
height = frame.shape[0]

dsize = (width, height)

fondo = cv.resize(fondo,dsize)

while ret:
    ret, frame = capture.read()

    if frame is None:
        break

    frame = cv.flip(frame,1)
    frame = cv.GaussianBlur(frame, (3, 3), 0)

    fgMask = backSub.apply(frame)

    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break