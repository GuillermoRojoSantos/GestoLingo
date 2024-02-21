# Para mayor organización y limpieza de código, las constantes han sido almacenadas en este archivo para su posterior importación

# -- Importación de Modulos y librerias --
import os
import cv2

# -- Rutas --

ROOT_PATH = os.getcwd()     # Ruta del directorio de trabajo actual y la cuál será la base desde las que obtendran el resto, obtenida mediante 'os.getcwd()'. 
FRAME_ACTIONS_PATH = os.path.join(ROOT_PATH, "frame_actions")   # Ruta que se usa para almacenar acciones en forma de fotogramas(frames)
DATA_PATH = os.path.join(ROOT_PATH, "data")                     # Ruta que se usará para almacenar los datos usados por la app.
MODELS_PATH = os.path.join(ROOT_PATH, "models")                 # Ruta usada para almacenar los modelos o archivos de configuración de modelos usados en la app

# -- Variables -- 
MAX_LENGTH_FRAMES = 15      # Longitud máxima de frames que se usaran para cada secuencia de acciones.
LENGTH_KEYPOINTS = 1662     # Variable que especifica el num total de caracteristicas que se extraerán de cada frame.
MIN_LENGTH_FRAMES = 5       # Longitud mínima de frames que se usaran para cada secuencia de acciones.
MODEL_NAME = f"actions_{MAX_LENGTH_FRAMES}.keras"   # Se define el nombre del modelo que se usará para el reconocimiento de acciones, reflejando MAX_LENGTH_FRAMES en el entrenamiento


# -- Parametros de imagen --
FONT = cv2.FONT_HERSHEY_PLAIN   # Tipo de fuente se usara para renderizar el texto en las imagenes.
FONT_SIZE = 1.5                 # Tamaño de la fuente que se usarña al momento de renderizar el texto en las imagenes
FONT_POS = (5, 30)              # Posición, (x,y), en la que se colocará el texto en la imagen.