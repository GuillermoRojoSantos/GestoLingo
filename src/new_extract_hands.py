import time

import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2
from mediapipe.python import solutions
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import os
import re

# Mediapipe code
# BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
# HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
# HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
# VisionRunningMode = mp.tasks.vision.RunningMode
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
baseOptions = mp.tasks.BaseOptions(model_asset_path='../data/model/hand_landmarker.task')
def get_result(result: mp.tasks.vision.HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    return result
hloptions = mp.tasks.vision.HandLandmarkerOptions(
    base_options=baseOptions,
    running_mode=mp.tasks.vision.RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.3,  # lower than value to get predictions more often
    min_hand_presence_confidence=0.1,  # lower than value to get predictions more often
    min_tracking_confidence=0.3,  # lower than value to get predictions more often
    # result_callback=get_result
)

ima_cont = 0
sample_var = "sample_00"

# Words' folders creation
word = input('Ingrese la palabra a aprender: ')
folder = f"../data/words/{word}/"

if not os.path.exists("../data/"):
    os.mkdir("../data/")
if not os.path.exists("../data/words/"):
    os.mkdir("../data/words/")

if not os.path.exists(folder):
    print('Carpeta creada ', folder)
    os.makedirs(folder)

# Una carpeta de muestra se va a llamar sample_n
dirs = os.listdir(folder)
if len(dirs) > 0:
    toma_cont = int(re.findall("\d+",dirs[-1])[0])+1
else:
    toma_cont = 0

# Camera capture object's initialization
cap = cv2.VideoCapture(0)
# Resolution's configuration (1280x720)
cap.set(3,1280)
cap.set(4,720)

with HandLandmarker.create_from_options(hloptions) as landmarker:
    while True:
        _,frame = cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) if cap.get(cv2.CAP_PROP_POS_MSEC) != None else 0
        result = landmarker.detect_for_video(mp_image,int(timestamp))
        frame_c = frame.copy()

        hand_landmarks_list = result.hand_landmarks
        handedness_list = result.handedness
        if result.hand_landmarks:
            if not os.path.exists(f"{folder}/{sample_var}{toma_cont}/"):
                os.mkdir(f"{folder}/{sample_var}{toma_cont}/")
                print(f" Carpeta {folder}/{sample_var}{toma_cont}/ creada")
        # Loop through the detected hands to visualize.
            for idx in range(len(hand_landmarks_list)):
                hand_landmarks = hand_landmarks_list[idx]
                handedness = handedness_list[idx]

                # Draw the hand landmarks.
                hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
                hand_landmarks_proto.landmark.extend([
                    landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
                ])
                solutions.drawing_utils.draw_landmarks(
                    frame_c,
                    hand_landmarks_proto,
                    solutions.hands.HAND_CONNECTIONS,
                    solutions.drawing_styles.get_default_hand_landmarks_style(),
                    solutions.drawing_styles.get_default_hand_connections_style())

            if ima_cont < 10:
                cv2.imwrite(f"{folder}/{sample_var}{toma_cont}/{word}_00{ima_cont}.jpg",
                            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            elif ima_cont < 100:
                cv2.imwrite(f"{folder}/{sample_var}{toma_cont}/{word}_0{ima_cont}.jpg",
                            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                cv2.imwrite(f"{folder}/{sample_var}{toma_cont}/{word}_{ima_cont}.jpg",
                            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            ima_cont += 1
            print(ima_cont)

        elif ima_cont >=10:
            toma_cont += 1
            if toma_cont == 10:
                sample_var = "sample_0"
            elif toma_cont == 100:
                sample_var = "sample_"
            print("me he sumado")
            print(toma_cont)
            ima_cont = 0

        cv2.imshow('GestoLingo', cv2.cvtColor(frame_c,cv2.COLOR_RGB2BGR))
        if cv2.waitKey(5) == 27:
            break
cap.release()
cv2.destroyAllWindows()
