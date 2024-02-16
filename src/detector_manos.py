# Importación de librerias
import cv2
import os   # Esta libreria es para poder crear carpetas en Windows 

# Importamos la clase 
import seguimiento_manos as sm

# Creamos la carpeta de la vocal A
nombre = 'Letra_A'
path='data'
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

    # Vamos a extraer información de la mano
    frame = detector.encontrarmanos(frame, dibujar=False)   # Al ponerno en False, no se veran las lineas y puntos en tu mano

    # Extraemos la posición de una sola mano
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=True, color_=[0,255,0] # lista 1, la caja alrededor de la mano, y la mano en cuestión
    
    # Si pilla la mano que queremos
    if mano == 

    # Mostramos los FPSs
    cv2.imshow('Detector de signos',frame)

    t = cv2.waitKey(1) # Leemos nuestro teclado, con un delay de 1 segundo
    if t == 27: # la tecla 27 es Esc, para cerrar la cámara 
        break

cap.release()
cv2.destroyAllWindows()