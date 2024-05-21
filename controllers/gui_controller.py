import streamlit as st
from controllers.back_controller import BackController
from view.main_view import draw_option_menu, draw_home_page, draw_event_manager_page, draw_ticket_office_page, \
    draw_access_management_page, draw_reports_page
from settings import BAR_EVENT_FIELDS, THEATER_EVENT_FIELDS, PHILANTHROPIC_EVENT_FIELDS
import webbrowser

class GUIController:
    """
    The GUIController class is responsible for managing the user interface of the application.
    It interacts with the BackController to handle the business logic and updates the interface accordingly.
    """

    def __init__(self):
        """
        Initializes the GUIController with a BackController instance and the current page to be displayed.
        """
        if 'my_state' not in st.session_state:
            self.back_controller = BackController()
            self.run_page = 'home'
            st.session_state['my_state'] = self
        else:
            self.back_controller = st.session_state.my_state.back_controller
            self.run_page = st.session_state.my_state.run_page

    def main(self):
        """
        Main method that handles the navigation between different pages of the application.
        """
        draw_option_menu(self)
        if self.run_page == 'home':
            draw_home_page()
        elif self.run_page == 'event_manager':
            draw_event_manager_page(self)
        elif self.run_page == 'ticket_office':
            draw_ticket_office_page(self)
        elif self.run_page == 'access_management':
            draw_access_management_page()
        elif self.run_page == 'reports':
            draw_reports_page()

    def create_event(self, event_type, event_data):
        """
       Creates a new event of the specified type with the provided data.
       It communicates with the BackController to create the event and displays a success or error message
       based on the result.
       """
        if self.back_controller.event_exists(event_data['date']):
            st.error("Ya existe un evento en esa fecha")
        else:
            self.back_controller.create_event(event_type, **event_data)
            st.success("Evento creado con éxito")

    def choose_event_fields(self, event_type):
        """
        Returns the appropriate fields for the specified event type.
        """
        fields = None
        if event_type == "bar":
            fields = BAR_EVENT_FIELDS
        elif event_type == "philanthropic":
            fields = PHILANTHROPIC_EVENT_FIELDS
        elif event_type == "theater":
            fields = THEATER_EVENT_FIELDS

        return fields

    def edit_event(self, event, new_value, field, ):
        """
        Edits the specified field of an existing event with a new value.
        It communicates with the BackController to edit the event and displays a success or error message
        based on the result.
        """
        current_value = getattr(event, field)

        if new_value == current_value:
            st.warning("El nuevo valor es igual al valor actual. No se realizó ningún cambio.")
        elif field == "date" and self.back_controller.event_exists(new_value):
            st.error("Ya existe un evento en esa fecha")
        else:
            setattr(event, field, new_value)
            st.success("Evento editado con éxito")

    def delete_event(self, event):
        """
        Deletes the specified event.
        It communicates with the BackController to delete the event and updates the interface accordingly.
        """

        self.back_controller.delete_event(event)
        if not self.back_controller.event_exists(event.date):
            st.session_state.delete_event_interface = False
            st.rerun()

    def ticket_sale(self, event, ticket_type, buyer_name, buyer_id):

        if buyer_name.strip() is "" or buyer_id.strip() is "":  # .strip use for remove white spaces
            st.warning("Please, complete all the fields")

        else:
            print(f"len event sold { len(event.sold_tickets)}, capacity {event.capacity}")
            if len(event.sold_tickets) < int(event.capacity):

                ticket_sold = self.back_controller.create_sold_ticket(event, ticket_type, buyer_name, buyer_id)
                self.back_controller.add_sold_ticket_to_event(event, ticket_sold)

                if self.back_controller.verify_sold_ticket(event, ticket_sold.buyer_id):
                    st.success("sale completed successfully")
                self.back_controller.generate_ticket_pdf(event, buyer_name, buyer_id, f"{buyer_id}.pdf")
                # Abrir el PDF en el navegador web
                webbrowser.open_new(f"{buyer_id}.pdf")
            else:
                st.error("The event is full")
