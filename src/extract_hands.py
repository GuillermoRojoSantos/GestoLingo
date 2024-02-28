import mediapipe as mp
import cv2
import Utils as ut
import os
import re

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
ima_cont = 0

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

with mp.solutions.hands.Hands(
    # Parametro para especificar la complejidad del modelo usado en la detección de las manos
    model_complexity=1,
    min_detection_confidence=0.2,
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
        image = frame.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            if not os.path.exists(f"{folder}/sample_{toma_cont}/"):
                os.mkdir(f"{folder}/sample_{toma_cont}/")
                print(f" Carpeta {folder}/sample_{toma_cont}/ creada")

            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                wrist_x = hand_landmarks.landmark[0].x
                if wrist_x > 0.5:
                    # Mano izquierda
                    print("Mano derecha")
                else:
                    # Mano derecha
                    print("Mano izquierda")
                # Save the frame in local folder
                cv2.imwrite(f"{folder}/sample_{toma_cont}/{word}_{ima_cont}.jpg",cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
                ima_cont +=1


        # Show the image, but flip horizontally it to have a selfie-view display
        cv2.imshow('GestoLingo', image)
        # If 'Esc'  is pressed, close the app
        if cv2.waitKey(5) == 27:
            break
        elif cv2.waitKey(5) & 0xFF == ord('q'):
            toma_cont+=1
            print("me he sumado")
            ima_cont=0

cap.release()
cv2.destroyAllWindows()