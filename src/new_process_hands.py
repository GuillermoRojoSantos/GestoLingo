import mediapipe as mp
import cv2
import os
import re
import pandas as pd
import numpy as np

# Mediapipe code
HandLandmarker = mp.tasks.vision.HandLandmarker
baseOptions = mp.tasks.BaseOptions(model_asset_path='../data/model/hand_landmarker.task')


def get_result(result: mp.tasks.vision.HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    return result


hloptions = mp.tasks.vision.HandLandmarkerOptions(
    base_options=baseOptions,
    running_mode=mp.tasks.vision.RunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.3,  # lower than value to get predictions more often
    min_hand_presence_confidence=0.1,  # lower than value to get predictions more often
    min_tracking_confidence=0.3,  # lower than value to get predictions more often
    # result_callback=get_result
)

if not os.path.exists("../data/dataFrames/"):
    os.mkdir("../data/dataFrames/")

with HandLandmarker.create_from_options(hloptions) as landmarker:
    for lista in os.listdir("../data/words/"):
        df = pd.DataFrame(columns=["n_sample", "frame", "keypoints"])
        for sample in os.listdir(f"../data/words/{lista}/"):
            f_counter = 1
            for image in os.listdir(f"../data/words/{lista}/{sample}/"):
                frame = cv2.imread(f"../data/words/{lista}/{sample}/{image}")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = landmarker.process(frame)
                left_hand = []
                right_hand = []

                # hand_landmarks_list = result.hand_landmarks
                # handedness_list = result.handedness
                if result.hand_landmarks:
                    for x in range(len(result.handedness)):
                        if result.handedness[x][0].index == 0:
                            right_hand = np.array([result.hand_landmarks[x][r].x, result.hand_landmarks[x][r].y,
                                                   result.hand_landmarks[x][r].z] for r in
                                                  range(len(result.hand_landmarks[x])))
                        else:
                            left_hand = np.array([result.hand_landmarks[x][r].x, result.hand_landmarks[x][r].y,
                                                  result.hand_landmarks[x][r].z] for r in
                                                 range(len(result.hand_landmarks[x])))

                    if len(left_hand) == 0:
                        left_hand = np.zeros(21 * 3)
                    elif len(right_hand) == 0:
                        right_hand = np.zeros((21 * 3))

                    res_hand_landmarks = np.concatenate([left_hand, right_hand])
                    df.loc[len(df.index)] = {"n_sample": int(re.findall("\d+", sample)[0]),
                                             "frame": f_counter,
                                             "keypoints": res_hand_landmarks}
            f_counter = 0
        df.to_hdf(f"../data/dataFrames/{lista}.h5", key="data", mode="w")
