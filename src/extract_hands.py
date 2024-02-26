import mediapipe as mp
import cv2
import Utils as ut

mp_hands = mp.solutions.hands


with Holistic() as hm:
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        hd_frame, results = ut.holistic_detection(frame, hm)

        # if results.left_hand_landmarks or results.right_hand_landmarks:

        ut.draw_hand_keypoints(hd_frame,results)
        cv2.imshow("GestoLingo", hd_frame)

        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()