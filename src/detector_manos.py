# Importación de librerias
import cv2
import os   # Esta libreria es para poder crear carpetas en Windows 

# Importamos la clase 
import seguimiento_manos as sm

# Creamos la carpeta de la vocal A
nombre = 'Letra_A'
path='pruebaGestoLingo/data'
carpeta=path+'/'+nombre


# Si no está creada, se crea
if not os.path.exists(carpeta):
    print('Carpeta creada ', carpeta)
    os.makedirs(carpeta) # Se crea la carpeta

# Lectura de la cámara
cap = cv2.VideoCapture(0)

# Establecemos la resolución
cap.set(3, 1280)
cap.set(4, 720)

# Declaramos al detector
detector = sm.detectormanos(Confdeteccion=0.9)

# Realizamos la lectura de la cap
while True:
    ret, frame = cap.read()

    # Mostramos los FPSs
    cv2.imshow('Detector de signos',frame)

    t = cv2.waitKey(1) # Leemos nuestro teclado, con un delay de 1 segundo
    if t == 27: # la tecla 27 es Esc, para cerrar la cámara 
        break

cap.release()
cv2.destroyAllWindows()