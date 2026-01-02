import streamlit as st
from PIL import Image


st.set_page_config(page_title="The Papus Official", page_icon="☠", layout="wide")


st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
    
    /* Estilo de tarjetas para estadísticas */
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
        transition: transform 0.3s;
    }
    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
    }

    /* Títulos personalizados */
    .main-title {
        font-size: 50px;
        font-weight: 800;
        color: #ff4b4b;
        text-shadow: 2px 2px #000000;
    }
    
    /* Sidebar estilizado */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #333;
    }
    
    /* Botones y enlaces */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


def render_profile(nombre, bio, stats, img_url, link_bio="https://google.com"):
    
    st.markdown(f"<h1 class='main-title'>{nombre}</h1>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        
        try:
            st.image(img_url, use_container_width=True)
        except:
            st.warning("⚠️ Imagen no encontrada. Sube 'julioF.jpeg' a la carpeta.")
        
        st.markdown(f"[🔗 Conoce más sobre su trabajo]({link_bio})")

    with col2:
        st.subheader("📜 Biografía")
        st.write(bio)
        
        st.subheader("📊 Ficha Técnica")
        
       
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='stat-card'><b>📛 Nombre:</b><br>{stats['Nombre']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>📏 Altura:</b><br>{stats['Altura']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>🎭 Apodo:</b><br>{stats['Apodo']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='stat-card'><b>🎂 Cumpleaños:</b><br>{stats['Cumpleaños']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>💡 Especialidad:</b><br>{stats['Especialidad']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>💻 Skill Principal:</b><br>{stats['Skill']}</div>", unsafe_allow_html=True)



def page_julio():
    bio = """Julio es una joven promesa de la programación. Empezó su camino en el código a los 5 años, 
    demostrando una habilidad innata para los algoritmos. A pesar de su calvicie precoz, su cerebro 
    funciona a una velocidad superior a la de un procesador i9."""
    
    stats = {
        "Nombre": "Julio Cesar Anturiano",
        "Altura": "1.73m",
        "Apodo": "Anturipenes",
        "Cumpleaños": "Desconocido",
        "Especialidad": "Calvicie de alto rendimiento",
        "Skill": "Python & Debugging"
    }
    
    render_profile("Julio Cesar (El Fundador)", bio, stats, "julioF.jpeg")

    
    st.divider()
    st.subheader("📸 Galería Comunitaria")
    if 'Juliofotos' not in st.session_state:
        st.session_state.Juliofotos = []
        
    uploaded_files = st.file_uploader("Sube contenido de Anturipenes:", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    if uploaded_files:
        for f in uploaded_files:
            if f not in st.session_state.Juliofotos:
                st.session_state.Juliofotos.append(f)
    
    if st.session_state.Juliofotos:
        cols = st.columns(4)
        for i, f in enumerate(st.session_state.Juliofotos):
            cols[i % 4].image(f, width=200)

def page_quilla():
    bio = "El estratega del grupo. Nadie conoce su verdadero origen, pero su habilidad para 'puntear' errores en el código es legendaria."
    stats = {
        "Nombre": "Quilla Omonte",
        "Altura": "1.79m",
        "Apodo": "Gurka",
        "Cumpleaños": "4 de Febrero",
        "Especialidad": "Infiltración y Sistemas",
        "Skill": "C++ & Networking"
    }
    render_profile("Quilla Omonte (El Gurka)", bio, stats, "gurka.jpeg")


with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💀 THE PAPUS</h2>", unsafe_allow_html=True)
    st.write("Selecciona a un integrante para ver su perfil detallado:")
    
    selection = st.radio("", ["Anturipenes", "Quilla", "Salva", "Roba Abuelas", "Ratateo"])
    
    st.divider()
    st.info("Proyecto desarrollado por la comunidad de Los Papus © 2024")


if selection == "Anturipenes":
    page_julio()
elif selection == "Quilla":
    page_quilla()
else:
    st.title(f"Perfil de {selection}")
    st.warning("Este perfil aún no ha sido completado. ¡Vuelve pronto!")
    st.image("https://via.placeholder.com/800x400.png?text=Proximamente")
