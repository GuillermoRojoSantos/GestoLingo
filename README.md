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

# Aplicación Web

# Bibliografía

# Conclusión
