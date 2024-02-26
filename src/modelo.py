# -- Importaciones de clases y variables del archivo 'constantes.py'

# Clase que permite construir modelos secuenciales, los cuales son modelos de redes neuronales, en los que las capas se apilan de forma secuencial unas sobre otras
from keras.models import Sequential     

# LSTM, son un tipo de capas recurrente que son útiles para aprender dependencias temporales en secuencias de datos
# Dense, capa densa que es la que se usa para producir la salida final de la red neuronal
from keras.layers import LSTM, Dense

from constantes import LENGTH_KEYPOINTS, MAX_LENGTH_FRAMES # Variebles constantes sacadas del archivo 'constantes.py'

NUM_EPOCH = 110 # Número de epochs para entrenar el modelo

# Función para la creación y entrenamiento del Modelo
def get_model(output_lenght: int):  # 'output_lenght' representa la longitud de la salida de la red neuronal

    model = Sequential()    # Crea el modelo secuencial de Keras

    # Se añade la capa de entrada, con función de activación 'ReLU', configurada para devolver sentencias 
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(MAX_LENGTH_FRAMES, LENGTH_KEYPOINTS)))

    # Capas intermedias
    # Capas LSTM, con 128 neuronas, con la función de activación 'ReLU', configurada para devolver sentencias
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    # Capas LSTM, con 128 neuronas, con la función de activación 'ReLU', configurada para NO devolver sentencias
    model.add(LSTM(128, return_sequences=False, activation='relu'))

    # Se añaden 4 capas densas conectadas con 64 neuronas, las 2 primeras, y 32 las dos ultimas, con la función de activación 'ReLU'
    model.add(Dense(64, activation='relu')) 
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))

    # Capa de salida, con el valor de 'output_lenght' como cantidad de neuronas, con la función de activación 'Softmax'
    model.add(Dense(output_lenght, activation='softmax'))

    # Se compila el modelo con el optimizador 'Adam', la función de perdida 'binary_crossentropy' y la métrica de precisión
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model