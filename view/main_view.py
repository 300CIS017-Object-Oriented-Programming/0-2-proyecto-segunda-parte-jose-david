import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from settings import button_style
from view.event_manager_view import draw_create_event_interface, draw_events_library, \
    draw_searched_event_interface
from view.ticket_office_view import draw_ticket_management_interface, draw_ticket_sales_management_interface
from view.access_management_view import draw_register_access_interface
from view.home_view import draw_dashboard, draw_sales_report_interface, draw_financial_reports_interface, \
    draw_demographic_reports_interface, draw_artist_reports_interface
from settings import TITLE_MAIN_PAGE, TITLE_MAIN_FUNCTIONS

""""Main view module for the GUI of the application. This module contains the main pages of the GUI."""


# Navigation menu
def draw_option_menu(gui_controller):
    """Draw the navigation menu of the application"""

    with st.sidebar:
        st.title("Humor Hub")
        menu = option_menu(
            menu_title="Menu",
            options=["Home", "Events", "Ticket Office", "Access"],
            icons=["house-fill", "calendar2-check-fill", "credit-card-fill", "person-check-fill"],
            menu_icon='list-ul',
            styles={
                "icon": {
                    "color": "wihte",
                    "font-size": "18px"
                },
                "nav-link-selected": {

                    "background-color": "#ff8906"
                }
            }
        )


    # Depending on the selected option in the menu, set the current page
    if menu == "Home":
        gui_controller.run_page = "home"
    elif menu == "Events":
        gui_controller.run_page = "event_manager"
    elif menu == "Ticket Office":
        gui_controller.run_page = "ticket_office"
    elif menu == "Access":
        gui_controller.run_page = "access_management"


# Main pages of the GUI
def draw_home_page(gui_controller):
    """On the home page, the user is welcomed and the main dashboard of the application is managed"""
    if "dashboard" not in st.session_state:
        st.session_state.dashboard = False
    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)

    st.markdown("# <div class='title_main_page'>HOME PAGE</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Welcome  😎 </h1>", unsafe_allow_html=True)
    st.text("Welcome, the best event management application. Here you can manage events, ticket sales,"
            "access to events, and view reports.")
    st.markdown("<br>", unsafe_allow_html=True)

    # dash boards
    draw_dashboard(gui_controller)
    sales_report_col, financial_reports_col = st.columns([1, 1])
    with sales_report_col:
        draw_sales_report_interface(gui_controller)
    with financial_reports_col:
        draw_financial_reports_interface(gui_controller)

    demographic_reports_col, artist_reports_col = st.columns([1, 1])

    with demographic_reports_col:
        draw_demographic_reports_interface(gui_controller)
    with artist_reports_col:
        draw_artist_reports_interface(gui_controller)


def draw_event_manager_page(gui_controller):
    """
    Dibujar lo relacionado con la pagina de manejo de eventos
    """

    # Incializacion de las variables de session state para manejar las paginas

    if "create_event" not in st.session_state:
        st.session_state.create_event = False
    if "search_event" not in st.session_state:
        st.session_state.search_event = False
    if "show_event_library" not in st.session_state:
        st.session_state.show_event_library = False

    #  Agregar estilo a los botones
    st.markdown(button_style, unsafe_allow_html=True)

    # Titulo
    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_page'>Event Manager</div>", unsafe_allow_html=True)

    """ Crear evento """
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Create Event  🗓️ ")
    # columnas
    empty, select_event_type_col, select_button_col, close_button_col, empty = st.columns([0.9, 1, 0.5, 0.4, 0.6])

    with select_event_type_col:
        event_type = st.selectbox("Select the type of event", ["bar", "philanthropic", "theater"])
    with select_button_col:
        st.write("")  # por motivos esteticos
        st.write("")
        if st.button("Select"):
            st.session_state.create_event = True
            st.session_state.search_event = False  # Cierra la interfaz de búsqueda
    if st.session_state.create_event:
        empty, form_col, empty = st.columns([0.5, 3, 0.5])  # columnas
        with form_col:
            draw_create_event_interface(gui_controller, event_type, close_button_col)  # view/event_manager_view

    """ Consular, editar o eliminar evento """

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Consult event 🔍")

    st.markdown("<br>", unsafe_allow_html=True)

    date_event_col, search_button_col, close_button_col, empty = st.columns([1, 0.5, 0.3, 2])  # columnas

    with date_event_col:
        event_date_consult = st.date_input("Enter the date of the event to consult")
    with search_button_col:
        st.write("")  # por motivos esteticos
        st.write("")
        if st.button("Search"):
            st.session_state.search_event = True
            st.session_state.create_event = False  # Cierra la interfaz de creación

    if st.session_state.search_event:
        draw_searched_event_interface(gui_controller, event_date_consult, close_button_col)  # view/event_view

    """Event library"""

    library_button_col, close_button_col, empty = st.columns([0.5, 0.5, 3])  # columnas

    with library_button_col:
        if st.button("Event library"):
            st.session_state.show_event_library = True

    if st.session_state.show_event_library:
        draw_events_library(gui_controller, close_button_col)  # view/event_manager_view


def draw_ticket_office_page(gui_controller):
    """On this page the user can manage the ticketing of the events and the sales"""

    # Initialize session state variables if they don't exist
    if "ticket_sale_management" not in st.session_state:
        st.session_state.ticket_sale_management = False
    if "ticket_management" not in st.session_state:
        st.session_state.ticket_management = False

    #  Agregar estilo a los botones
    st.markdown(button_style, unsafe_allow_html=True)

    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_page'>TICKET OFFICE</div>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    (empty, management_col, close_button_col, empty,
     sales_col, close_button_col1, empty) = st.columns([0.5, 1, 0.3, 1, 1, 0.3, 0.1])

    """ Tickets management """

    with management_col:
        st.subheader("Price of the tickets 🎫")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Tickets management"):
            st.session_state.ticket_management = True
            st.session_state.ticket_sale_management = False  # Close the ticket sales management interface

    if st.session_state.ticket_management:
        draw_ticket_management_interface(gui_controller, close_button_col)  # view/ticket_office_view

    """ Ticket sales management """

    with sales_col:
        st.subheader("Sales management 💰")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sales management"):
            st.session_state.ticket_sale_management = True

    if st.session_state.ticket_sale_management:
        draw_ticket_sales_management_interface(gui_controller, close_button_col1)  # view/ticket_office_view


def draw_access_management_page(gui_controller):
    if "access_management" not in st.session_state:
        st.session_state.access_management = False

    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_page'>ACCSESS MANAGEMENT</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    current_date = gui_controller.back_controller.get_current_date()
    event_today = gui_controller.back_controller.get_event_by_date(current_date)
    if event_today:
        st.markdown("<h1 style='text-align: center;'>Event programing for today  📌 </h1>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        name_event_col, opening_time_col, show_time_col = st.columns([1, 1.4, 0.7])  # Columns
        with name_event_col:
            st.markdown(f"<h4>Event: {event_today.name}</h4>", unsafe_allow_html=True)
        with opening_time_col:
            st.markdown(f"<h4>Opening time: {event_today.opening_time}</h4>", unsafe_allow_html=True)
        with show_time_col:
            st.markdown(f"<h4>Show time: {event_today.show_time}</h4>", unsafe_allow_html=True)

        empty, button_col, close_button, empty = st.columns([2.5, 1, 1, 3])  # Columns

        with button_col:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Register access"):
                st.session_state.access_management = True
        if st.session_state.access_management:
            draw_register_access_interface(gui_controller, event_today, close_button)

    else:
        st.markdown("<h1 style='text-align: center;'>Not event for today  😅 </h1>", unsafe_allow_html=True)
