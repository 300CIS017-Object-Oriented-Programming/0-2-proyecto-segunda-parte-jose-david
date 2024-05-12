import streamlit as st
from controllers.back_controller import BackController
from view.main_view import draw_option_menu, draw_home_page, draw_event_manager_page, draw_ticket_office_page, \
    draw_access_management_page, draw_reports_page


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
        draw_option_menu(self)
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
