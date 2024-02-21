# Importación de librerias
import math
import cv2
import mediapipe as mp        # Libreria que contiene el detector de Manos, gracias a la cual sacaremos la información de la mano
import time

# Creamos la clase
class detectormanos():
    def __init__(self, mode=False, maxManos=2, model_complexity=1, Confdeteccion=0.5, Confsegui=0.5):   # Método constructor
        self.mode = mode                        # Parametro para indicar si se aplica o no el modo de seguimiento de manos, de base.
        self.maxManos = maxManos                
        self.compl = model_complexity           # Parametro para especificar la complejidad del modelo usado en la detección de las manos
        self.Confdeteccion = Confdeteccion      # Umbral de confianza mínimo para la detección de las manos
        self.Confsegui = Confsegui              # Umbral de confianza mínimo para el seguimiento de las manos

        # Creamos los objetos que detectarán las manos y las dibujaran
        self.mpmanos = mp.solutions.hands       # módulo que contiene la funcionabilidad para detectar las manos (libreria mediapipe)
        self.manos = self.mpmanos.Hands(self.mode, self.maxManos, self.compl, self.Confdeteccion, self.Confsegui)   # objeto que se usará para detectar las manos en las imagenes procesadas
        self.dibujo = mp.solutions.drawing_utils    # Con este modulo, se nos proporciona utiles para dibujar sobre imagenes
        self.tip = [4,8,12,16,20]               # Estos numeros son los indices de los puntos de referencia de la punta de los dedos en una mano que haya sido detectada
                                                # Se usan para identificar los dedos

    # Función para encontrar las manos
    def encontrarmanos(self, frame, dibujar = True):
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # Transforma el marco de BRG a RGB, debido a que Mediapipe lo requiere así
        self.resultados = self.manos.process(imgcolor)      # Se procesa la imagen , mediante self.manos, y se detectan las manos en ella.  

        if self.resultados.multi_hand_landmarks:                # Se verifican si se detectaron manos en la imagen.
            for mano in self.resultados.multi_hand_landmarks:   # Se itera por cada mano detectada | self.resultados.multi_hand_landmarks es una lista que contiene los puntos caracteristicos de cada mano detectada
                if dibujar:                                     
                    self.dibujo.draw_landmarks(frame, mano, self.mpmanos.HAND_CONNECTIONS)  # Dibujamos las conexiones de los puntos
        return frame
    
    # Función para encontrar la posición
    def encontrarposicion(self, frame, ManoNum = 0, dibujarPuntos = True, dibujarBox=True, color_ = []):
        xlista = []
        ylista = []
        bbox = []
        player = 0
        self.lista = []
        if self.resultados.multi_hand_landmarks:
            miMano = self.resultados.multi_hand_landmarks[ManoNum]
            prueba = self.resultados.multi_hand_landmarks
            player = len(prueba)
            for id, lm in enumerate(miMano.landmark):
                alto, ancho, c = frame.shape  # Extraemos las dimensiones de los fps
                cx, cy = int(lm.x * ancho), int(lm.y * alto)  # Convertimos la informacion en pixeles
                xlista.append(cx)
                ylista.append(cy)
                self.lista.append([id, cx, cy])
                if dibujarPuntos:
                    cv2.circle(frame,(cx, cy), 3, (0, 0, 0), cv2.FILLED)  # Dibujamos un circulo

            xmin, xmax = min(xlista), max(xlista)
            ymin, ymax = min(ylista), max(ylista)
            bbox = xmin, ymin, xmax, ymax
            if dibujarBox:
                # Dibujamos cuadro
                cv2.rectangle(frame,(xmin - 20, ymin - 20), (xmax + 20, ymax + 20), color_,2)
        return self.lista, bbox, player
    
    # Función para detectar y dibujar los dedos arriba
    def dedosarriba(self):
        dedos = []
        if self.lista[self.tip[0]][1] > self.lista[self.tip[0]-1][1]:
            dedos.append(1)
        else:
            dedos.append(0)

        for id in range(1,5):
            if self.lista[self.tip[id]][2] < self. lista[self.tip[id]-2][2]:
                dedos.append(1)
            else:
                dedos.append(0)

        return dedos
    
    # Función para detectar la distancia que hay entre los dedos
    def distancia(self, p1, p2, frame, dibujar=True, r=15, t=3):
        x1,y1 = self.lista[p1][1:]
        x2,y2 = self.lista[p2][1:]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        if dibujar:
            cv2.line(frame, (x1,y1), (x2,y2), (0,0,255),t)
            cv2.circle(frame,(x1,y1),r,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),r,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(cx,cy),r,(0,0,255),cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        return length, frame, [x1,y1,x2,y2,cx,cy]
    
    # Función principal
    def main():
        ptiempo=0
        ctiempo=0

        cap = cv2.VideoCapture(0) # Leemos la camara web

        detector = detectormanos()  # Creamos el objeto de la clase

        # Realizamos la detección de las manos
        while True:
            ret, frame = cap.read()

            frame = detector.encontrarmanos(frame) # Una vez que se obtenga la imagen, la enviamos

            lista, bbox = detector.encontrarposicion(frame)

            # Mostramos los fps
            ctiempo = time.time()
            fps = 1/(ctiempo-ptiempo)
            ptiempo = ctiempo

            cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

            cv2.imshow('Manos',frame)
            k = cv2.waitKey()

            if k==27:
                break
        
        cap.release()

        cv2.destroyAllWindows()