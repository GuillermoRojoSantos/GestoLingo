# -- Importación de librerias, módulos, funciones, variables y clases --
import os
#import pandas as pd
import cv2
import numpy as np
from mediapipe.python.solutions.holistic import Holistic

# Desactivación de la variable de entorno 'TF_ENABLE_ONEDNN_OPTS' por razones de compatibilidad y/o rendimiento
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Importación de funciones y variables de los archivos 'funciones.py' y 'constantes.py'
from funciones import create_folder, draw_keypoints, mediapipe_detection, save_frames, there_hand
from constantes import FONT, FONT_POS, FONT_SIZE, FRAME_ACTIONS_PATH, ROOT_PATH


# -- Función principal --

# Función de captura de muestras para una SOLA palabra, se recibe la ruta de guardado 
def capture_samples(path, margin_frame=2, min_cant_frames=5): 
    '''
        - Parametros de entrada de la función -
            - 'path' = ruta de la carpeta para la palabra 
            - 'margin_frame'= cuantos frames se ignoran al comiezo y al final de la captura  
            - 'min_cant_frames' cantidad de frames minimos para cada muestra
    '''

    create_folder(path) # Ejecuta la función para crear la carpeta en la ruta proporcionada

    
    cant_sample_exist = len(os.listdir(path))   # Se inicializa con la cantidad de muestras que ya existan en la ruta 'path'
    count_sample = 0                            # Servirá para contar el numero de muestras creadas/procesadas
    count_frame = 0                             # Se usará para contar el numero total de fotogramas procesados 
    frames = []                                 # Lista donde se almacenará los frames ya procesados
    
    # con 'with' nos aseguramos que cualquier recurso usado en el proceso, al acabar, quede limpiado correctamente al finalizar el proceso.
    # con 'as' se designa un objeto creado a una variable
    with Holistic() as holistic_model:
        # Se configura para que se use la cámara primera que haya conectada al PC que uses, modifica el 0 en función de la que vayas a usar(si tienes más de una)
        video = cv2.VideoCapture(0)     
        
        # Mientras el objeto de captura de video esté abierto, se ejecutará el siguiente código
        while video.isOpened():             
            frame = video.read()[1] # Se lee el frame que esté captando 'video'

            # Se procesa la imagen actual, guardando el frame con las detecciones superpuestas, 'image', y se almacena los resultados de la detección,  'results'
            image, results = mediapipe_detection(frame, holistic_model) 
            
            if there_hand(results):     # Comprobamos que se haya detectado alguna mano revisando los resultados del procesado anterior
                count_frame += 1        # De haberla, aumenta el contador de frames
                if count_frame > margin_frame:                                                      # Si el contador de frames supera a los frames de margen,
                    cv2.putText(image, 'Capturando...', FONT_POS, FONT, FONT_SIZE, (255, 50, 0))    # añadirá el frame actual al array de Frames guardados, 'frames',
                    frames.append(np.asarray(frame))                                                # mostrando el mensaje 'Capturando...'
                
            else:                                                                                           # De no detectar ninguna mano, comprobará si hay suficientes frames.
                if len(frames) > min_cant_frames + margin_frame:                                            # De haber más que el mínimo, más los del margen, 
                    frames = frames[:-margin_frame]                                                         # Se eliminaran una parte de los frames guardados (evitando solapamiento)
                    output_folder = os.path.join(path, f"sample_{cant_sample_exist + count_sample + 1}")    # Crea la ruta para el almacenamiento de los frames restantes
                    
                    create_folder(output_folder)            # Confirma si existe la carpeta, sino, la crea
                    save_frames(frames, output_folder)      # Almacena los frames restantes en la carpeta de la ruta que haya en 'output_folder'
                    count_sample += 1
                
                frames = []                                                                             # Una vez finalizada la captura de muestra, se resetean el array 'frames'
                count_frame = 0                                                                         # y la variable 'count_frame'
                cv2.putText(image, 'Listo para capturar...', FONT_POS, FONT, FONT_SIZE, (0,220, 100))   # Por pantalla, seguirá mostrando la cámara, y 
                
            
            draw_keypoints(image, results)  # Se dibujan los keypoints detectados en la imagen, mediante los resultados obtenidos por el modelo de detección

            cv2.imshow(f'Toma de muestras para "{os.path.basename(path)}"', image)  # Muestra la imagen actual en una ventana con el mensaje 'Toma de muestras para' + el archivo/ruta

            if cv2.waitKey(10) == 27:   # Se esperan 10 milisegundos. Si se pulsa la tecla Esc de tu teclado (en Windows)
                break                                                   # El programa se cierra

        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    word_name = "palabra"
    word_path = os.path.join(ROOT_PATH, FRAME_ACTIONS_PATH, word_name)
    capture_samples(word_path)
