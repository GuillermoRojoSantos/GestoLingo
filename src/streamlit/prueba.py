import cv2
import streamlit as st
import mediapipe as mp
import base64
import boto3
from PIL import Image
from io import BytesIO

# Configuración de la página
st.set_page_config(
    page_title="Gestolingo",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state = "expanded"
)



# Logo
file_ = open("./images/logo1.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

# Imagen Inicio
file2_ = open("./images/SBG-TEC.png", "rb")
contents2 = file2_.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file2_.close()

# Código html para header y footer

header = f'''
    <header>
        <div id="logo-container">
            <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''

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
        </ul>
    </div>
    <div class="image-block">
        <img class = "img-index" src="data:image/png;base64,{data_url2}" alt="Logo">
    </div>
</div>
'''

# Mostrar el código html y cargar la hoja de estilos (CSS)

with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)
footer = f'''
    <footer>
        &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
    </footer>
'''


tab1, tab2, tab3 = st.tabs(["Inicio", "Aprender", "Practicar"])

st.markdown(footer, unsafe_allow_html=True)
with tab1:
  st.markdown(body, unsafe_allow_html=True)

with tab2:
    busqueda = st.text_input("Buscar la palabra que quieras aprender:")
    col1, col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text("")

    with col2:
        st.header("La palabra que usted ha escogido es:")
        st.subheader(busqueda)
    with col3:
        st.text("")
    with col4:

        aws_id="ASIAXYKJRAYDE7NXZN5Z"
        aws_key="6IWny0cTRhi+87EVSoUsjtX6cVTJDcbvCchLzJek"
        aws_token="FwoGZXIvYXdzEHgaDIFFcmATCnlgh9DTXCK+Ad56vpuVK5NT5MQFg9zVt63r9+Bo2fAE8MXiR7o8/ZAfLW3XLHnuOoRckUxO+SusvuMzAqLUe2brMo6cMIRgSM3Kch0jX4KzjNcHMjch1vksM/JnE7lQzE+A3qgmZ3eFAvXDE9uQrfBtXRROzh3JyhZs1B+OlQUV89uajsBLSxEWY+ALRNIEcMjQgGmDLcuA3QG6LUi/ZcvTLufg1VF7cT8YaYOoNB0hQkcrvhmvPKZhCNw1CCFKq8iejmQl0+Uo55eSrwYyLeMgMKjhkv0m7zR30Qfq1EcnnyYLf3pCckGu0vw6R33jXqXEjjEbP+GbNw9EPQ=="
        # Configurar la conexión a S3
        # aws_id="ASIAWVSX7FOF7DIM5O4B"
        # aws_key="luRO9l/BmxATYHC+krdOtCA4NWiGLWN/kTlh6DI+"
        # aws_token="FwoGZXIvYXdzEHgaDPwES6AdSG0ZUwwfvyLCAYNBtOBaCz9a0ixfVn0ruobDDT71U3FC+WR4yLgRz6LI4Md0Pyl/iWZBMWKmwdLzn6Qn5zdjU3i+CDICx38HLm+mRbKcq+6gRe33JXpehVfx8hOn5Volfl7g/zrAb8v4zlUgKoZrYRrhDPHF09OhaVnPs5CEdSkx6KQ1ey2f13YpNyqy9+aFrj0SXRQIiFS4qKMQ1nBh1qZvH8idLLR1VXNYZHisGkr9PGLkjTy03+2Ko1B080aCEUJ6M2pXC8fsQWx7KK+Jkq8GMi2AfOHG2rCun0lKPAmETxALvCqvNPsiQ635/RIp5URRpCxFLisvWYksVOf0z3c="
        

        s3 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_key,aws_session_token=aws_token)

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
                    st.header("La palabra introducida no se encuentra en nuestra Base de Datos")
                
            except s3.exceptions.ClientError as e:
                if e.response['Error']['Code'] == '404':
                    st.header(f"El objeto {video_key} no existe en el bucket {bucket_name}.")
                else:
                    st.header(f"Error al verificar la existencia del objeto: {e}")
            except Exception as e:
                st.header(f"Se produjo un error inesperado: {e}")
    with col5:
        st.text("")



with tab3:
    abrir = st.button("Comenzar")
    if abrir:
        cap = cv2.VideoCapture(0)

        frame_placeholder = st.empty()
        stop_button_pressed = st.button("stop")
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles

        with mp.solutions.hands.Hands(
            # Parametro para especificar la complejidad del modelo usado en la detección de las manos
            model_complexity=1,
            min_detection_confidence=0.3,
            min_tracking_confidence=0.6
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
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp.solutions.hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )

                frame_placeholder.image(cv2.cvtColor(image,cv2.COLOR_BGR2RGB), channels="RGB")
                if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                    break
        cap.release()
        cv2.destroyAllWindows()

