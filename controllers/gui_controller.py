import streamlit as st
from controllers.back_controller import BackController
from view.main_view import draw_option_menu, draw_home_page, draw_event_manager_page, draw_ticket_office_page, \
    draw_access_management_page, draw_reports_page

import webbrowser
import datetime


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
            draw_access_management_page(self)
        elif self.run_page == 'reports':
            draw_reports_page()

    def valid_event_data(self, event_data, event_type, fields_to_validate=None):
        """
        Checks if the event data is valid.
        """

        event_fields = self.back_controller.choose_event_fields(event_type)

        # Si no se proporciona una lista de campos para validar, validar todos los campos
        if fields_to_validate is None:
            fields_to_validate = event_fields.keys()

        # Verificar que los datos no estén vacíos
        for field in fields_to_validate:
            if field != "state":  # Skip the state field
                value = event_data.get(field)
                if not value:
                    st.error(f"El campo {field} no puede estar vacío.")
                    return False

                # Verificar que los datos correspondan a lo que deben tener
                config = event_fields[field]
                if config["type"] == "number" and value <= 0:
                    st.error(f"El campo {field} debe ser un número mayor que 0.")
                    return False
                elif config["type"] == "text" and not isinstance(value, str):
                    st.error(f"El campo {field} debe ser un texto.")
                    return False
                elif config["type"] == "date" and not isinstance(value, datetime.date):
                    st.error(f"El campo {field} debe ser una fecha.")
                    return False
                elif config["type"] == "time" and not isinstance(value, datetime.time):
                    st.error(f"El campo {field} debe ser una hora.")
                    return False

                # Verificar que no exista un evento con la misma fecha
                if field == 'date' and self.back_controller.event_exists(value):
                    st.error("Ya existe un evento en esa fecha.")
                    return False

        return True

    def create_event(self, event_type, event_data):
        """
       Creates a new event of the specified type with the provided data.
       It communicates with the BackController to create the event and displays a success or error message
       based on the result.
       """
        if self.valid_event_data(event_data, event_type):
            self.back_controller.create_event(event_type, **event_data)
            st.success("event created successfully")


    def edit_event(self, event, new_value, field):
        """
        Edits the specified field of an existing event with a new value.
        It communicates with the BackController to edit the event and displays a success or error message
        based on the result.
        """
        # Crear una copia de los datos actuales del evento
        event_data = vars(event).copy()

        # Actualizar el campo que se está editando con el nuevo valor
        event_data[field] = new_value

        # Validar los datos del evento
        if not self.valid_event_data(event_data, event.type, [field]):
            return
        else:
            print(field)
            self.back_controller.edit_event(event, field, new_value)
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

    def valid_ticket_fields(self, other_amount, new_amount, price, ticket_type, event):

        """
        Checks if the fields to create a ticket are valid.
        """

        valid_fields = True
        if ticket_type == "philanthropic" and price != 0:
            valid_fields = False
            st.error("The price for philanthropic events should be zero. Please consider setting a price.")
        elif ticket_type != "philanthropic" and price == 0:
            valid_fields = False
            st.error("The price for non-philanthropic events should not be zero. Please consider setting a price.")
        elif new_amount <= 0:
            valid_fields = False
            st.error("The amount of tickets should be greater than zero.")
        elif new_amount + other_amount > event.capacity:
            valid_fields = False
            st.error("The amount of tickets should not exceed the event's capacity.")
        return valid_fields

    def assign_ticket_to_event(self, event, ticket_type, price, new_amount):

        other_amount = self.get_other_amount(event, ticket_type)

        if self.valid_ticket_fields(other_amount, new_amount, price, ticket_type, event):
            self.back_controller.create_ticket(event, ticket_type, price, new_amount)
            st.success("Ticket assigned successfully")

    def get_other_amount(self, event, ticket_type):
        other_amount = self.back_controller.get_amount_ticket_assigned("regular", event)
        if ticket_type == "regular":
            other_amount = self.back_controller.get_amount_ticket_assigned("presale", event)

        return other_amount

    def ticket_sale(self, event, ticket_type, buyer_name, buyer_id):

        if buyer_name.strip() == "" or buyer_id.strip() == "":  # .strip use for remove white spaces
            st.warning("Please, complete all the fields")

        else:

            ticket_sold = self.back_controller.create_sold_ticket(event, ticket_type, buyer_name, buyer_id)
            self.back_controller.add_sold_ticket_to_event(event, ticket_sold)

            if self.back_controller.verify_sold_ticket(event, ticket_sold.buyer_id):
                st.success("sale completed successfully")
            self.back_controller.generate_ticket_pdf(event, buyer_name, buyer_id, f"{buyer_id}.pdf")
            # Abrir el PDF en el navegador web
            webbrowser.open_new(f"{buyer_id}.pdf")

    def verify_access(self, event, buyer_id):
        sold_ticket = self.back_controller.get_sold_ticket_by_id(event, buyer_id)
        if sold_ticket is not None:
            st.success(f"Access granted, welcome {sold_ticket.buyer_name}")
        else:
            st.error(f"Access denied, {buyer_id} is not registered")
