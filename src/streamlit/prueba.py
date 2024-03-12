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


with open('./style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Aprender", "Practicar","Configuración"])

with tab1:
  st.title("'La IA que da voz al silencio'")
  st.image("./images/indice.png")
     
with tab2:
  st.text("Hola")
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