import sys
import cv2 as cv
import numpy as np

# Numero de imagenes antes de detectar de nuevo la cara
MAX_DETECTAR_CARA = 20

def draw_rects(img, rects, color):
    for (x, y, w, h) in rects:
        #cv.rectangle(img, (x,y), (x+w,y+h), color, 2)
        cv.circle(img, (x+w//2, y+h//2), w//2, color, 2)

def detect_faces(img_gray, img_color):
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    # Draw the rectangle around each face
    draw_rects(img_color, faces, (255,0,0))


# Load the cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_nested  = cv.CascadeClassifier('haarcascade_eye.xml')

capture = cv.VideoCapture('/dev/video2')

if not capture.isOpened():
    print("No puedo abrir la camara", file=sys.stderr)
    exit(1)

# Leemos el primer frame de la imagen original
ret, img_original = capture.read()

if not ret:
    print("No puedo leer de la camara", file=sys.stderr)
    exit(2)

# Leemos el fondo
fondo = cv.imread("chapala.webp")

# Redimencionamos el fondo al tamañano de la imagen capturada
width  = img_original.shape[1]
height = img_original.shape[0]

fondo = cv.resize(fondo,(width, height))

# Inicializamos contador caras en max para que lo haga la primera vez
contador_caras = MAX_DETECTAR_CARA - 1

while ret:
    ret, img_original = capture.read()

    if not ret:
        print("No podemos leer de la camara (while)", file=sys.stderr)
        exit(3)

    # Convert to grayscale
    gray = cv.cvtColor(img_original, cv.COLOR_BGR2GRAY)

    #Crear mascara en ceros
    mascara = np.zeros(gray.shape, dtype = np.uint8)

    contador_caras = contador_caras + 1
    if contador_caras == MAX_DETECTAR_CARA:
        # Detect the faces
        new_faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        contador_caras = 0

    if len(new_faces) > 0:
        faces = new_faces

    for (x, y, w, h) in faces:
        #cv.rectangle(img, (x,y), (x+w,y+h), color, 2)
        #cv.circle(img_original, (x+w//2, y+h//2), w//2, (255,0,0), 2)
        cv.circle(mascara, (x+w//2, y+h//2), w//2-10, (255,0,0), cv.FILLED)


    #for (x, y, w, h) in faces:
        # Region of Interest = La cara
        #roi = gray[y:h, x:w]
        #eyes = face_nested.detectMultiScale(roi.copy(), 1.1, 4)
        #draw_rects(roi, eyes, (0,255,0))
        #cv.rectangle(img_original, (x, y), (x+w, y+h), (255, 0, 0), 2)


    # Usamos el filtro de Canny
    #filtro = cv.Canny(img_original, 100, 200)
    #filtro = cv.dilate(filtro, None)
    #mascara = mascara + filtro

    # Suabisamos la imagen
    #imagen = cv.blur(flip, (20,20))


    #cv.line(img_original, (width//2, 3*height//4), (width//2, height), (255,0,0), 5)

    # Bitwise-AND mask and original image
    #res = cv.bitwise_and(img_original,img_original, mask=mascara)

    #flip = cv.flip(img_original, 1)

    cv.imshow('Original', img_original)
    cv.imshow('Mask', mascara)
    #cv.imshow('Res', res)
    #cv.imshow('Filtro', filtro)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
    elif key == ord('s'):
         ret = cv.imwrite("test.png", img_original)
         if ret:
             print("La imagen se salvo corretamente")
         else:
            print("Error al salvar la imagen", file=sys.stderr)


cv.destroyAllWindows()
capture.release()
