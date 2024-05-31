import streamlit as st

from controllers.gui_controller import GUIController

st.set_page_config(page_title="Humor Hub", layout="wide")
if __name__ == "__main__":
    # Punto de entrada de la aplicación, llama al controlador de la interfaz gráfica
    gui = GUIController()
    gui.main()
