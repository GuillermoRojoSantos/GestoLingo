import streamlit as st
import streamlit.components.v1 as com
import base64

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

# Imagenes
file2_ = open("./images/SBG-TEC.png", "rb")
contents2 = file2_.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file2_.close()

# Botones en la barra lateral
opcion_1_button = st.sidebar.button("Índice")
opcion_2_button = st.sidebar.button("App")

# Contenido para la Opción 1
if opcion_1_button:

    header = f'''
        <header>
            <div id="logo-container">
                <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
            </div>
            <div id="app-name">Gestolingo</div>
        </header>
    '''

    body = f'''
            <div class="contenedor">
                <div class="texto">
                    <p class="title-box"> La IA que da voz al silencio </p>
                    <p> Imaginen un mundo donde la barrera del lenguaje no sea un obstáculo, donde la comunicación sea fluida para todos, independientemente de su habilidad auditiva. Esto es exactamente lo que los alumnos del máster de Inteligencia Artificial y Big Data está logrando.</p>
                    <p class="title-box"> Cómo funciona </p>
                    <p> Esta innovadora IA utiliza avanzados algoritmos de visión por computadora para interpretar los gestos y signos realizados por personas que se comunican a través del lenguaje de signos. Entrenada con el Diccionario de la lengua de signos española y con los integrantes del proyecto, la IA puede traducir estos gestos en tiempo real. </p>
                </div>
                <div class="imagen">
                    <img src="data:image/png;base64,{data_url2}" alt="robot">   
                </div>
            </div>

            <div class="features">
                <div class="feature">
                    <p class="title-box">Traducción Instantánea</p>
                    <p>Convierte gestos y expresiones en texto comprensible al instante.</p>
                </div>
                <div class="feature">
                    <p class="title-box">Interfaz Amigable</p>
                    <p>Diseñada pensando en la facilidad de uso para usuarios de todas las edades.</p>
                </div>
                <div class="feature">
                    <p class="title-box">Accesibilidad Total</p>
                    <p>Disponible en cualquier momento y lugar a través de la web, sin necesidad de descargas.</p>
                </div>
            </div>

            <footer>
                &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
            </footer>
        '''


    with open('./style.css') as css:
            st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
    st.markdown(header, unsafe_allow_html=True)
    st.markdown(body, unsafe_allow_html=True)

# Contenido para la Opción 2
if opcion_2_button:
    # Botón
    sin_puntos = 'width: 50%; height: 50%'
    con_puntos = 'display:none'
    my_js = """
    const videoElement = document.getElementsByClassName('input_video')[0];
    const canvasElement = document.getElementsByClassName('output_canvas')[0];
    const canvasCtx = canvasElement.getContext('2d');

    function onResults(results) {
        canvasCtx.save();
        canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
        canvasCtx.drawImage(
            results.image, 0, 0, canvasElement.width, canvasElement.height);
        if (results.multiHandLandmarks) {
            for (const landmarks of results.multiHandLandmarks) {
                drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
                                {color: '#00FF00', lineWidth: 5});
                drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
            }
        }
        canvasCtx.restore();
    }

    const hands = new Hands({locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
    }});
    hands.setOptions({
        maxNumHands: 2,
        modelComplexity: 1,
        minDetectionConfidence: 0.7,
        minTrackingConfidence: 0.9
    });
    hands.onResults(onResults);

    const camera = new Camera(videoElement, {
        onFrame: async () => {
            await hands.send({image: videoElement});
        },
        width: 1280,
        height: 720
    });
    camera.start();
    """
    com.html(f'''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@mediapipe/control_utils/control_utils.js" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
        <script type="module">
            {my_js}
        </script>
        </head>

        <body>
        <div class="container">
            <video class="input_video" style="{sin_puntos}"></video>
            <canvas class="output_canvas" width="1280px" height="720px" style="{con_puntos}"></canvas>
        </div>
        </body>
        </html>
    ''', height=300)

    

    on = st.toggle('Activar sensor')

    if on:
        sin_puntos = 'display:none'
        con_puntos = 'width: 50%; height: 50%'
    else:
        con_puntos = 'display:none'
        sin_puntos = 'width: 50%; height: 50%'
