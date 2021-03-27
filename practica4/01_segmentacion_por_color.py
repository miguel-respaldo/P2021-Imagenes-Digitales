import cv2 as cv
import numpy as np

camara = cv.VideoCapture('/dev/video2')

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:

    # Take each frame
    ret, frame = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

camara.release()
cv.destroyAllWindows()