import streamlit as st
from controllers.back_controller import BackController
from view.main_view import draw_option_menu, draw_home_page, draw_event_manager_page, draw_ticket_office_page, \
    draw_access_management_page, draw_reports_page
from settings import BAR_EVENT_FIELDS, THEATER_EVENT_FIELDS, PHILANTHROPIC_EVENT_FIELDS


class GUIController:
    def __init__(self):
        if 'my_state' not in st.session_state:
            self.back_controller = BackController()
            self.run_page = 'home'
            st.session_state['my_state'] = self
        else:
            self.back_controller = st.session_state.my_state.back_controller
            self.run_page = st.session_state.my_state.run_page

    def main(self):
        draw_option_menu(self)  # Menu de opciones siempre abierto sin necesitar condicional
        if self.run_page == 'home':
            draw_home_page()
        elif self.run_page == 'event_manager':
            draw_event_manager_page(self)
        elif self.run_page == 'ticket_office':
            draw_ticket_office_page()
        elif self.run_page == 'access_management':
            draw_access_management_page()
        elif self.run_page == 'reports':
            draw_reports_page()

    def create_event(self, event_type, event_data):
        if self.back_controller.event_exists(event_data['date']):
            st.error("Ya existe un evento en esa fecha")
        else:
            self.back_controller.create_event(event_type, **event_data)
            st.success("Evento creado con éxito")

    def choose_event_fields(self, event_type):
        fields = None
        if event_type == "bar":
            fields = BAR_EVENT_FIELDS
        elif event_type == "philanthropic":
            fields = PHILANTHROPIC_EVENT_FIELDS
        elif event_type == "theater":
            fields = THEATER_EVENT_FIELDS

        return fields
