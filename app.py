import streamlit as st
from PIL import Image

# 1. Configuración de la página
st.set_page_config(page_title="The Papus Official", page_icon="☠", layout="wide")

# 2. Estilo CSS Avanzado (Interfaz Gráfica)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
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
    .main-title {
        font-size: 50px;
        font-weight: 800;
        color: #ff4b4b;
        text-shadow: 2px 2px #000000;
        margin-bottom: 0px;
    }
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Función Maestra para Renderizar Perfiles
def render_profile(nombre_titulo, bio, stats, img_url):
    st.markdown(f"<h1 class='main-title'>{nombre_titulo}</h1>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        try:
            st.image(img_url, use_container_width=True)
        except:
            st.warning(f"⚠️ Imagen '{img_url}' no encontrada.")
        
        st.markdown(f"**Estado:** Activo 🟢")

    with col2:
        
        st.write(bio)
        
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='stat-card'><b>📛 Nombre:</b><br>{stats['Nombre']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>📏 Altura:</b><br>{stats['Altura']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>🎭 Apodo:</b><br>{stats['Apodo']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='stat-card'><b>🎂 Cumpleaños:</b><br>{stats['Cumpleaños']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>💡 Especialidad:</b><br>{stats['Especialidad']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-card'><b>💻 Skill Principal:</b><br>{stats['Skill']}</div>", unsafe_allow_html=True)

# 4. Funciones de cada Página
def page_julio():
    bio = "Julio es el fundador y una joven promesa de la programación. Empezó a los 5 años y, aunque la calvicie llegó temprano, su capacidad de procesamiento es legendaria."
    stats = {"Nombre": "Julio Cesar Anturiano", "Altura": "1.73m", "Apodo": "Espantaviejas", "Cumpleaños": "Misterio", "Especialidad": "Calvicie Precoz", "Skill": "Horas cívicas"}
    render_profile("Julio Cesar (El primer calvo)", bio, stats, "julioF.jpeg")
    
    # Galería exclusiva de Julio
    st.divider()
    st.subheader("📸 Galería de Julio")
    if 'Juliofotos' not in st.session_state: st.session_state.Juliofotos = []
    up = st.file_uploader("Sube fotos:", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    if up:
        for f in up:
            if f not in st.session_state.Juliofotos: st.session_state.Juliofotos.append(f)
    if st.session_state.Juliofotos:
        cols = st.columns(4)
        for i, f in enumerate(st.session_state.Juliofotos): cols[i % 4].image(f, width=200)

def page_quilla():
    bio = "El gurka oficial. Nadie sabe su nombre real, pero su capacidad para infiltrarse y su altura lo hacen el estratega por excelencia."
    stats = {"Nombre": "Quilla Omonte", "Altura": "1.79m", "Apodo": "Gurka", "Cumpleaños": "4 de Febrero", "Especialidad": "Infiltración", "Skill": "Acuchillar califachos"}
    render_profile("Quilla Omonte (El Gurka)", bio, stats, "gurka.jpeg")

def page_salva():
    bio = "Especialista en optimización. Salva es el encargado de que todo en el grupo funcione con la máxima eficiencia posible."
    stats = {"Nombre": "Salvador Eulate", "Altura": "1.73m", "Apodo": "Salva", "Cumpleaños": "Desconocido", "Especialidad": "Optimización", "Skill": "Código Limpio"}
    render_profile("Salva (El Optimizador)", bio, stats, "salva.jpeg")

def page_roba():
    bio = "Un integrante legendario conocido por su extraño magnetismo con las personas de la tercera edad. Un caballero de otra época."
    stats = {"Nombre": "Desconocido", "Altura": "1.75m", "Apodo": "Roba Abuelas", "Cumpleaños": "Enero", "Especialidad": "Seducción Vintage", "Skill": "Carisma nivel 100"}
    render_profile("Roba Abuelas", bio, stats, "roba.jpeg")

def page_rata():
    bio = "Experto en encontrar recursos donde no los hay. Si algo falta, el Ratateo lo consigue, aunque sea mordisqueando cables."
    stats = {"Nombre": "Teo", "Altura": "1.70m", "Apodo": "Ratateo", "Cumpleaños": "Misterio", "Especialidad": "Supervivencia", "Skill": "Roer firewalls"}
    render_profile("Ratateo", bio, stats, "julioF.jpeg")

def page_buzz():
    bio = "Siempre apuntando al infinito y más allá. Es el encargado de los viajes espaciales y de las misiones imposibles del grupo."
    stats = {"Nombre": "Buzz", "Altura": "1.80m", "Apodo": "Buzz Put", "Cumpleaños": "20 de Julio", "Especialidad": "Aeronáutica", "Skill": "Volar con estilo"}
    render_profile("Buzz Put", bio, stats, "julioF.jpeg")

def page_kakas():
    bio = "El guerrero más resistente. Ha sobrevivido a las situaciones más insalubres y siempre sale con una sonrisa (y un olor extraño)."
    stats = {"Nombre": "El Kakas", "Altura": "1.72m", "Apodo": "Kakas", "Cumpleaños": "Misterio", "Especialidad": "Resistencia biológica", "Skill": "Inmunidad total"}
    render_profile("El Kakas", bio, stats, "julioF.jpeg")

def page_prota():
    bio = "El centro de la narrativa. Todo lo que pasa en Los Papus tiene que ver con él. Tiene el 'plot armor' más fuerte del mundo."
    stats = {"Nombre": "Protagonista", "Altura": "1.75m", "Apodo": "El Prota", "Cumpleaños": "Cuando empieza la temporada", "Especialidad": "Guionazo", "Skill": "No morir"}
    render_profile("El Prota", bio, stats, "julioF.jpeg")

def page_cuca():
    bio = "La más pequeña pero la más fuerte. Puede sobrevivir a una explosión nuclear y seguir programando en COBOL."
    stats = {"Nombre": "Cuca", "Altura": "1.65m", "Apodo": "La Cuca", "Cumpleaños": "Misterio", "Especialidad": "Inmortalidad", "Skill": "Escabullirse"}
    render_profile("Cuca", bio, stats, "julioF.jpeg")

# 5. Sidebar y Navegación
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>💀 THE PAPUS</h2>", unsafe_allow_html=True)
    st.divider()
    selection = st.radio("Integrantes:", 
        ["Anturianos", "Quilla", "Salva", "Roba Abuelas", "Ratateo", "Buzz Put", "El kakas", "El Prota", "Cuca"])
    st.divider()
    st.info("The Papus Official © 2026")

# 6. Lógica de Enrutamiento
pages = {
    "Anturianos": page_julio,
    "Quilla": page_quilla,
    "Salva": page_salva,
    "Roba Abuelas": page_roba,
    "Ratateo": page_rata,
    "Buzz Put": page_buzz,
    "El kakas": page_kakas,
    "El Prota": page_prota,
    "Cuca": page_cuca
}

pages[selection]()
