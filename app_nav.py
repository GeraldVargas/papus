import streamlit as st
from PIL import Image

st.set_page_config(page_title="The Papus", page_icon="☠", layout="wide")

# --- Helpers / pages

def page_home():
    st.header("Bienvenido a The Papus")
    st.title("The Papus")
    st.write("Somos un grupo de desarrolladores apasionados por la tecnología y la innovación.")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("¿Quiénes somos?")
        st.write(
            """
            Somos un grupo de desarrolladores apasionados por la tecnología y la innovación. 
            Nuestro objetivo es crear soluciones digitales que mejoren la vida de las personas y 
            faciliten sus actividades diarias. Con un enfoque en la calidad y la creatividad, 
            trabajamos en proyectos que abarcan desde aplicaciones móviles hasta plataformas web.
            """
        )
    with right_column:
        st.header("Noticias")
        st.info("Aquí aparecerán novedades y proyectos recientes.")


def page_upload():
    st.header("Subir imagen")
    uploaded_file = st.file_uploader("Selecciona una imagen (png/jpg)", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file)
            st.image(img, caption="Imagen subida", use_column_width=True)
            # Guardar en session_state para usar en otras pestañas
            st.session_state["uploaded_image"] = img
        except Exception as e:
            st.error(f"No se pudo abrir la imagen: {e}")


def page_analysis():
    st.header("Análisis de imagen")
    img = st.session_state.get("uploaded_image")
    if img is None:
        st.warning("No hay imagen. Ve a 'Upload Image' y sube una imagen para analizarla.")
        return
    st.write("Información básica de la imagen:")
    st.write(f"- Tamaño: {img.size}")
    st.write(f"- Modo: {img.mode}")
    # Ejemplo simple: mostrar versión en escala de grises
    try:
        gray = img.convert("L")
        st.image(gray, caption="Versión en escala de grises", use_column_width=True)
    except Exception as e:
        st.error(f"Error al procesar la imagen: {e}")


def page_settings():
    st.header("Ajustes")
    st.write("Opciones de configuración (local, no persistente):")
    theme = st.selectbox("Tema", ["Claro", "Oscuro"])
    st.write(f"Tema seleccionado: {theme}")


def page_about():
    st.header("Acerca de")
    st.write("Proyecto de ejemplo con Streamlit. Navega por la barra lateral para ver las distintas pestañas.")
    st.write("Contacto: ejemplo@dominio.com")


# --- Sidebar / navigation
with st.sidebar:
    st.header("The Papus")
    page = st.radio("Navegación", ["Home", "Upload Image", "Analysis", "Settings", "About"])
    st.markdown("---")
    st.write("Made by The Papus")

# Inicializar session_state si falta
if "uploaded_image" not in st.session_state:
    st.session_state["uploaded_image"] = None

# Mapear páginas y renderizar la seleccionada
pages = {
    "Home": page_home,
    "Upload Image": page_upload,
    "Analysis": page_analysis,
    "Settings": page_settings,
    "About": page_about,
}

pages.get(page, page_home)()
