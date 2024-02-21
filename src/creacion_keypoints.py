# -- Importación de librerias y módulos
import os

# Desactivación de la variable de entorno 'TF_ENABLE_ONEDNN_OPTS' por razones de compatibilidad y/o rendimiento
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import warnings # Módulo de Python que sirve para escribir un código más limpio, seguro y libre de potenciales problemas

import pandas as pd
from mediapipe.python.solutions.holistic import Holistic

# Funciones y variables procedentes de los archivos 'funciones' y 'constantes'
from funciones import get_keypoints, insert_keypoints_sequence
from constantes import DATA_PATH, FRAME_ACTIONS_PATH, ROOT_PATH

# Función que recorre la carpeta donde están los frames guardados y guarda sus keypoints en la ruta 'save_path'
def create_keypoints(frames_path, save_path):
    data = pd.DataFrame([])     # Se crea un DataFrame donde se almacenarán los keypoints
    
    with Holistic() as model_holistic:
        # Se itera cada elemento de la ruta 'frames_path'
        for n_sample, sample_name in enumerate(os.listdir(frames_path), 1):     # n_sample = indice de la muestra 
            sample_path = os.path.join(frames_path, sample_name)                # se crea la ruta para guardar las muestras
            keypoints_sequence = get_keypoints(model_holistic, sample_path)     # mediante la función 'get_keypoints()' se obtienen las secuencias de keypoints para la muestra actual
            data = insert_keypoints_sequence(data, n_sample, keypoints_sequence)    # Se guardan las keypoints obtenidas junto al indice de muestra

    data.to_hdf(save_path, key="data", mode="w") # Se guarda el DataFrame 'data' en un archivo HDF5 en la ruta 'save_path', bajo la clave 'data' y en modo escritura(mode='w')

if __name__ == "__main__":
    words_path = os.path.join(ROOT_PATH, FRAME_ACTIONS_PATH) # Se establece la ruta donde se guardan las muestras de palabras
    
    with warnings.catch_warnings():                                 # esto se hace para capturar advertencias
        warnings.simplefilter("ignore")                             # esto sirve para ignorar las advertencias que se generen dentro del bloque de código que sigue
        # GENERAR LOS KEYPOINTS DE TODAS LAS PALABRAS
        for word_name in os.listdir(words_path):                    
            word_path = os.path.join(words_path, word_name)        
            hdf_path = os.path.join(DATA_PATH, f"{word_name}.h5")
            print(f'Creando keypoints de "{word_name}"...')
            create_keypoints(word_path, hdf_path)
            print(f"Keypoints creados!")
            
        # GENERAR SOLO DE UNA PALABRA
        # word_name = "hola"
        # word_path = os.path.join(words_path, word_name)
        # hdf_path = os.path.join(data_path, f"{word_name}.h5")
        # create_keypoints(word_path, hdf_path)
        # print(f"Keypoints creados!")