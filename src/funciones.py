# -- Importaciones de módulos, librerias, constantes y funciones --

import os                       # Módulo que proporciona funciones para interactuar con el Sistema Operativo
import cv2                      # Libreria de OpenCV, usada en el procecsamiento de imagenes y videos en tiempo real
import numpy as np              # Libreria Numpy, usada para el manejo de matrices y operaciones matemáticas
import pandas as pd             # Libreria Pandas, usada para el análisis y la manipulación de datos estructurados
from typing import NamedTuple   # Clase 'NamedTuple', del módulo 'typing'. Sirve para definir el tipo de datos con nombre y atributos propios de Python

# Se importan las constantes 'FACEMESH_CONTOURS', 'POSE_CONNECTIONS', 'HAND_CONNECTIONS' del modulo 'holistic'. 
# Son usadas para definir puntos de referencia y las conexiones entre ellos para el seguimiento de la cara, pose y manos, respectivamente
from mediapipe.python.solutions.holistic import FACEMESH_CONTOURS, POSE_CONNECTIONS, HAND_CONNECTIONS

# Se importan las funciones 'draw_landmarks' y 'DrawingSpec' del módulo 'drawing_utils'.
# Son usadas para dibujar los puntos de referencia y las conexiones en las imágenes procesadas
from mediapipe.python.solutions.drawing_utils import draw_landmarks, DrawingSpec



def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convierte la imagen de formato BGR a formato RGB, ya que Mediapipe requiere este ultimo formato

    image.flags.writeable = False                   # Establece que la imagen sea solo de 'lectura', para evitar alteraciones cuando sean procesadas por Mediapipe
    results = model.process(image)                  # Se pasa la imagen procesada al modelo de Mediapipe para realizar la detección

    image.flags.writeable = True                    # Tras el proceso de detección, se vuelve a establecer la imagen para que sea de 'Escritura'
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Se vuelve a establecer el formato BRG a la imagen, el cuál es el formato usado por cv2
    return image, results                           # Devuelve la imagen procesada y los resultados de la detección

# Función que sirve para crear la carpeta que se especifica en la variable 'path', en caso de existir ya, esta función no hará nada
def create_folder(path):   
    if not os.path.exists(path):
        os.makedirs(path)

# Función que toma los resultados de 'mediapipe_detection()' y verifica que se haya detectado una mano en la imagen procesada
def there_hand(results: NamedTuple) -> bool:                            # Devolverá un booleano
    return results.left_hand_landmarks or results.right_hand_landmarks  # Con esto indica que si se ha detectado una mano, ya sea la izquierda o la derecha, devolverá True

# Función que busca en la ruta especificada un archivo '.h5', devuelve una lista de los archivos que sean de ese formato
def get_actions(path):
    out = []                                    
    for action in os.listdir(path):             # Se itera sobre los archivos que hay en ese directorio, cuya ruta está almacenada en 'path'
        name, ext = os.path.splitext(action)    # Con 'os.path.splitext(action)' separa el nombre del archivo(name) y la extensión del mismo(ext)
        if ext == ".h5":                        
            out.append(name)            
    return out


# -- Funciones de captura de imagen --

# Función para configurar la resolución de la cámara, usando OpenCV
def configurar_resolucion(camara):                  # 'camara' es el objeto de captura de la cámara
    camara.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)      # Configura el ancho
    camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)      # Configura el alto

# Función encargada de dibujar los keypoins de las landmarks detectadas.
def draw_keypoints(image, results):
    # En este caso, dibuja los keypoints de los landmarks de la cara, 'face_landmarks'
    draw_landmarks(                                                         
        image,
        results.face_landmarks,
        FACEMESH_CONTOURS,                                                  # Se usa 'FACEMESH_CONTOURS' para indicar que landmarks deben dibujarse
        DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),     # Con los 'DrawingSpec()' se especifica el color, el grosor y el radio de los circulos 
        DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1),    # que representan a los keypoints
    )

    # En este caso, dibuja los keypoints de los landmarks de la pose, 'pose_landmarks'
    draw_landmarks(                                                         
        image,
        results.pose_landmarks,
        POSE_CONNECTIONS,
        DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
        DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2),
    )

    # En este caso, dibuja los keypoints de los landmarks de la mano izquierda, 'left_hand_landmarks'
    draw_landmarks(                                                         
        image,
        results.left_hand_landmarks,
        HAND_CONNECTIONS,
        DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
        DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2),
    )

    # En este caso, dibuja los keypoints de los landmarks de la mano derecha, 'right_hand_landmarks'
    draw_landmarks(                                                         
        image,
        results.right_hand_landmarks,
        HAND_CONNECTIONS,
        DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
        DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
    )

# Función para guardar los frames en el directorio de salida especificado, 'output_folder'
def save_frames(frames, output_folder):
    for num_frame, frame in enumerate(frames):                           # Se itera sobre cada frame en la lista de frames, 'frames', con 'enumerate()', obteniendo su indice y frame
        
        frame_path = os.path.join(output_folder, f"{num_frame + 1}.jpg") # Se construye una ruta completa para el frame actual mediante 'os.path.join()'

        cv2.imwrite(frame_path, cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)) # Guarda el frame como un archivo, sin antes convertirlo a BGRA para que cumpla con el formato establecido


# -- Creación de Keypoints -- 

# Función que recoge los resultados almacenados, de los que extrae las coordenadas de los keypoints(de la cara, pose y manos) si están disponibles, 
# concatena estas coordenadas en un único vector y lo devuelve
def extract_keypoints(results):
    # Se extraen las coordenadas x,y,z y la visibilidad de los keypoints de la pose, cada conjunto se almacena en un array de 1 dimensión, en caso de haber disponibles.

    # De no haber keypoints almecenados en 'results', se crea un array de ceros, con la forma correspondiente(33 keypoints * 4 valores en este caso) en su lugar
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    # Lo mismo, pero con los keypoints de la cara
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)

    # Lo mismo, pero con los keypoints de la mano izquierda
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)

    # Lo mismo, pero con los keypoints de la mano derecha
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)

    return np.concatenate([pose, face, lh, rh]) # Se concatenan todos los arrays de coordenadas en un solo vector y se devuelve este último como resultado de la función

# Función mediante la que se extraen y concatenan los keypoints de cada imagen en una secuencia de keypoints.
def get_keypoints(model, path):
    kp_seq = np.array([])                               # Inicializa un array para almacenar la secuencia de keypoints
    for img_name in os.listdir(path):                       
        img_path = os.path.join(path, img_name)         # Se obtiene el nombre de la ruta completa

        frame = cv2.imread(img_path)                    # Se lee la imagen y se almacena en 'frame'
        _, results = mediapipe_detection(frame, model)  # Medainte la función 'mediapipe_detection()' se obtienen los resultados de la detección de keypoints
        
        kp_frame = extract_keypoints(results)           # Se extraen los keypoints de la pose, cara y las manos de la imagen actual
        
        # Se agregan los keypoints actuales, si ya habia almacenados anteriormente, se concatenan, sino habia nada antes, se crear una nueva matriz con 'kp_frame'
        kp_seq = np.concatenate([kp_seq, [kp_frame]] if kp_seq.size > 0 else [[kp_frame]])

    return kp_seq   # Se devuelve una secuencia de keypoints que contiene los keypoints de todas las imagenes procesadas

# Función que almacena los keypoints de la muestra en un DataFrame y devuelve ese mismo DataFrame con los keypoints de la muestra añadidos
def insert_keypoints_sequence(df, n_sample: int, kp_seq):
    for frame, keypoints in enumerate(kp_seq):
        data = {'sample': n_sample, 'frame': frame + 1,'keypoints': [keypoints]}
        df_keypoints = pd.DataFrame(data)
        df = pd.concat([df, df_keypoints])
    return df 


# -- Entrenamiento del Modelo

# Función que toma una lista de acciones y la ruta donde están los datos, devuelve las secuencias de keypoints y las etiquetas, para el posterior entrenamiento del modelo
def get_sequences_and_labels(actions, data_path):
    sequences, labels = [], []
    
    for label, action in enumerate(actions):
        hdf_path = os.path.join(data_path, f"{action}.h5")  # Construye una ruta completa al archivo que contiene los datos para la acción actual
        data = pd.read_hdf(hdf_path, key='data')            # Lee los datos de ese archivo, mediante pandas y se almacenan en el dataframe 'data'
        
        for _, data_filtered in data.groupby('sample'):     #Itera sobre cada grupo de datos filtrados por la columna 'sample', en el DataFrame 'data'
            sequences.append([fila['keypoints'] for _, fila in data_filtered.iterrows()])   # Se almacenan los keypoints a una lista de secuencias. A su vez, hay creada una lista de listas, 
                                                                                            # donde cada sublista es sobre cada secuencia de keypoints
            labels.append(label)
            
    return sequences, labels


# --Evaluación--

# Función que guarda el contenido proporcionado en un archivo de texto
def save_txt(file_name, content):
    # 'with' garantiza que el archivo se cerrará una vez terminado el bloque de código 
    with open(file_name, 'w') as archivo:   # Se abre el archivo, en formato de lectura 'w'. De no existir, se crea el archivo. 
        archivo.write(content)              # Se escribe en el archivo el contenido de la variale 'content'

# Función para el formateo de oraciones procedentes de una lista de oraciones
def format_sentences(sent, sentence, repe_sent):
    if len(sentence) > 1:                           # Comprueba que haya oraciones en la lista
        if sent in sentence[1]:                     # Comprueba si la oración actual, 'sent', es la que está en la 2º posición, verificando que coincida con la siguiente
            repe_sent += 1
            sentence.pop(0)                         # Elimina el 1º elemento para ir avanzando en la lista
            sentence[0] = f"{sent} (x{repe_sent})"  # Se modifica el 1º elemento de la lista para incluir el contador de repeticiones de 'sent'
        else:                                       
            repe_sent = 1                           # En caso de que no se cumpla 'sent in sentence[1]', implicando que es una nueva oración, el cont de repeticiones se reestablece
    return sentence, repe_sent
