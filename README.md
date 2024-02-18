# GestoLingo
---
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
