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

status = True


with open('./style_2.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
st.markdown(header, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Aprender", "Practicar","Configuración"])

with tab1:
  st.text("Hola")

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


with tab3:
  st.text("Hola")

with tab4:
    if st.button('Submit'):
        st.write('Realizando la predicción...')