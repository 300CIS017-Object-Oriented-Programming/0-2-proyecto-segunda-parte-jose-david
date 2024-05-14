import streamlit as st
from settings import TITLE_MAIN_PAGE, TITLE_MAIN_FUNCTIONS
from streamlit_option_menu import option_menu
from view.event_view import draw_create_event_interface, display_event


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
    # Titulo de la página
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de eventos</div>", unsafe_allow_html=True)

    # Creacion de eventos
    st.subheader("Crear Evento")
    empty_col1, col1, empty_col2 = st.columns([0.9, 2.5, 1])

    with col1:
        event_type = st.selectbox("Seleccione el tipo de evento", ["Seleccione...", "bar", "philanthropic", "theater"])

        # Elegir los campos del evento dependiendo del tipo de evento
        event_fields = gui_controller.choose_event_fields(event_type)

        # Si se ha seleccionado un tipo de evento, dibuja la interfaz de creación de eventos
        if event_fields is not None and event_type != "Seleccione...":
            draw_create_event_interface(gui_controller, event_type, event_fields)

    st.subheader("Consultar evento")
    event_date_consult = st.date_input("Ingrese la fecha del evento a consultar")
    if st.button("Buscar"):
        searched_event = gui_controller.back_controller.get_event_by_date(event_date_consult)
        if searched_event is not None:
            display_event(gui_controller, searched_event, event_type)
        else:
            st.error("No se encontró ningún evento en la fecha seleccionada.")


def draw_ticket_office_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de boletería</div>", unsafe_allow_html=True)


def draw_access_management_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Manejo de ingreso</div>", unsafe_allow_html=True)


def draw_reports_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Generar reportes</div>", unsafe_allow_html=True)
