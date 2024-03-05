import cv2
import mediapipe as mp
from tensorflow import keras
import numpy as np
import streamlit as st
import os

st.title("Webcam Live Feed")

cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()
stop_button_pressed = st.button("stop")
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
model:keras.Sequential = keras.models.load_model("../data/model/GestoLingo.keras")

keypoints = []
frame_count = 0
words = [x[0:-11] for x in os.listdir("../data/treatedDF/")]
model_prediction_idx = None
hold_model_result = st.empty()
hold_model_result.write("Esperando")
with mp.solutions.hands.Hands(
        # Parametro para especificar la complejidad del modelo usado en la detección de las manos
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.6
) as mp_hands:
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = mp_hands.process(frame)
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        left_hand = []
        right_hand = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                wrist_x = hand_landmarks.landmark[0].x
                # Comparar la coordenada x de la muñeca con un valor arbitrario para distinguir izquierda y derecha

                if wrist_x > 0.5:
                    left_hand = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten()
                else:
                    right_hand = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten()

        if len(left_hand) == 0:
            left_hand = np.zeros(21 * 3)
        if len(right_hand) == 0:
            right_hand = np.zeros((21 * 3))
        keypoints.append(np.concatenate([left_hand, right_hand]))

        # Check if we have enough data in keypoints (len>60) and of there's a hand detected
        if len(keypoints) > 30 and (np.all(left_hand!=0) or np.all(right_hand!=0)):
            frame_count+=1
        else:
            # check if we have enough frames
            if frame_count >=10:
                # Take the last 60 keypoint record
                # Keypoint is a 1 dim array like (,60) and we need (at least) (1,60)
                model_prediction = model.predict(np.expand_dims(keypoints[-30:],axis=0))
                model_prediction_idx = np.argmax(model_prediction)
                print(words[model_prediction_idx])
                hold_model_result.write(words[model_prediction_idx])
                frame_count=0
                keypoints=[]
                print("keypoints",len(keypoints))
        frame_placeholder.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")
        if stop_button_pressed:
            break