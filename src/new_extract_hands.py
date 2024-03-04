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
def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

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
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

  return annotated_image
hloptions = mp.tasks.vision.HandLandmarkerOptions(
    base_options=baseOptions,
    running_mode=mp.tasks.vision.RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.3,  # lower than value to get predictions more often
    min_hand_presence_confidence=0.3,  # lower than value to get predictions more often
    min_tracking_confidence=0.3,  # lower than value to get predictions more often
    # result_callback=get_result
)

cap = cv2.VideoCapture(0)

with HandLandmarker.create_from_options(hloptions) as landmarker:
    while True:
        _,frame = cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) if cap.get(cv2.CAP_PROP_POS_MSEC) != None else 0
        result = landmarker.detect_for_video(mp_image,int(timestamp))

        hand_landmarks_list = result.hand_landmarks
        handedness_list = result.handedness

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
                frame,
                hand_landmarks_proto,
                solutions.hands.HAND_CONNECTIONS,
                solutions.drawing_styles.get_default_hand_landmarks_style(),
                solutions.drawing_styles.get_default_hand_connections_style())

        cv2.imshow('GestoLingo', cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
        if cv2.waitKey(5) == 27:
            break
cap.release()
cv2.destroyAllWindows()


