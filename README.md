# GestoLingo
<img src="https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/logo_tfm.jpeg" width=500px>

## Autores
- [Guillermo Rojo Santos](https://github.com/GuillermoRojoSantos)
- [José Antonio Díaz](https://github.com/jada1998velez)
- [Gabriel Postigo](https://github.com/GabrielPostigo)
---
## Descripción y Justificación
**GestoLingo** es una herramienta de interpretación y traducción en tiempo real del **LSE** (Lengua de Signos Española) que usa **CV** (Computer Vision) y **NLP** (Natural Language Processing) para identificar, interpretar y transformar las frases simples del LSE en frases equivalentes en español.
Este modelo será entrenado usando el diccionario de la [**Funcación DILSE**](https://fundacioncnse-dilse.org/) (Diccionario de la Lengua de Signos Española) y multiples videos subtitulados en los cuales se hace uso del LSE.

Con esta herramienta queremos ayudar a gente con diversidad funcional o impedimentos del habla a comunicarse con gente que no posea conocimientos de LSE.

---
## Obtención de datos

### 1º intento
En un principio se probbó a obtener los datos de la fuente  "[**Diccionario de la Lengua de Signos Española**](https://fundacioncnse-dilse.org/)", ésta página nos ofrece un buscador en el que nosotros podremos elegir la palabra que queramos aprender y nos aparecerá un video descargable para esa palabra.

En primer lugar utilizamos técnicas de Web Scraping desde Google Colab para la obtención de esos vídeos.
Utilizaremos la librería `BeautifulSoup` y la librería `request` para la obtención de dichos datos

Cuando obtengamos los vídeos de la web, es necesario dividirlo en frames, por lo que usaremos la siguiente función para dividir el vídeo y guardar esos frames en carpetas

(***NOTA:** Vamos a usar una sola palabra como ejemplo, pero se deberá de hacer después con todas las que queramos*)

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/scraping.png' width = 800px>

Para guardar las imágenes y no tener que repetir el proceso cada vez que iniciamos el colab, utilizamos el siguiente código

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/descargar_directorio.png' width = 800px>

Usando el modelo de Mediapipe de detección de manos, hacemos una predicción en cada frame de la posición de las manos, para ello utilizamos el siguiente código:

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/marcar_mediapipe.png' width = 800px>

Con el modelo de Mediapipe que se ha mencionado antes, se ha creado una clase con funcionalidades dedicadas al seguimiento de manos (el archivo `src/seguimiento_manos.py`), en el cuál se establecen las funciones para ubicar una sola mano o ambas, detectar la posición de de estas, cuantos dedos hay levantados y la distancia que hay entre los dedos de cada mano.

Vamos a mostrar un ejemplo de como se vería un frame de la palabra `hola` con la detección del mediapipe.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/hola_15_marked.png' width = 800px>

### 2º intento y con el que nos quedamos
Después de probar este método y ver que no sabiamos como implementarlo, decidimos obtener los datos de las manos directamente nosotros mismos con una aplicación en Python, el archivo `src/extract_hands.py`.
Su funcionamiento redica en que al ejecutarse, pedirá por la terminal que palabras vas a capturar, creando las carpetas correspondientes, cada vez que detecte una mano capturará. Pero, para pasar de toma habrá que pulsar la tecla `Q` del teclado. Si quieres cerrar el programa, solamente tendrás que pulsar `Esc`.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/Muestradecapturademanos.png' width = 800px>

#### Extracción de Keypoints de los samples y almacenamiento en archivos HDF
Tras sacar todas las tomas que necesites de esa Palabra, se ejecutará `process_hands.py` para procesar los keypoints de cada frame almacenado en cada sample, nos generará un archivo `<palabra>.h5`, donde se almacenará el Dataframe de la palabra.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/muestradesamplesydataframes.png' width = 800px>
