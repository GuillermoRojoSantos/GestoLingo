import streamlit as st
import streamlit.components.v1 as com

## Configuración
st.set_page_config(
    page_title="Gestolingo",
    layout="wide"
)

# Using object notation
add_selectbox = st.sidebar.image('images/logo1.png')

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

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
# st.title("Javascript example")



header = '''
    <header>
        <div id="logo-container">
            <img id="logo" src="images/logo1.png" alt="Logo de Gestolingo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''

body = '''

        <h1>¡Bienvenido a Gestolingo!</h1>
        <p> Explora la revolución en la comunicación inclusiva a través de nuestro traductor de lenguaje de signos inteligente.</p>

        <div class="features">
            <div class="feature">
                <h2>Traducción Instantánea</h2>
                <p>Convierte gestos y expresiones en texto comprensible al instante.</p>
            </div>
            <div class="feature">
                <h2>Interfaz Amigable</h2>
                <p>Diseñada pensando en la facilidad de uso para usuarios de todas las edades.</p>
            </div>
            <div class="feature">
                <h2>Accesibilidad Total</h2>
                <p>Disponible en cualquier momento y lugar a través de la web, sin necesidad de descargas.</p>
            </div>
        </div>


    '''
    
footer = '''
    <footer>
        &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
    </footer>



         '''
with open('./style.css') as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)
st.markdown(body, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)


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
    <video class="input_video" style="width: 100%; height: 100%;"></video>
    <canvas class="output_canvas" width="1280px" height="720px" style="width: 100%; height: 100%;"></canvas>
  </div>
</body>
</html>
''', height = 10000)
