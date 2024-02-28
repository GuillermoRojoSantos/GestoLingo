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



header = f'''
    <header>
        <div id="logo-container">
            <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''

body = f'''
        <footer>
            &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
        </footer>
    '''


with open('./style.css') as css:
            st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

# Contenido para la Opción 2
sin_puntos = 'width: 50%; height: 50%'
con_puntos = 'display:none'

    # Botón
st.text("Para poder ver los puntos de su mano deberá de activar el siguiente sensor")
on = st.toggle('Activar sensor')

if on:
    sin_puntos = 'display:none'
    con_puntos = 'width: 50%; height: 50%'
else:
    con_puntos = 'display:none'
    sin_puntos = 'width: 50%; height: 50%'
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
    minDetectionConfidence: 0.2,
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
''', height=500)




# st.markdown(body, unsafe_allow_html=True)