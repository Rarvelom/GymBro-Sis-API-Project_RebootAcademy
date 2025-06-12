import streamlit as st
import requests
import json
from typing import Optional
from datetime import datetime

# Configuración de la aplicación
st.set_page_config(page_title="GymBro/Sis API Tester", layout="wide")

# URL base de la API
BASE_URL = "http://localhost:8000/api/v1"  # Ajusta según tu configuración

# Estilos CSS personalizados
st.markdown("""
<style>
    /* Contenedor principal para el contenido */
    .block-container {
        padding: 2rem;
        border-radius: 15px;
    }
    
    /* Título neón */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #ff0000, 
                     0 0 20px #ff0000, 
                     0 0 30px #ff0000, 
                     0 0 40px #ff0000, 
                     0 0 70px #ff0000, 
                     0 0 80px #ff0000;
        animation: flicker 1.5s infinite alternate;
        font-size: 4rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            text-shadow: 0 0 10px #ff0000, 
                         0 0 20px #ff0000, 
                         0 0 30px #ff0000, 
                         0 0 40px #ff0000, 
                         0 0 70px #ff0000, 
                         0 0 80px #ff0000;
        }
        20%, 24%, 55% {        
            text-shadow: none;
        }
    }

    /* Sidebar */
    .css-1d391kg {  /* Clase de sidebar container, puede variar */
        background-color: rgba(31, 31, 31, 0.9) !important;
        color: #ff4500 !important;
        font-weight: bold;
        font-size: 18px;
    }
    
    /* Botones en sidebar */
    .css-1emrehy.edgvbvh3 {
        background-color: #ff4500 !important;
        color: white !important;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    .css-1emrehy.edgvbvh3:hover {
        background-color: #ff6333 !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 69, 0, 0.4);
    }

    /* Títulos */
    .stHeader, h1, h2, h3, h4, h5 {
        font-family: 'Arial Black', Arial, sans-serif;
        color: #ff4500;
        text-shadow: 1px 1px 3px #000000a0;
    }

    /* Botones generales */
    .stButton>button {
        background-color: #ff4500;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(255,69,0,0.4);
    }
    .stButton>button:hover {
        background-color: #ff6333;
        cursor: pointer;
        transform: translateY(-2px);
        box-shadow: 0 7px 15px rgba(255, 69, 0, 0.6);
    }

    /* Inputs y TextArea */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        background-color: rgba(31, 31, 31, 0.9) !important;
        color: #f5f5f5 !important;
        border: 2px solid #ff4500 !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 8px !important;
    }
    .stTextInput>div>div>input::placeholder,
    .stTextArea>div>div>textarea::placeholder {
        color: #ff784e !important;
        font-style: italic;
    }

    /* Selectbox */
    div[role="combobox"] > div > div > div {
        background-color: rgba(31, 31, 31, 0.9) !important;
        color: #f5f5f5 !important;
        border: 2px solid #ff4500 !important;
        border-radius: 8px !important;
        font-weight: bold;
    }

    /* Tabs */
    .css-1v3fvcr.e1fqkh3o3 > div[role="tablist"] > button {
        background-color: rgba(42, 42, 42, 0.9);
        color: #ff4500;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px 8px 0 0;
        border: none;
        margin-right: 4px;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    .css-1v3fvcr.e1fqkh3o3 > div[role="tablist"] > button[aria-selected="true"] {
        background-color: #ff4500;
        color: white;
        box-shadow: 0 4px 6px rgba(255,69,0,0.6);
    }
    .css-1v3fvcr.e1fqkh3o3 > div[role="tablist"] > button:hover:not([aria-selected="true"]) {
        background-color: #ff6333;
        color: white;
    }

    /* JSON output box */
    .stJson {
        background-color: rgba(26, 26, 26, 0.9) !important;
        color: #ff784e !important;
        font-family: monospace;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 0 10px #ff4500aa;
        max-height: 400px;
        overflow-y: auto;
    }

</style>
""", unsafe_allow_html=True)

def make_request(method, endpoint, data=None):
    """Función genérica para hacer requests a la API"""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        else:
            return {"error": "Método no soportado"}
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": str(e)}

def spot_operations():
    st.header("Spots Operations")
    tab1, tab2, tab3, tab4 = st.tabs(["Get Spot by Type", "Get All Spots", "Create Spot", "Update Spot"])
    
    with tab1:
        st.subheader("Get Spot by Type")
        spot_type = st.text_input("Enter spot type (gym, park, etc.)", key="spot_type")
        if st.button("Get Spot"):
            result = make_request("GET", f"/spots/{spot_type}")
            st.json(result)
    
    with tab2:
        st.subheader("Get All Spots")
        if st.button("Get All Spots"):
            result = make_request("GET", "/spots")
            st.json(result)
    
    with tab3:
        st.subheader("Create New Spot")
        with st.form("create_spot_form"):
            spot_data = {
                "id": st.number_input("ID", min_value=1, step=1),
                "user_id": st.number_input("User ID", min_value=1, step=1),
                "name": st.text_input("Name"),
                "location": st.text_input("Location"),
                "description": st.text_area("Description"),
                "type": st.selectbox("Type", ["gym", "park", "studio", "other"]),
                "schedule": st.text_input("Schedule")
            }
            submitted = st.form_submit_button("Create Spot")
            if submitted:
                result = make_request("POST", "/spots", spot_data)
                st.json(result)
    
    with tab4:
        st.subheader("Update Existing Spot")
        with st.form("update_spot_form"):
            spot_name = st.text_input("Spot Name to Update")
            spot_data = {
                "name": st.text_input("New Name (optional)"),
                "location": st.text_input("New Location (optional)"),
                "description": st.text_area("New Description (optional)"),
                "type": st.selectbox("New Type (optional)", ["", "gym", "park", "studio", "other"]),
                "schedule": st.text_input("New Schedule (optional)")
            }
            # Eliminar campos vacíos
            spot_data = {k: v for k, v in spot_data.items() if v}
            submitted = st.form_submit_button("Update Spot")
            if submitted:
                result = make_request("PUT", f"/spots/{spot_name}", spot_data)
                st.json(result)

def user_operations():
    st.header("Users Operations")
    tab1, tab2, tab3, tab4 = st.tabs(["Get User by Username", "Get All Users", "Create User", "Update User"])
    
    with tab1:
        st.subheader("Get User by Username")
        username = st.text_input("Enter username", key="username")
        if st.button("Get User"):
            result = make_request("GET", f"/users/{username}")
            st.json(result)
    
    with tab2:
        st.subheader("Get All Users")
        if st.button("Get All Users"):
            result = make_request("GET", "/users")
            st.json(result)
    
    with tab3:
        st.subheader("Create New User")
        with st.form("create_user_form"):
            user_data = {
                "username": st.text_input("Username"),
                "email": st.text_input("Email"),
                "full_name": st.text_input("Full Name"),
                "password": st.text_input("Password", type="password")
            }
            submitted = st.form_submit_button("Create User")
            if submitted:
                result = make_request("POST", "/users", user_data)
                st.json(result)
    
    with tab4:
        st.subheader("Update Existing User")
        with st.form("update_user_form"):
            username = st.text_input("Username to Update")
            user_data = {
                "email": st.text_input("New Email (optional)"),
                "full_name": st.text_input("New Full Name (optional)"),
                "password": st.text_input("New Password (optional)", type="password")
            }
            # Eliminar campos vacíos
            user_data = {k: v for k, v in user_data.items() if v}
            submitted = st.form_submit_button("Update User")
            if submitted:
                result = make_request("PUT", f"/users/{username}", user_data)
                st.json(result)

def training_operations():
    st.header("Training Operations")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Get Training by Type", "Get All Training", "Create Training", "Get Training by Level", "Update Training"])
    
    with tab1:
        st.subheader("Get Training by Type")
        training_type = st.text_input("Enter training type", key="training_type")
        if st.button("Get Training by Type"):
            result = make_request("GET", f"/training/{training_type}")
            st.json(result)
    
    with tab2:
        st.subheader("Get All Training")
        if st.button("Get All Training"):
            result = make_request("GET", "/training")
            st.json(result)
    
    with tab3:
        st.subheader("Create New Training")
        with st.form("create_training_form"):
            training_data = {
                "name": st.text_input("Name"),
                "type": st.text_input("Type"),
                "level": st.selectbox("Level", ["beginner", "intermediate", "advanced"]),
                "duration": st.number_input("Duration (minutes)", min_value=1),
                "exercises": st.text_area("Exercises (JSON format)", value='[]'),
                "created_by": st.text_input("Created By")
            }
            submitted = st.form_submit_button("Create Training")
            if submitted:
                try:
                    training_data["exercises"] = json.loads(training_data["exercises"])
                    result = make_request("POST", "/training", training_data)
                    st.json(result)
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for exercises")
    
    with tab4:
        st.subheader("Get Training by Level")
        level = st.selectbox("Select level", ["beginner", "intermediate", "advanced"], key="level")
        if st.button("Get Training by Level"):
            result = make_request("GET", f"/training/level/{level}")
            st.json(result)
    
    with tab5:
        st.subheader("Update Existing Training")
        with st.form("update_training_form"):
            training_id = st.text_input("Training ID to Update")
            training_data = {
                "name": st.text_input("New Name (optional)"),
                "type": st.text_input("New Type (optional)"),
                "level": st.selectbox("New Level (optional)", ["", "beginner", "intermediate", "advanced"]),
                "duration": st.number_input("New Duration (minutes, optional)", min_value=1, value=None),
                "exercises": st.text_area("New Exercises (JSON format, optional)", value='')
            }
            # Eliminar campos vacíos
            training_data = {k: v for k, v in training_data.items() if v}
            if "exercises" in training_data and training_data["exercises"]:
                try:
                    training_data["exercises"] = json.loads(training_data["exercises"])
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for exercises")
                    training_data.pop("exercises", None)
            submitted = st.form_submit_button("Update Training")
            if submitted:
                result = make_request("PUT", f"/training/{training_id}", training_data)
                st.json(result)

def main():
    # Título con efecto neón
    st.markdown('<h1 class="neon-title">GymBro/Sis</h1>', unsafe_allow_html=True)

    # Inicializa la sesión si no existe
    if "active_section" not in st.session_state:
        st.session_state.active_section = "Spots"

    st.sidebar.markdown("## 📂 Colecciones")
    
    if st.sidebar.button("📍 Spots", use_container_width=True):
        st.session_state.active_section = "Spots"
    if st.sidebar.button("👤 Users", use_container_width=True):
        st.session_state.active_section = "Users"
    if st.sidebar.button("🏋️ Training", use_container_width=True):
        st.session_state.active_section = "Training"

    # Visual feedback del botón activo
    st.sidebar.markdown(f"### Sección activa: **{st.session_state.active_section}**")

    st.markdown("---")

    # Muestra la sección correspondiente
    if st.session_state.active_section == "Spots":
        spot_operations()
    elif st.session_state.active_section == "Users":
        user_operations()
    elif st.session_state.active_section == "Training":
        training_operations()


if __name__ == "__main__":
    main()