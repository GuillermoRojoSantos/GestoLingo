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

# Código html para header y footer

header = f'''
    <header>
        <div id="logo-container">
            <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''

footer = f'''
        <footer>
            &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
        </footer>
    '''

# Variables para elegir la cámara
sin_puntos = 'width: 50%; height: 50%'
con_puntos = 'display:none'



# Mostrar el código html y cargar la hoja de estilos (CSS)

with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

# Botón para elegir la cámara
st.text("Para poder ver los puntos de su mano deberá de activar el siguiente sensor")
on = st.toggle('Activar sensor')

if on:
    sin_puntos = 'display:none'
    con_puntos = 'width: 50%; height: 50%'
else:
    con_puntos = 'display:none'
    sin_puntos = 'width: 50%; height: 50%'

# Variable para el código JavaScript para la ejecución de la cámara

my_js = """
const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');

function onResults(results) {
    // Guarda el estado actual del contexto del lienzo
    canvasCtx.save();

    // Limpia el lienzo, borra todo el contenido existente
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);

    // Dibuja la imagen resultante en el lienzo
    canvasCtx.drawImage(
        results.image, 0, 0, canvasElement.width, canvasElement.height);

    // Verifica si hay múltiples landmarks (puntos característicos) de manos en los resultados
    if (results.multiHandLandmarks) {
        // Itera sobre cada conjunto de landmarks de mano
        for (const landmarks of results.multiHandLandmarks) {
            // Dibuja conectores entre los landmarks de la mano
            drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
                            {color: '#00FF00', lineWidth: 5});

            // Dibuja los landmarks de la mano
            drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
            if (results.multiHandLandmarks) {
            const handPointsData = results.multiHandLandmarks.flat();  // Obtener todos los puntos de la mano como un array plano
            console.log(handPointsData)
            //sendMessageToStreamlitClient("streamlit:setComponentValue", handPointsData);
            }
        }
        
    }

    // Restaura el estado previo del contexto del lienzo
    canvasCtx.restore();
}

const hands = new Hands({locateFile: (file) => {
    return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});

// Opciones de la captación de manos
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


# Código html y JavaScript para mostrar la cámara

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
    <script> console.log(handPointsData) </script>
    </head>

    <body>
    <div class="container">
        <video class="input_video" style="{sin_puntos}"></video>
        <canvas class="output_canvas" width="1280px" height="720px" style="{con_puntos}"></canvas>
    </div>
    </body>
    </html>
''', height=500)

# Mostrar el footer
# st.markdown(footer, unsafe_allow_html=True)
