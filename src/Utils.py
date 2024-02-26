import cv2
from typing import NamedTuple
from mediapipe.python.solutions.holistic import HAND_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks, DrawingSpec


def draw_hand_keypoints(hk_frame, pred):
    # Dibuja los keyoints en las manos usando las predicciones del modelo Holistic de Mediapipe
    # Izquierda
    draw_landmarks(hk_frame, pred.left_hand_mark, HAND_CONNECTIONS,
                   DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=1))

    # Derecha
    draw_landmarks(hk_frame, pred.right_hand_landmarks, HAND_CONNECTIONS,
                   DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4))

def holistic_detection(hd_frame, model):
    image = cv2.cvtColor(hd_frame, cv2.COLOR_BGR2RGB)

    # Establece que la imagen sea solo de 'lectura', para evitar alteraciones cuando sean procesadas por Mediapipe
    image.flags.writeable = False

    # Se pasa la imagen procesada al modelo de Mediapipe para realizar la detección
    results = model.process(image)

    # Tras el proceso de detección, se vuelve a establecer la imagen para que sea de 'Escritura'
    image.flags.writeable = True

    # Se vuelve a establecer el formato BRG a la imagen, el cuál es el formato usado por cv2
    image_r = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image_r, results

def there_hand(results: NamedTuple) -> bool:                            # Devolverá un booleano
    return results.left_hand_landmarks or results.right_hand_landmarks  # Con esto indica que si se ha detectado una mano, ya sea la izquierda o la derecha, devolverá True