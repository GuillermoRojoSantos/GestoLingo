import mediapipe as mp
import cv2
import os
import re
import pandas as pd
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
count=0

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.8
) as hands:
    for lista in os.listdir("../data/words/"):
        data = pd.DataFrame([])
        for sample in os.listdir(f"../data/words/{lista}/"):
            for image in os.listdir(f"../data/words/{lista}/{sample}/"):
                frame = cv2.imread(f"../data/words/{lista}/{sample}/{image}")

                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                result = hands.process(frame)
                # print(lista)
                # print(sample)
                # print(image)
                # print(result.multi_hand_landmarks)



                for hand_landmark in result.multi_hand_landmarks:
                    wrist_x = hand_landmark.landmark[0].x

                    # Comparar la coordenada x de la muñeca con un valor arbitrario para distinguir izquierda y derecha
                    if wrist_x > 0.5:
                        # Mano izquierda
                        print(lista,sample,image)
                        print("Mano derecha")
                    else:
                        # Mano derecha
                        print(lista,sample,image)
                        print("Mano izquierda")
                count+=1

print(count)
