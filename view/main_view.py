import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

from view.event_manager_view import draw_create_event_interface, draw_events_library, \
    draw_searched_event_interface
from view.ticket_office_view import draw_ticket_management_interface, draw_ticket_sales_management_interface
from view.access_management_view import draw_register_access_interface
from view.home_view import draw_dashboard
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
    st.markdown("# <div class='title_main_page'>WELCOME !</div>", unsafe_allow_html=True)
    st.write("Welcome to Humor Hub, here you can manage events, ticketing, access and reports.")

    # dash board

    st.markdown("## Dashboard")
    st.text("put a date range")
    empty, start_date_col, end_date_col, button_col, empty = st.columns([2, 1, 1, 1, 2])
    with start_date_col:
        star_date = st.date_input("star_date")
    with end_date_col:
        end_date = st.date_input("end_date")
    with button_col:
        st.write("")
        st.write("")
        if st.button("Show"):
            st.session_state.dashboard = True
    empty, dashboard_col = st.columns([1, 4])
    if st.session_state.dashboard:
        draw_dashboard(gui_controller, star_date, end_date)







    # Supongamos que tienes un DataFrame de pandas 'df' con las columnas 'event_type', 'date' y 'total_income'
    df = pd.DataFrame({
        'event_type': ['Bar', 'Theater', 'Philanthropic', 'Bar', 'Theater', 'Philanthropic'],
        'date': pd.to_datetime(['2024-01-01', '2024-01-01', '2024-01-01', '2024-02-01', '2024-02-01', '2024-02-01']),
        'total_income': [1000, 2000, 3000, 1500, 2500, 3500]
    })

    # Filtrar el DataFrame por el rango de fechas
    start_date = '2024-01-01'
    end_date = '2024-02-01'
    mask = (df['date'] > start_date) & (df['date'] <= end_date)
    df = df.loc[mask]

    # Crear el gráfico de barras con Plotly
    fig = px.bar(df, x='event_type', y='total_income', color='event_type', title='Total income by event type')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
    # ---------------------------------------
    df = pd.DataFrame({
        'date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'value': [2, 1, 3, 4, 3, 4, 5, 4, 5, 6, 7, 8]
    })

    fig = px.line(df, x='date', y='value', title='Line Chart Example')
    st.plotly_chart(fig)
    # ---------------------------------------
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 1, 3, 4, 3]
    })

    fig = px.scatter(df, x='x', y='y', title='Scatter Plot Example')
    st.plotly_chart(fig)

    # ---------------------------------------

    df = pd.DataFrame({
        'fruit': ['apple', 'banana', 'orange'],
        'count': [10, 15, 7]
    })

    fig = px.pie(df, values='count', names='fruit', title='Pie Chart Example')
    st.plotly_chart(fig)

    # ---------------------------------------
    df = pd.DataFrame({
        'value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    })

    fig = px.histogram(df, x='value', nbins=4, title='Histogram Example')
    st.plotly_chart(fig)

    # ---------------------------------------
    df = pd.DataFrame({
        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'group': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
    })

    fig = px.box(df, x='group', y='value', title='Box Plot Example')
    st.plotly_chart(fig)

    df = pd.DataFrame({
        'date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'value1': [2, 1, 3, 4, 3, 4, 5, 4, 5, 6, 7, 8],
        'value2': [3, 2, 4, 5, 4, 5, 6, 5, 6, 7, 8, 9]
    })

    fig = px.area(df, x='date', y=['value1', 'value2'], title='Area Chart Example')

    st.plotly_chart(fig)


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

    # Titulo
    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Event Manager</div>", unsafe_allow_html=True)

    """ Crear evento """

    st.subheader("Create Event")
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

    st.subheader("Consult event")

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

    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Gestor de boletería</div>", unsafe_allow_html=True)
    empty, management_col, sales_col, empty = st.columns([1, 1, 1, 1])

    """ Tickets management """

    with management_col:
        st.subheader("price of the tickets")
        if st.button("Tickets management"):
            st.session_state.ticket_management = True
            st.session_state.ticket_sale_management = False  # Close the ticket sales management interface

    if st.session_state.ticket_management:
        draw_ticket_management_interface(gui_controller)  # view/ticket_office_view

    """ Ticket sales management """

    with sales_col:
        st.subheader("Sales management")
        if st.button("Sales management"):
            st.session_state.ticket_sale_management = True

    if st.session_state.ticket_sale_management:
        draw_ticket_sales_management_interface(gui_controller)  # view/ticket_office_view


def draw_access_management_page(gui_controller):
    if "access_management" not in st.session_state:
        st.session_state.access_management = False

    st.markdown(TITLE_MAIN_FUNCTIONS, unsafe_allow_html=True)
    st.markdown("# <div class='title_main_functions'>Manejo de ingreso</div>", unsafe_allow_html=True)

    current_date = gui_controller.back_controller.get_current_date()
    event_today = gui_controller.back_controller.get_event_by_date(current_date)
    if event_today:
        st.write("Event programing for today")  # FIXME: CSS
        name_event_col, opening_time_col, show_time_col = st.columns([1, 1, 1])  # Columns
        with name_event_col:
            st.write(f"Event: {event_today.name}")
        with opening_time_col:
            st.write(f"Opening time: {event_today.opening_time}")
        with show_time_col:
            st.write(f"Show time: {event_today.show_time}")
        button_col, close_button, empty = st.columns([1, 1, 3])  # Columns
        with button_col:
            if st.button("Register access"):
                st.session_state.access_management = True
        if st.session_state.access_management:
            draw_register_access_interface(gui_controller, event_today, close_button)

    else:
        st.subheader("No event for today")  # FIXME: CSS
