import mediapipe as mp
import cv2
import Utils as ut

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Camera capture object's initialization
cap = cv2.VideoCapture(0)

with mp.solutions.hands.Hands(
    # Parametro para especificar la complejidad del modelo usado en la detección de las manos
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.9
) as mp_hands:
    while True:
        # Read Camera
        _, frame = cap.read()

        # Predict hand landmarks
        frame.flags.writeable = False
        # Conversion the Frame from BGR to RGB
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = mp_hands.process(frame)

        # Draw the annotations on the image
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        x = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                if x<1:
                    print(hand_landmarks)
                    x = x + 1
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        # Show the image, but flip horizontally it to have a selfie-view display
        cv2.imshow('GestoLingo', frame, 1)
        # If 'Esc'  is pressed, close the app
        if cv2.waitKey(5) == 27:
            break

cap.release()
cv2.destroyAllWindows()