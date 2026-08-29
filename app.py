import streamlit as st  # Importa la librería Streamlit con el alias st.
inicio = st.Page("inicio.py", title="Inicio", icon="🏠", default=True)  # Define la página donde se ingresará el dato.
api = st.Page("api.py", title="Resultado API", icon="🛢️")  # Define la página donde se utilizará el dato guardado.
pagina = st.navigation([inicio, api])  # Registra las páginas de la aplicación.
pagina.run()  # Ejecuta la página seleccionada por el usuario.
