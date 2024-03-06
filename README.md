# GestoLingo
<img src="https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/logo_tfm.jpeg" width=500px>

# Autores
- [Guillermo Rojo Santos](https://github.com/GuillermoRojoSantos)
- [José Antonio Díaz](https://github.com/jada1998velez)
- [Gabriel Postigo](https://github.com/GabrielPostigo)
---
# Descripción y Justificación

👋 ¡Hola!,¿Te gustaría aprender más sobre la Lengua de Signos Española? 👋

Entonces debes de conocer **GestoLingo**, la mejor APP para aprender esta lengua. 🤙

Pero, ¿qué es GestoLingo? 🤔

**GestoLingo** es una herramienta de interpretación y traducción en tiempo real del **LSE** (Lengua de Signos Española) que usa `CV` (Computer Vision) y `NLP` (Natural Language Processing) para identificar, interpretar y transformar palabras simples del LSE en palabras equivalentes en español.

El principal propósito de esta herramienta es ayudar a gente con impedimentos del habla a aprender a comunicarse mediante el uso del Lenguaje de Signos en Español. ☝

¿Cómo ha sido logrado? 😱

Gracial al grupo de estudiantes del **Máster de Inteligencia Artificial y Big Data**, logrando conseguir crear un modelo  con Inteligencia Artificial capaz de realizar esta difícil tarea 🦾🤖

# Índice


[Arquitectura del proyecto](#arquitectura-del-proyecto-1)
--
[Tecnologías utilizadas](#tecnologc3adas-utilizadas-1)
--
[Obtención de datos](#obtencic3b3n-de-datos-1)
--
[Limpieza de datos](#limpieza-de-datos-1)
--
[Exploración y visualización de los datos](#preparacic3b3n-de-los-datos-1)
--
[Preparación de los datos](#preparacic3b3n-de-los-datos-1)
--
[Entrenamiento del modelo y comprobación del rendimiento](#entrenamiento-del-modelo-y-comprobacic3b3n-del-rendimiento-1)
--
[Procesamiento de Lenguaje Natural](#procesamiento-de-lenguaje-natural-1)
--
[Aplicación Web](#aplicacic3b3n-web-1)
--
[Bibliografía](#bibliografc3ada-1)
--
[Conclusión](#conclusic3b3n-1)
--

# Arquitectura del proyecto

## Diagrama
Este proyecto recoge 2 campos fundamentales de la Inteligencia Artificial, como lo son el NLP y el Reconocimiento de Imágenes. Se ha decidido dividir el proyecto en 3 campos fundamentales: 

* **Data:** Para la recogida y procesamiento de datos
* **Modelo:** Para la realización de una red neuronal que será el cerebro de la aplicación
* **Web:** Para mostrar de forma más interactiva el resultado final.

<img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/ArquitecturaGestoLingo.png' width = 800px>

A continuación se explicará de manera más detallada cada apartado:

**Data:**
* Se recogerán los datos para el entrenamiento con `grabaciones` realizadas por los propios participantes del proyecto para posteriormente tratarlas y exportarlas a un DataFrame.
* Se realizarán técnicas de `Web Scraping` a la página web [DILSE](https://fundacioncnse-dilse.org/) para la obtención de Videos y comprobación de palabras. Esos datos serán tratados y cargados a un Bucket de S3 el cual servirá como “Base de Datos”.

**Modelo:**


* En primer lugar, gracias a la librería `Keras`, se creará una red neuronal, la cual obtendrá datos de entrenamiento y validación. Posteriormente con la librería `TensorFlow` entrenaremos dicho modelo.


**Web:**

Se creará una aplicación web con Streamlit, la cual permanecerá en local debido a las limitaciones obtenidas por la plataforma a la hora de albergarla. La web estará dividida en las siguientes pestañas:

* **Índice:** Donde tendremos información principal sobre la página
* **Aprende:** En esta pestaña podremos aprender varias de las palabras del lenguaje de signos, gracias a que podemos buscar en el bucket de `S3` los vídeos para la demostración de éstas.
* **Practicar:** Aquí estará albergado el modelo, podremos activar la opción de “Cámara” para en tiempo real realizar algunas de las palabras que anteriormente hemos podido aprender.
* **Configuración:** Esta pestaña es necesaria para poder acceder al bucket de `AWS`, escribiendo las credenciales, diferenciando entre cuentas profesionales y corporativas

## Jerarquía de directorios

[Data](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data): Directorio donde se almacenan los datos que se irán generando para el entrenamiento del modelo.
* [DataFrames](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data/dataFrames):  Directorio donde se almacenan los archivos HDF5 antes de la limpieza, generados al pasar las fotos por ‘src/new_process_hands.py’.

* [model](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data/model): Directorio donde se guarda el modelo tras ser creado por ‘src/train_model.py’ .
    * [GestoLingo.keras](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data/model/GestoLingo.keras): Modelo entrenado.
    * [hand_landmarker.tas](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data/model/hand_landmarker.tas): Archivo que se usará para realizar las inferencias en ‘src/new_extract_hands.py’.

* [treatedDF](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/data/treatedDF): Directorio donde se almacenan los DataFrames tras ser limpiados en el cuaderno ‘notebooks/Limpieza_y_Exploración_de_datos.ipynb’.

[words](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/words): Directorio donde se almacenan las palabras, con sus samples y frames de cada gesto obtenido por src/new_extract_hands.py.

[images](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/words): Directorio donde están las imagenes que usaremos en README.md.

[notebooks](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/notebooks): Directorio se encuentran los cuadernos Jupyter.

* [Limpieza_y_Exploración_de_datos.ipynb](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/notebooks/Limpieza_y_Exploración_de_datos.ipynb): Cuaderno Jupyter que limpia los Dataframes almacenados en ‘data/dataframes’ y los almacena en ‘data/treatedDF’

* [WebScrapingGestolingo.ipynb](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/notebooks/WebScrapingGestolingo.ipynb):  Cuaderno Jupyter donde se realiza un scrapeo al diccionario Dilse, descarga los videos y los sube a un bucket en S3.

[src](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src): Directorio donde se almacenan los scripts principales.

* [legacy](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/legacy): Directorio donde quedan guardados los scripts de una versión antigua, en la que se usó un modelo de mediapipe diferente.

    * [extract_hands.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/legacy/extract_hands.py): Script de extracción de gestos y almacenado en local.

    * [process_hands.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/legacy/process_hands.py): Script para procesar y obtener los archivos HDF5 de las palabras almacenadas en el directorio words.


* [streamlit](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/streamlit): Directorio donde se almacenan los scripts y archivos relacionados con la aplicación web.

    * [images](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/streamlit/images): Directorio donde se almacenan las imágenes usadas en la web.

    * [streamlit_main.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/streamlit/streamlit_main.py): Script principal de la web.

    * [style.css](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/streamlit/style.css): Archivo de la hoja de estilos CSS para la web.

* [new_extract_hands.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/new_extract_hands.py): Script para capturar gestos y almacenar los frames en local, en la carpeta words.

* [new_process_hands.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/new_process_hands.py): Script que procesa los gestos almacenados en words y genera un archivo HDF5 correspondiente en la carpeta data/dataframes.

* [train_model.py](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/train_model.py): Script que sirve para crear, entrenar y guardar el modelo entrenado en la carpeta data/models.

# Tecnologías utilizadas

<div>
    <img src="images/aws.png" width="100px" style="margin: 2px;">
    <img src="images/colab.png" width="100px" style="margin: 2px;">
    <img src="images/css.png" width="100px" style="margin: 2px;">
    <img src="images/git.png" width="100px" style="margin: 2px;">
    <img src="images/github.png" width="100px" style="margin: 2px;">
    <img src="images/html.png" width="100px" style="margin: 2px;">
    <img src="images/jupyter.png" width="100px" style="margin: 2px;">
    <img src="images/keras.png" width="100px" style="margin: 2px;">
    <img src="images/mediapipe.png" width="100px" style="margin: 2px;">
    <img src="images/miniconda.png" width="100px" style="margin: 2px;">
    <img src="images/opencv.png" width="100px" style="margin: 2px;">
    <img src="images/pycharm.png" width="100px" style="margin: 2px;">
    <img src="images/python.png" width="100px" style="margin: 2px;">
    <img src="images/streamlit.png" width="100px" style="margin: 2px;">
    <img src="images/tensorflow.png" width="100px" style="margin: 2px;">
    <img src="images/visual.png" width="100px" style="margin: 2px;">
</div>

* **Open CV:** Biblioteca de visión por computadora.
* **Python:** Lenguaje de programación de alto nivel.
* **Streamlit:** Marco de creación de aplicaciones web interactivas con Python.
* **Mediapipe:** Biblioteca para análisis de datos de medios (imágenes y videos).
* **AWS:** Amazon Web Services, plataforma de servicios en la nube.
* **Google Colab:** Entorno de cuadernos colaborativos basado en la nube.
* **Jupyter:** Entorno interactivo para escribir y ejecutar código en cuadernos.
* **Miniconda:** Distribución de Conda más ligera para gestión de paquetes.
* **Tensorflow:** Biblioteca de código abierto para aprendizaje automático.
* **Keras:** Interfaz de alto nivel para redes neuronales, integrada en TensorFlow.
* **html:** Lenguaje de marcado para la creación de páginas web.
* **CSS:** Lenguaje para el diseño y estilo de páginas web.
* **Cx-Freeze:** Herramienta para crear ejecutables a partir de programas de Python.
* **Lupas Rename:** Aplicación para renombrar muchos archivos.
* **Github:** Plataforma de desarrollo colaborativo utilizando Git.
* **Git:** Sistema de control de versiones distribuido.
* **Visual Studio Code:** Editor de código fuente.
* **Pycharm:** Entorno de desarrollo integrado (IDE) para Python.



# Obtención de datos

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

# Limpieza de datos
   ## Dentro de `WebScrapingGestolingo.ipynb`
   Debido a que muchas de las palabras de la lengua española no tienen una traducción definida es necesario limpiar de las palabras propuestas todas aquellas que no se encuentren dentro del diccionario de lenguaje de signos
   ```py
   palabras_no_encontradas = []
   palabras_encontradas = []
   requisito = "No se ha encontrado ningún resultado para el término buscado."

   for palabra in palabras_limpias:
       url2 = f"https://fundacioncnse-dilse.org/?buscar={palabra}"
       headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
       response = re.get(url2, headers=headers)
       soup = BeautifulSoup(response.text, 'html.parser')
       if soup.find_all("h2")[1].text == requisito:
           palabras_no_encontradas.append(palabra)
       else:
           palabras_encontradas.append(palabra)



      # Crear un gráfico de barras
      fig, ax = plt.subplots()
      bars = plt.bar(['Encontradas', 'No encontradas'], [len(palabras_encontradas), len(palabras_no_encontradas)])
      
      # Agregar etiquetas y título
      plt.xlabel('Estado de las palabras')
      plt.ylabel('Número de palabras')
      plt.title('Comparación de palabras encontradas y no encontradas')
      
      # Mostrar el número encima de cada barra
      for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      
      # Mostrar el gráfico
      plt.show()
   ```
   <img src = 'https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/images/graficas_encontradas.png' width = 800px>   

   Tras esta separación entre encontradas y no encontradas, las no encontradas no son más usadas.

   ## Dentro de `Limpieza_y_Exploración_de_Datos.ipynb`

   Tras visualizar el estado de las palabras almacenadas en DataFrames, se limitan los samples a tener um máximo de 60 frames por sample, eliminando aquellos samples que superen esa cifra de frames.

   ```py
   for ind, x in enumerate(ls):
    for num in x.n_sample.unique():
        indices = x[x.n_sample==num].index
        if x.loc[indices[-1],"frame"]>60:
            x.drop(indices,inplace=True)
   ```
   
# Exploración y visualización de los datos


# Preparación de los datos

# Entrenamiento del modelo y comprobación del rendimiento -- `src/train_model.py`
Se realizan las importaciones:
```py
import os
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.utils import pad_sequences, to_categorical
from tensorflow.keras import layers, callbacks
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
```
Se establece cuantas palabras hay, la cantidad máxima de frames por sample y se crean dos listas vacias una para almacenar los keypoints y otra para almacenar las etiquetas, respectivamente 
```py
words = [x for x in os.listdir("../data/treatedDF")]
max_frames = 30
word_keypoints = []  # Keypoint sequence for each sample
word_nums = []  # Words represented by numbers
```

Se empeiza a procesar los datos, por cada Dataframe, se itera sobre el número de muestras y sus etiquetas, mediante la función `pad_sequences` de Keras
```py
for num, word in enumerate(words):
    df = pd.read_hdf(f"../data/treatedDF/{word}")
    for num_sample in df.n_sample.unique():
        word_keypoints.append([data["keypoints"] for _, data in df[df.n_sample == num_sample].iterrows()])
        word_nums.append(num)
```

Se rellena y truncan las secuencias de keypoints de una longitud de max frames. 

Separación de datos en conjuntos de entrenamiento y prueba. Y preparación de etiquetas, donde las etiquetas de las palabras pasan a ser vectores one-hot mediante el uso del método ‘to_categorical’.

```py
word_keypoints = pad_sequences(word_keypoints, maxlen=30, padding="post", truncating="post", dtype='float32')

X_train, X_test, y_train, y_test = train_test_split(word_keypoints, word_nums, test_size=0.30)
X_train = np.array(X_train)
y_train = to_categorical(y_train, num_classes=4, dtype="int")
X_test = np.array(X_test)
y_test = to_categorical(y_test, num_classes=4, dtype="int")

```

Se define un callback que será el encargado de detener el entrenamiento del modelo si no hay mejoras en la pérdida durante un número específico de epochs
```py
early_stoping = callbacks.EarlyStopping(min_delta=0.001,
                                        patience=5,
                                        restore_best_weights=True,
                                        monitor="loss")
```

Definimos el modelo, mediante `keras.Sequential`
Se agregan capas LSTM con diferentes configuraciones. 
También se agregan capas de Batch Normalización, Dense(las cuales están completamente conectadas) y Dropout para regularizar el modelo y evitar el sobreajuste.
La compilación del modelo es mediante el optimizador Adam, la función de pérdida de ‘categorical_crossentropy’ y la métrica de ‘accuracy’

```py
model = keras.Sequential(
    [layers.LSTM(64, return_sequences=True, activation="tanh", input_shape=(30, 126)),
     layers.LSTM(128, return_sequences=True, activation="tanh"),
     layers.LSTM(128, return_sequences=False, activation="tanh"),
     layers.BatchNormalization(),
     layers.Dense(70, activation="sigmoid"),
     layers.Dropout(0.2),
     layers.Dense(70, activation="relu"),
     layers.Dense(70, activation="relu"),
     layers.Dropout(0.2),
     layers.Dense(70, activation="relu"),
     layers.Dense(70, activation="relu"),
     layers.Dropout(0.2),
     layers.Dense(64, activation="relu"),
     layers.Dense(64, activation="relu"),
     layers.BatchNormalization(),
     layers.Dropout(0.2),
     layers.Dense(32, activation="sigmoid"),
     layers.Dense(32, activation="relu"),
     layers.Dense(4, activation="softmax")]
)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

```

El entrenamiento del modelo se realiza mediante el uso del método ‘fit’ de Keras.
Se le proporcionan los datos de entrenamiento, X_train e y_train, y los datos de validación, X_test e y_test. Se establece un número de epochs en 100 y se le proporciona el callback establecido antes.

```py
history = model.fit(X_train,
                    y_train,
                    epochs=100,
                    validation_data=(X_test, y_test),
                    callbacks=[early_stoping])
```

Se creará un Dataframe donde se almacenará todo sobre el entrenamiento del modelo, su pérdida y la validación de cada epoch
```py
history_df = pd.DataFrame(history.history)
```

Se visualiza esos valores de perdida, validación mediante Matplotlib, a lo largo del entrenamiento.

```py
history_df.loc[:, ['loss', 'val_loss']].plot()
plt.show()
```

Se muestra por pantalla un resumen del modelo

```py
print(model.summary())
```

Antes de guardar el modelo entrenado, se comprueba que la ruta exista, de no hacerlo, se crea.
Después, se guarda el modelo

```py
if not os.path.exists("../data/model/"):
    os.mkdir("../data/model/")

model.save("../data/model/GestoLingo.keras")
```

# Procesamiento de Lenguaje Natural

# Aplicación Web -- `src/streamlit/streamlit_main.py`
Importación de las librerias
```py
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
```
Se establece una configuración general de la página
```py
st.set_page_config(
    page_title="Gestolingo",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state = "expanded"
)
```
Se cargan las diferentes imagenes y se transfomran en una cadena base64, mediante `base64.b64encode()`
```py
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
```
Se establece un header
```py
header = f'''
    <header>
        <div id="logo-container">
            <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
        </div>
        <div id="app-name">Gestolingo</div>
    </header>
'''
```
El código que genera una cadena de texto HTML para la pestaña índice
```py
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
```

El código para la parte donde se muestra el logo de AWS dentro de la pestaña 'Configuración'
```py
configLogo = f'''
        <div class="logo-aws">
            <img style = "width:50% " src="data:image/png;base64,{data_url3}" alt="Logo">
        </div>
        <h3>Configuración del servidor AWS</h3>
        <li> ¡Disponible para cuentas corporativas! </li>
        <li> Accede a nuestra base de datos aportando las credenciales de AWS </li>
        <li> No olvides confirmar los datos antes de abandonar esta pestaña </li>
'''
```
El código para el bocadillo que se mostrará, en la pestaña 'Aprender', en caso de que no se haya iniciado conexión con el S3
```py
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
```
El código para el footer, que se mostrará en todas las pestañas
```py
footer = f'''
    <br>
    <br>
    <br>
    <footer>
        &copy; 2024 Gestolingo - Traductor de Lenguaje de Signos
    </footer>
'''
```
Menos el footer, todos estos codigos tienen una imagen que se carga desde una URL de datos base64, generada anteriormente.

Se carga el documento CSS, gracias a `st.markdown` se inserta el contenido del CSS en Streamlit. Enlace al [CSS](https://github.com/GuillermoRojoSantos/GestoLingo/blob/main/src/streamlit/style.css) 
Gracias a la opción de `unsafe_allow_html=True` se permite que se renderice el contenido HTML dentro de la app de forma segura.
```py
with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
```
Se muestra el header en todas las pestañas llamando a ‘st.markdown’ para que muestre el contenido HTML de la variable ‘header’.
```py
st.markdown(header, unsafe_allow_html=True)
```
Ahora veremos el código de verificación de inicio de sesión con AWS, verificando que ciertas claves estén presentes en el estado de la sesión de Streamlit. 
Si alguna falla/falta, se establece su valor a ‘False’. Se usan para controlar el estado de configuración de AWS
```py
state = st.session_state

if 'aws_id' not in st.session_state:
    state["aws_id"] = False
if 'aws_key' not in st.session_state:
    state["aws_key"] = False
if 'aws_token' not in st.session_state:
    state["aws_token"] = False
if 'open_key' not in st.session_state:
    state["open_key"] = False

```
Mediante `st.tabs` se crean 4 pestañas que permiten al usuario moverse entre diferentes secciones de la app. 
Las instancias de cada pestaña se almacenan en las variables tab1,tab2,tab3 y tab4, 'Inicio','Aprender','Practicar' y 'Configuración', respectivamente.
```py
tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Aprender", "Practicar","Configuración"])
```
Primero que nada, empecemos poniendo el footer, puesto que tiene que aparecer en todas las pestañas.
Por eso hay que ponerlo antes de establecer ninguna pestaña
```py
st.markdown(footer, unsafe_allow_html=True)
```

Ahora, empezamos a hacer las pestañas. Una a una.
Empecemos con la primera, la de inicio.
Al ser solo texto y una foto, código que se expusó antes(variable `body`), no tiene mucha complicación.
```py
with tab1:
  st.markdown(body, unsafe_allow_html=True)
```

La siguiente pestaña a realizar es 'Aprender'
En esta pestaña se mostrará un contenido u otro en función de si se ha establecido conexión o no con AWS. Para ello usaremos un condicional para verificar que `state["open_key"]=True`.

En caso de ser `True`, se mostrará un campo de texto donde podrás escribir una palabra, esta se buscará en la lista que hay y, de estar en ella, verás que aparece un video donde podrás ver el gesto de esa palabra.
Al introducir una palabra que no esté en la lista, te saldrá un error avisando de que esa palabra no está disponible.
Si tuvieras dudas con respecto a que palabra puedes o no encontrar, habrá un botón abajo donde ponga 'Mostrar Diccionario'. Al darle, veremos un DataFrame que nos muestra todas las palabras disponibles.

En caso de ser `False`, Se mostrara un bocadillo, la variable `bocadillo` antes vista, que nos indicará que debemos ir a la pestaña de 'Configuración' para poder ingresar las credenciales necesarias para establecer conexión con AWS.

```
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

```
Pasemos a la pestaña 3, 'Practicar'
En la cual, verás un botón que te dice 'Comenzar', si le das, se abrira tu cámara, mediante `cap = cv2.VideoCapture(0)`
Se crea un espacio de visualización  para los frames, mediante `st.empty()`
Se carga el modelo (entrenado previamente con `src/train_model.py`), con `model:keras.Sequential = keras.models.load_model("../../data/model/GestoLingo.keras")`
Se inicia un bucle `while` que va capturando frames del video en vivo y procesa la detección de las manos. Este bucle finalizará al pulsar el botón 'Stop'
Por cada frame se hace una serie de pasos:
   - Se convierte a RGB y se procesa con `Mediapipe Hands` para detectar las manos.
   - Se dibujan las landmarks
   - Se procesan las coordenadas de los landmarks para dictaminar que mano se está captando, si la derecha o la izquierda.
   - Se almacenan los keypoints de la mano detectada en una lista
   - Se verifica si se ha detectado una mano y si hay suficientes keypoints almacenados. Si se cumplen ambas, se incrementa el contador de frames y se realiza una predicción.
   - Dicha predicción se muestra en un objeto de Streamlit llamado `hold_meter_result.write()`
   - La imagen del frame procesado se muestra en el espacio de visualización creado usando `frame_placeholder.image`
```py
with tab3:
    abrir = st.button("Comenzar")
    if abrir:
        
        st.title("Webcam Live Feed")

        cap = cv2.VideoCapture(0)

        frame_placeholder = st.empty()
        stop_button_pressed = st.button("stop")
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        model:keras.Sequential = keras.models.load_model("../../data/model/GestoLingo.keras")

        keypoints = []
        frame_count = 0
        words = [x[0:-11] for x in os.listdir("../../data/treatedDF/")]
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
```
Y por último, pero no menos importante, pasamos a la pestaña 4, 'Configuración'
Aquí nos dividimos en dos columnas lo que veremos lo siguiente,
En la columna 1:
- Hay un interruptor toggle, que indicará quieres o no ingresar con una cuenta de estudiante. Esto hará que aparezca un campo extra para introducir la credencial de token su usas una cuenta de estudiante o no aparezca.
- Al introducir las credenciales correspondientes, pulsaremos el botón de 'Guardar', cuando esto suceda, se intentará verificar las credenciales, si son correctas, se modificará el estado de sesión, `state["open_key"]`.
- Se intentará establecer conexión con AWS S3, si es exitosa, devuelve `state["open_key"]=True`, se mostrará un mesaje de exito, se guardan las credenciales y que el usuario confirme pulsando un nuevo botón.
- En caso de fallar algo, saldrá un mensaje de error.

En la columna 2 se muestra el logo de AWS que establecimos antes en la variable `configLogo`
```py
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
```



# Bibliografía
- [Hand landmarks detection guide for Python](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python#video)
- [Mediapipe - GitHub](https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md)
- [Diccionario Dilse](https://fundacioncnse-dilse.org/index.php)
- [Anaconda - Docs](https://docs.anaconda.com/free/miniconda/index.html)
- [OpenCV - Docs](https://docs.opencv.org/4.x/)
- [Python - Docs](https://www.python.org/doc/)
- [Streamlit - Docs](https://docs.streamlit.io/)
- [Amazon AWS - Docs](https://docs.aws.amazon.com/)
- [Jupyter - Docs](https://docs.jupyter.org/en/latest/)
- [Tensorflow](https://www.tensorflow.org/?hl=es)
- [Keras - Docs](https://keras.io/)
- [Cx-Freeze](https://cx-freeze.readthedocs.io/en/stable/)
- [GitHub - Docs](https://docs.github.com/en)
- [Git - Docs](https://git-scm.com/doc)

# Conclusión
