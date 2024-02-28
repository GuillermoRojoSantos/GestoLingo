import mediapipe as mp
import cv2
import os
import re
import pandas as pd
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
f_counter = 0

if not os.path.exists("../data/dataFrames/"):
    os.mkdir("../data/dataFrames/")

with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.2,
        min_tracking_confidence=0.9
) as hands:
    for lista in os.listdir("../data/words/"):
        df = pd.DataFrame(columns=["n_sample", "frame", "keypoints"])
        for sample in os.listdir(f"../data/words/{lista}/"):
            for image in os.listdir(f"../data/words/{lista}/{sample}/"):
                frame = cv2.imread(f"../data/words/{lista}/{sample}/{image}")

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(frame)
                left_hand = []
                right_hand = []

                if result.multi_hand_landmarks != None:
                    for hand_landmark in result.multi_hand_landmarks:

                        wrist_x = hand_landmark.landmark[0].x
                        # Comparar la coordenada x de la muñeca con un valor arbitrario para distinguir izquierda y derecha
                        if wrist_x > 0.5:
                            # Mano izquierda
                            left_hand = np.array([[res.x, res.y, res.z] for res in hand_landmark.landmark]).flatten()

                        else:
                            # Mano derecha
                            right_hand = np.array([[res.x, res.y, res.z] for res in hand_landmark.landmark]).flatten()

                    # si alguna mano está vacia, rellenar con 0
                    if len(left_hand) == 0:
                        left_hand = np.zeros(21 * 3)
                    elif len(right_hand) == 0:
                        right_hand = np.zeros((21 * 3))

                    res_hand_landmarks = np.concatenate([left_hand, right_hand])
                    # Agregar filas al DataFrame

                    df.loc[len(df.index)] = {"n_sample": int(re.findall("\d+", sample)[0]),
                                             "frame": int(re.findall("\d+", image)[0]) + 1,
                                             "keypoints": res_hand_landmarks}
                    df.loc[len(df.index)] = {"n_sample": int(re.findall("\d+", sample)[0]),
                                             "frame": f_counter,
                                             "keypoints": res_hand_landmarks}
                    f_counter += 1

                    print(df.head())
            f_counter = 0

df.to_hdf(f"../data/dataFrames/{lista}.h5", key="data", mode="w")
