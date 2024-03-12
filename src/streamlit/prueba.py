import streamlit as st
import base64


# Configuración de la página

st.set_page_config(
    page_title="Gestolingo",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state = "expanded"
)

# Carga de imágenes para código HTML

# Logo
with open("./images/logo1.png", "rb") as f:
    contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")


# Código para el header
header = f'''
<header>
    <div id="logo-container">
        <img class = "logo-image" src="data:image/png;base64,{data_url}" alt="Logo">
    </div>
    <div id="app-name">Gestolingo</div>
</header>
'''

entra = f'''
<p>👋 ¡Hola!,¿Te gustaría aprender más sobre la Lengua de Signos Española? 👋</p>
<p>Entonces debes de conocer <b>GestoLingo</b>, la mejor APP para aprender esta lengua. 🤙</p>
'''

body = f'''
<div>
    <h3>Pero, ¿qué es GestoLingo? 🤔</h3>
    <p><b>GestoLingo</b> es una herramienta de interpretación y traducción en tiempo real del <b>LSE</b> (Lengua de
            Signos Española) que usa <i>CV</i> (Computer Vision) y <i>NLP</i> (Natural Language Processing) para identificar,
            interpretar y transformar palabras simples del LSE en palabras equivalentes en español.</p>
    <p>
        El principal propósito de esta herramienta es ayudar a gente con impedimentos del habla a aprender a
        comunicarse
        mediante el uso del Lenguaje de Signos en Español. ☝
    </p>
    <h3>¿Cómo ha sido logrado? 🧐</h3>
    <p>Gracial al grupo de estudiantes del <b>Máster de Inteligencia Artificial y Big Data</b>, logrando conseguir
        crear un modelo con Inteligencia Artificial capaz de realizar esta difícil tarea 🦾🤖</p>
    <br>
    <h2>Realizado por:</h2>
    <p style="display: flex;flex-direction: column;align-items: center;">Guillermo Rojo Santos | José Antonio Díaz | Gabriel Postigo Rando</p>
</div>
'''

sin_con= f'''
<div class="sin_con">
    <h1>Bienvenido a la pestaña 'Aprender'</h1>
    <div>
        <p>
            Para poder acceder a esta pestaña es necesario que inicie sesión en
        </p>
        <p style="margin-top: -10px;">
            la pestaña 'Configuración' con una cuenta de AWS.
        </p>
    </div>
    <div>
        <p>
            Si no sabes cómo iniciar sesión con tu cuenta, pulsa el botón
        </p>
        <p style="margin-top: -10px;">
            que pone 'Información'
        </p>
    </div>
</div>
'''

tablas_info= f'''
<div class="tablas">
    <div class="uni">
        <h2>Configuración</h2>
        <p>En primer lugar, en la pestaña configuración, deberás de elegir el tipo de cuenta de AWS que utilizarás,
            distinguiendo entre cuenta personal y cuenta de estudiante.</p>
    </div>
    <div>
        <h2>Cuenta personal</h2>
        <ol>
            <li>Accede a tu cuenta de AWS</li>
            <li>Click sobre tu perfil > " Mis credenciales de Seguridad"</li>
            <li>Dirigete al apartado "Claves de acceso"</li>
        </ol>
    </div>
    <div>
        <h2>Cuenta Estudiante</h2>
        <ol>
            <li>Inicia tu laboratorio en la página "Vocareum"</li>
            <li>Pulsa sobre el apartado "AWS Details"</li>
            <li>En AWS CLI pulsa en "Show"</li>
        </ol>
    </div>
</div>
'''

logo = '''
<img src="./images/logo_tfm.jpeg" style="max-width: 20%; border-radius: 10%;">
'''

titulo = '''
<div>
    <h2>Gestolingo</h2>
    <br>
    <h4>'La IA que da voz al silencio'</h4>
</div>
'''

status = True # simula haberse conectado o no al AWS

with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Aprender", "Practicar","Configuración"])

with tab1:
    st.write('')
    col0,col21, col22,col23,col24,col5 = st.columns(6)
    with col0:
       st.text('')
    with col21:
       st.text('')
    with col22:
        st.image('./images/logo_tfm.jpeg', width=200)
    with col23:
        st.markdown(titulo, unsafe_allow_html=True)
    with col24:
       st.text('')
    with col5:
       st.text('')

    col31,col32,col33 = st.columns(3)

    with col31:
       st.text('')
    with col32:
       st.markdown(body, unsafe_allow_html=True)
    with col33:
       st.text('')

    st.text('')
    st.text('')
     
with tab2:
    if status:
        st.text('Conectado')
        col1, col2,col3 = st.columns(3)
        col11,col12,col13 = st.columns(3)
        with col1:
            st.text('')
        
        with col2:
            st.header('¿Qué palabra te gustaria aprender?')
            busqueda = st.text_input("Buscar la palabra que quieras aprender:")
            if busqueda:
                st.image('./images/roboto.png', width=200) #aquí va el video
        with col3:
            st.text('')

        with col11:
            st.text('')
        with col12:
            st.text("")
            mostrar = st.button("Mostrar Diccionario")

            if mostrar:
                st.title('Palabras disponibles')
                st.image('./images/prinny.png', width=200)
        with col13:
            st.text('')
        

    else:
        st.text('No conectado')
        st.markdown(sin_con, unsafe_allow_html=True)

        if st.button('Información'):
            st.markdown(tablas_info, unsafe_allow_html=True)
        else:
            st.image('./images/roboto.png', width=200)

# Pestaña practicar

with tab3:
  col1, col2,col3 = st.columns(3)
  with col1:
    st.text("")
  with col2:
    st.title("Practica lo aprendido")
    bot1, bot2 = st.columns(2)
    with bot1:
      empezar = st.button("Empezar")
    with bot2:
      terminar = st.button("Parar")
    if empezar:
      st.image("./images/SBG-TEC.png")
  
  with col3:
    st.text("")
# Pestaña Configuración

with tab4:
  col1, col2,col3 = st.columns(3)

  with col1:
      st.text("")
  with col2:
      st.image("images/awsLogo.png", width=150)
      estudiante = st.toggle("Estudiante")
      aws_id = st.text_input("Introduce el aws_access_key_id: ")
      aws_key =st.text_input("Introduce el aws_secret_access_key: ")
      if estudiante:
        aws_token =st.text_input("Introduce el aws_session_token: ")
        st.markdown("<br>",unsafe_allow_html=True)
      guardar = st.button("Guardar")
      st.markdown("<br>",unsafe_allow_html=True)
      if guardar:
        st.text("Las credenciales han sido guardadas")
        confirmar = st.button("Confirmar")
        st.text(aws_id)
        st.text(aws_key)
        st.text(aws_token)
        if confirmar:
           st.text("")
        # try:
        #     if aws_id and aws_key:
        #         if aws_id:
        #             # Eliminamos el valor del estado de sesion
        #             del state["aws_id"]
        #             # Le aplicamos a este estado el valor del id introducido
        #             state["aws_id"] = aws_id
        #         if aws_key:
        #             # Eliminamos el valor del estado de sesion
        #             del state["aws_key"]
        #             # Le aplicamos a este estado el valor del id introducido
        #             state["aws_key"] = aws_key
        #         if aws_token:
        #             # Eliminamos el valor del estado de sesion
        #             del state["aws_token"]
        #             # Le aplicamos a este estado el valor del id introducido
        #             state["aws_token"] = aws_token

        #         try:
        #             if state["aws_token"] is not None:
        #                 s3 = boto3.client('s3', aws_access_key_id=state["aws_id"],
        #                                   aws_secret_access_key=state["aws_key"],
        #                                   aws_session_token=state["aws_token"])
        #             else:
        #                 s3 = boto3.client('s3', aws_access_key_id=state["aws_id"],
        #                                   aws_secret_access_key=state["aws_key"])
        #             s3.head_object(Bucket='gestolingo', Key='hola.mov')
        #             state["open_key"] = True
        #             st.text("Los datos han sido guardados, pulse para confirmar")
        #             st.button("Confirmar")
        #         except:
        #             st.error("Error de Conexión", icon="🚨")
        # except:
        #     st.error("Las credenciales no son correctas", icon="🚨")
  with col3:
      st.text("")