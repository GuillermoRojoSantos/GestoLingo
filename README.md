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
Como anteriormente se mencionó, vamos a obtener los datos de la fuente  "[**Diccionario de la Lengua de Signos Española**](https://fundacioncnse-dilse.org/)", ésta página nos ofrece un buscador en el que nosotros podremos elegir la palabra que queramos aprender y nos aparecerá un video descargable para esa palabra.

En primer lugar utilizaremos técnicas de Web Scraping desde Google Colab para la obtención de esos vídeos.
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

Por otra parte, tenemos la app en Python que hemos creado para grabar, frame a frame, los gestos para cada letra del abecedario. Este archivo es `src/detector_manos.py`. En esta app, se importa la clase del archivo `src/seguimiento_manos.py` para usar sus funciones. Al ejecutarla, te pedirá que letra vas a tomar, creará, si no existe, una carpeta llamada `data/Letra_{letra_introducida}`(la letra dependerá de la letra ingresada), que es donde la app tomará y guardará las fotos que tome a tu mano al momento de ejecutar la app.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/captura_mano_con_dibujo.png' width = 800px>

Al momento de guardar la imagenes, las guarda tal y como lo ves, así que normalmente, estas variables subrayadas, se dejan en `False` para dejar solo la mano sin lines o recuadros.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/partes_a_alterar_dibujo.png' width = 800px>
