import streamlit as st
from settings import TITLE_MAIN_PAGE, TITLE_MAIN_FUNCTIONS
from streamlit_option_menu import option_menu
from view.event_view import draw_create_event_interface, display_event, draw_events_library, \
    draw_searched_event_interface

""""Main view module for the GUI of the application. This module contains the main pages of the GUI."""


# Navigation menu
def draw_option_menu(gui_controller):
    with st.sidebar:
        menu = option_menu(
            menu_title="Menu",
            options=["Home", "Events", "Ticket Office", "Access", "Reports"],
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
    elif menu == "Reports":
        gui_controller.run_page = "reports"


# Main pages of the GUI
def draw_home_page():
    """On the home page, the user is welcomed and the main dashboard of the application is managed"""
    st.markdown(TITLE_MAIN_PAGE, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_page'>HUMOR HUB</div>", unsafe_allow_html=True)
    st.write("Welcome to Humor Hub, here you can manage events, ticketing, access and reports.")


def draw_event_manager_page(gui_controller):
    """On this page the user can create, edit, delete and search events. The user can also see the events library"""
    # Initialize session state variables if they don't exist
    if "create_event" not in st.session_state:
        st.session_state.create_event = False
    if "search_event" not in st.session_state:
        st.session_state.search_event = False
    if "show_event_library" not in st.session_state:
        st.session_state.show_event_library = False
    if "edit_event_interface" not in st.session_state:
        st.session_state.edit_event_interface = False
    if "delete_event_interface" not in st.session_state:
        st.session_state.delete_event_interface = False

    # Page title
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Event Manager</div>", unsafe_allow_html=True)

    """Create events"""
    st.subheader("Create Event")
    empty_col1, col1, empty_col2 = st.columns([0.9, 2.5, 1])

    with col1:
        event_type = st.selectbox("Select the type of event", ["Select...", "bar", "philanthropic", "theater"])

        # Choose the event fields depending on the type of event
        if event_type != "Select...":
            st.session_state.create_event = True
            event_fields = gui_controller.choose_event_fields(event_type)

            # If an event type has been selected, draw the event creation interface
            if event_fields is not None and st.session_state.create_event:
                draw_create_event_interface(gui_controller, event_type, event_fields)

                # Close the other interfaces while creating an event (Generate a better feeling for the user)
    """Consult event, edit and delete events"""
    st.subheader("Consult event")
    event_date_consult = st.date_input("Enter the date of the event to consult")

    # columns for search buttons
    search_button_col, out_search_button_col, empty = st.columns([0.3, 0.3, 3])

    with search_button_col:
        if st.button("Search"):
            st.session_state.search_event = True

        with out_search_button_col:
            if st.button("close"):  # FIXME: change to an X icon
                st.session_state.search_event = False
                st.session_state.edit_event_interface = False
                st.session_state.delete_event_interface = False

    if st.session_state.search_event:
        draw_searched_event_interface(gui_controller, event_date_consult)

    """Event library"""
    library_button_col, out_library_button_col, empty = st.columns([0.5, 0.5, 3])  # FIXME: change size
    with library_button_col:
        if st.button("Event library"):
            st.session_state.show_event_library = True
    with out_library_button_col:
        if st.button("Close library"):  # FIXME: change to an X icon
            st.session_state.show_event_library = False

    if st.session_state.show_event_library:
        draw_events_library(gui_controller)


def draw_ticket_office_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de boletería</div>", unsafe_allow_html=True)


def draw_access_management_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Manejo de ingreso</div>", unsafe_allow_html=True)


def draw_reports_page():
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Generar reportes</div>", unsafe_allow_html=True)
