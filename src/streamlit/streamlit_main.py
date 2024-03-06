import cv2
import streamlit as st
import mediapipe as mp
import base64
import boto3
import pandas as pd
from io import StringIO
from io import BytesIO
from tensorflow import keras
import numpy as np
import os


# Configuración de la página

st.set_page_config(
    page_title="Gestolingo",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state = "expanded"
)

# Carga de imágenes para código HTML

# Logo
with open("./images/logo1.png", "rb") as f:
    contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")

# Imagen Inicio
with open("./images/SBG-TEC.png", "rb") as f:
    contents2 = f.read()
    data_url2 = base64.b64encode(contents2).decode("utf-8")

# Logo AWS
with open("./images/aws.png", "rb") as f:
    contents3 = f.read()
    data_url3 = base64.b64encode(contents3).decode("utf-8")

# Robot
with open("./images/buenas.gif", "rb") as f:
    contents4 = f.read()
    data_url4 = base64.b64encode(contents4).decode("utf-8")


# Código HTML

# Código para el header
header = f'''
    <header>
        <div id="logo-container">
            <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''

# Código para el body de la pestaña índice
body = f'''
<div class= "index-div">
    <div class="text-block">
        <h2>La IA que da voz al silencio</h2>
        <p>Imaginen un mundo donde la barrera del lenguaje no sea un obstáculo, donde la comunicación sea fluida para todos, independientemente de su habilidad auditiva. Esto es exactamente lo que la nueva IA, desarrollada por los alumnos del Máster de IA & Big Data quieren lograr.</p>
        <h2>Cómo funciona</h2>
        <p>Esta innovadora IA utiliza avanzados algoritmos de visión en tiempo real para interpretar los gestos y signos realizados por personas que se comunican a través del lenguaje de signos. Esta IA puede traducir estos gestos en tiempo real.</p>
        <ul>
            <li> En la pestaña <b>Aprender</b> de nuestra Web podrás empezar con un diccionario de vídeos explicativos a aprender tus primeras palabras con el Lenguaje de Signos. </li>
            <li> En el apartado <b>Practicar</b> puedes poner a prueba tus habilidades sobre lo aprendido gracias al sistema de IA implementado en tiempo Real. Recuerda tener tu cámara lista y, ¡A gesticular se ha dicho!. </li>
            <li> Inicie sesión en <b>Configuración</b> con su cuenta de AWS para poder empezar a aprender </li>
        </ul>
    </div>
    <div class="image-block">
        <img class = "img-index" src="data:image/png;base64,{data_url2}" alt="Logo">
    </div>
</div>
'''

# Código para el logo de AWS
configLogo = f'''
        <div class="logo-aws">
            <img style = "width:50% " src="data:image/png;base64,{data_url3}" alt="Logo">
        </div>
        <h3>Configuración del servidor AWS</h3>
        <li> ¡Disponible para cuentas corporativas! </li>
        <li> Accede a nuestra base de datos aportando las credenciales de AWS </li>
        <li> No olvides confirmar los datos antes de abandonar esta pestaña </li>
'''

# Código para el bocadillo
bocadillo = f'''
<div class="centrado">
    <div>
        <div class="bocadillo-redondo">
            <section class="texto-bocadillo">  
                <p class="texto-animado"> Vaya a <b>"Configuración"</b> </p>
            </section>
        </div>
        <img class="robotin" src="data:image/png;base64,{data_url4}" alt="Robotin">
    </div>
</div>
'''

# Código para el footer
footer = f'''
    <br>
    <br>
    <br>
    <footer>
        &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
    </footer>
'''

# Mostrar el header en todas las pestañas y cargar la hoja de estilos (CSS)

with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

state = st.session_state

if 'aws_id' not in st.session_state:
    state["aws_id"] = False
if 'aws_key' not in st.session_state:
    state["aws_key"] = False
if 'aws_token' not in st.session_state:
    state["aws_token"] = False
if 'open_key' not in st.session_state:
    state["open_key"] = False

tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Aprender", "Practicar","Configuración"])

# Pestaña Inicio

st.markdown(footer, unsafe_allow_html=True)
with tab1:
  st.markdown(body, unsafe_allow_html=True)


# Pestaña Aprender

with tab2:
    if state["open_key"]:
        # Configurar la conexión a S3
        if state["aws_token"] is not None:
            s3 = boto3.client('s3', aws_access_key_id=state["aws_id"], aws_secret_access_key=state["aws_key"],
                              aws_session_token=state["aws_token"])
        else:
            s3 = boto3.client('s3', aws_access_key_id=state["aws_id"], aws_secret_access_key=state["aws_key"])
        busqueda = st.text_input("Buscar la palabra que quieras aprender:")
        col1, col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.text("")

        with col2:
            st.header("La palabra elegida es:")
            st.subheader(busqueda)
        with col3:
                st.text("")
        with col4:

            bucket_name = 'gestolingo'
            video_key = f'{busqueda}.mov'
            if busqueda:
            # Obtener el objeto desde S3
                try:
                    response = s3.head_object(Bucket=bucket_name, Key=video_key)
                    if response:
                        response2 = s3.get_object(Bucket=bucket_name, Key=video_key)
                        # Obtener los datos del video
                        video_data = response2['Body'].read()

                        # Mostrar el video desde los datos obtenidos de S3
                        st.video(BytesIO(video_data))
                    else:
                        st.alert("La palabra introducida no se encuentra en nuestra Base de Datos", icon="🚨")

                except s3.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == '404':
                        st.header(f"La palabra {busqueda} no se encuentra en nuestra base de datos.")
                    else:
                        st.header(f"Error al verificar la existencia del objeto: {e}")
                except Exception as e:
                    st.header(f"Se ha perdido la conexión")

        with col5:
            st.text("")
        mostrar = st.button("Mostrar Diccionario")
        if mostrar:
            # Descargar el archivo CSV desde S3
            response = s3.get_object(Bucket=bucket_name, Key='palabras_encontradas.csv')
            content = response['Body'].read().decode('utf-8')

            # Crear el DataFrame a partir del contenido del archivo
            palabras = pd.read_csv(StringIO(content))
            # Dividir la columna 'Palabras' en 16 columnas
            num_columnas = 16
            columnas_divididas = pd.DataFrame(palabras['Palabras'].to_numpy().reshape(-1, num_columnas),
                                            columns=[f'Columna_{i+1}' for i in range(num_columnas)])
            st.title('Palabras Disponibles')
            st.dataframe(columnas_divididas)
    else:
        st.markdown(bocadillo, unsafe_allow_html=True)

# Pestaña Practicar

with tab3:
    abrir = st.button("Comenzar")
    if abrir:

        st.title("Webcam Live Feed")

        cap = cv2.VideoCapture(0)

        frame_placeholder = st.empty()
        stop_button_pressed = st.button("stop")
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        model:keras.Sequential = keras.models.load_model("./models/GestoLingo.keras")

        keypoints = []
        frame_count = 0
        words = ["Hola", "Mundo", "Ordenador", "Rojo"]
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

# Pestaña Configuración

with tab4:

    col1, col2 = st.columns(2)
    with col1:
        aws_token = ""
        estudiante = st.toggle("Cuenta de estudiante")
        aws_id = st.text_input("Introduce el aws_access_key_id: ")
        aws_key =st.text_input("Introduce el aws_secret_access_key: ")
        if estudiante:
            aws_token =st.text_input("Introduce el aws_session_token: ")

        guardar = st.button("Guardar")
        if guardar:
                try:
                    if aws_id and aws_key:
                        if aws_id:
                            # Eliminamos el valor del estado de sesion
                            del state["aws_id"]
                            # Le aplicamos a este estado el valor del id introducido
                            state["aws_id"] = aws_id
                        if aws_key:
                            # Eliminamos el valor del estado de sesion
                            del state["aws_key"]
                            # Le aplicamos a este estado el valor del id introducido
                            state["aws_key"] = aws_key
                        if aws_token:
                            # Eliminamos el valor del estado de sesion
                            del state["aws_token"]
                            # Le aplicamos a este estado el valor del id introducido
                            state["aws_token"] = aws_token

                        try:
                            if state["aws_token"] is not None:
                                s3 = boto3.client('s3', aws_access_key_id=state["aws_id"],
                                                  aws_secret_access_key=state["aws_key"],
                                                  aws_session_token=state["aws_token"])
                            else:
                                s3 = boto3.client('s3', aws_access_key_id=state["aws_id"],
                                                  aws_secret_access_key=state["aws_key"])
                            s3.head_object(Bucket='gestolingo', Key='hola.mov')
                            state["open_key"] = True
                            st.text("Los datos han sido guardados, pulse para confirmar")
                            st.button("Confirmar")
                        except:
                            st.error("Error de Conexión", icon="🚨")
                except:
                    st.error("Las credenciales no son correctas", icon="🚨")
    with col2:
        st.markdown(configLogo, unsafe_allow_html=True)