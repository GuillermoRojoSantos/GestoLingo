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
  st.text("Hola")

with tab2:
  st.text("Hola")

with tab3:
  st.text("Hola")

with tab4:
  st.text("Hola")