# Importación de librerias
import cv2
import os   # Esta libreria es para poder crear carpetas en Windows 

# Importamos la clase 
import seguimiento_manos as sm

# Indicamos que letra vamos a escanear
while True:
    letra = input('Introduce la letra a captar: ').strip().upper()
    if len(letra)==1 and letra.isalpha() and 'A'<=letra<='Z':
        break
    else:
        print('Solo una sola letra en mayusculas del alfabeto Castellano')
nombre = f'Letra_{letra}'
path='data'
carpeta=path+'/'+nombre


# Si no está creada la carpeta de esa letra, se crea
if not os.path.exists(carpeta):
    print('Carpeta creada ', carpeta)
    os.makedirs(carpeta) # Se crea la carpeta

# Lectura de la cámara
cap = cv2.VideoCapture(0)  # Hay que modificar este valor, el 0, en funcion de cuantas cámaras tengas en el equipo

# Establecemos la resolución
cap.set(3, 1280)
cap.set(4, 720)

# Inicializamos el contador para más adelante
cont=0

# Declaramos al detector
detector = sm.detectormanos(Confdeteccion=0.9)

# Realizamos la lectura de la cap
while True:
    ret, frame = cap.read()

    # Vamos a extraer información de la mano
    frame = detector.encontrarmanos(frame, dibujar=False)   # Al ponerno en False, no se veran las lineas y puntos en tu mano

    # Extraemos la posición de una sola mano
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color_=[0,255,0]) # lista 1, la caja alrededor de la mano, y la mano en cuestión
    
    # Si pilla la mano que queremos, le extraeremos los pixeles que conforman esa mano que realizan la seña que queremos detectar.
    if mano == 1:
        # Extramos la info del recuadro que la rodea
        xmin, ymin, xmax, ymax = bbox

        # Vamos a darle un margen al rectangulo, ya que, sin él, el recuadro que capta la mano, deja fuera las puntas de varios dedos
        xmin = xmin-50 # Es -40 debido a que estamos hablando del lado izquierdo en el eje X, es decir, que se posicione aún más a la izq
        ymin = ymin-50

        xmax = xmax+50    # Ahora hablamos del lado positivo del eje, así que, a mayor sea esta variable, más a la derecha se irá
        ymax = ymax+50

        # Realizamos un recorte de la mano (una instantanea/captura de imagen)
        recorte = frame[ymin:ymax, xmin:xmax]

        # Con esto podremos ver que hemos capturado(se debe de generar una segunda ventana que muestre lo que hay en el recuadro)
        cv2.imshow('Captura', recorte)      

        # Redimensionamiento de la imshow() del recorte(establecemso que sea 640x640 pixeles fijos y que interpolacion usa)
        # recorte = cv2.resize(recorte, (640,640), interpolation=cv2.INTER_CUBIC)  # Este paso puede desactivarse en función de lo que veamos

        # Almacenar nuestras imagenes
        ima_letra = '/'+letra
        cv2.imwrite(carpeta + ima_letra +"_{}.jpg".format(cont), recorte) # Este método permite guardar la imagen que haya en 'recorte'
            #(direccion+nombre_archivo(la vez que sea), la imagen/recorte a almacenar)

        # Cada vez que guardemos una imagen, se aumenta el contador 'cont'
        cont = cont+1
        
        # cv2.rectangle(frame,(xmin, ymin),(xmax,ymax),[0,255,0], 2) # Con este recuadro es con el que sacaremos los datos que usaremos en el entrenamiento
    
    # Mostramos los FPSs
    cv2.imshow('Detector de signos',frame)

    t = cv2.waitKey(1) # Leemos nuestro teclado, con un delay de 1 segundo
    if t == 27 or cont==100: # la tecla 27 es Esc, para cerrar la cámara | limitamos a que sean 100 imagenes
        break

cap.release()
cv2.destroyAllWindows()