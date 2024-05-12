import streamlit as st
from settings import TITLE_MAIN_PAGE, TITLE_MAIN_FUNCTIONS
from streamlit_option_menu import option_menu
from view.event_view import draw_create_bar_event, draw_create_philanthropic_event, draw_create_theater_event


def draw_option_menu(gui_controller):
    # Menú de opcodes para manejar las páginas principales
    with st.sidebar:
        menu = option_menu(
            menu_title="Menu",
            options=["Home", "Eventos", "Boleteria", "Ingreso", "Reportes"],
        )
    if menu == "Home":
        gui_controller.run_page = "home"
    elif menu == "Eventos":
        gui_controller.run_page = "event_manager"
    elif menu == "Boleteria":
        gui_controller.run_page = "ticket_office"
    elif menu == "Ingreso":
        gui_controller.run_page = "access_management"
    elif menu == "Reportes":
        gui_controller.run_page = "reports"


# Fucnciones para dibujar las paginas principales del menu de opciones
def draw_home_page():
    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_page'>HUMOR HUB</div>", unsafe_allow_html=True)
    st.write("Bienvenido a Humor Hub, aquí podrás gestionar eventos, boletería, ingreso y reportes.")


def draw_event_manager_page(gui_controller):
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de eventos</div>", unsafe_allow_html=True)
    st.subheader("Crear Evento")  # FIX ME. Cambiaar css
    empty_col0, col1, col2, col3, empty_col4 = st.columns([2, 2, 2, 2, 2])

    with col1:
        if st.button("Evento bar"):

            draw_create_bar_event()

    with col2:
        if st.button("Evento filantropico"):

            draw_create_philanthropic_event()

    with col3:
        if st.button("Evento teatro"):

            draw_create_theater_event()

    st.subheader("Consultar evento")
    st.date_input("Fecha del evento")
    if st.button("Buscar"):
        # Funcion para buscar evento
        pass


def draw_ticket_office_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de boletería</div>", unsafe_allow_html=True)


def draw_access_management_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Manejo de ingreso</div>", unsafe_allow_html=True)


def draw_reports_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Generar reportes</div>", unsafe_allow_html=True)
