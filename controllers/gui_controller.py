import streamlit as st
from controllers.back_controller import BackController
from view.main_view import draw_option_menu, draw_home_page, draw_event_manager_page, draw_ticket_office_page, \
    draw_access_management_page

import webbrowser
import datetime


class GUIController:
    """
    Clase que controla la interfaz gráfica de la aplicación. Cuando dibujar cada pagina y manejar la interacción
    con el usuario.
    """

    def __init__(self):

        if 'my_state' not in st.session_state:
            self.back_controller = BackController()  # Crear una instancia del controlador de la aplicación
            self.run_page = 'home'
            st.session_state['my_state'] = self  # Guardar el estado de la aplicación en la sesión
        else:
            # Recuperar el estado de la aplicación de la sesión
            self.back_controller = st.session_state.my_state.back_controller
            self.run_page = st.session_state.my_state.run_page

    def main(self):
        """ Maneja cuando se debe dibujar cada página de la aplicación. """
        draw_option_menu(self)
        if self.run_page == 'home':
            draw_home_page(self)
        elif self.run_page == 'event_manager':
            draw_event_manager_page(self)
        elif self.run_page == 'ticket_office':
            draw_ticket_office_page(self)
        elif self.run_page == 'access_management':
            draw_access_management_page(self)

    """ Event manager page """

    def valid_event_data(self, event_data, event_type, fields_to_validate=None):
        """ Valida los datos de un evento.
        al mismo tiempo maneja la interaccion con el usuario si los datos no son válidos."""

        event_fields = self.back_controller.choose_event_fields(event_type)

        # Si no se proporciona una lista de campos para validar, validar todos los campos
        if fields_to_validate is None:
            fields_to_validate = event_fields.keys()

        # Verificar que los datos no estén vacíos
        for field in fields_to_validate:
            if field != "state":  # El campo state no se valida
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
        """  Manneja la interaccion con el usuario al crear el evento validando los datos """

        if self.valid_event_data(event_data, event_type):
            self.back_controller.create_event(event_type, **event_data)
            st.success("event created successfully")

    def edit_event(self, event, new_value, field):
        """ Edita un campo de un evento y actualiza la interfaz. """

        # Crear una copia de los datos actuales del evento
        event_data = vars(event).copy()

        # Actualizar el campo que se está editando con el nuevo valor
        event_data[field] = new_value

        # Validar los datos del evento
        if not self.valid_event_data(event_data, event.type, [field]):
            return
        else:

            self.back_controller.edit_event(event, field, new_value)
            st.success("Evento editado con éxito")

    def delete_event(self, event):
        """ Elimina un evento y actualiza la interfaz. """

        self.back_controller.delete_event(event)

        if not self.back_controller.event_exists(event.date):
            st.session_state.delete_event_interface = False
            st.rerun()

    def draw_input_field_edit(self, field, config):
        """ Dibuja un campo de entrada para editar un evento. """

        if config["type"] == "text":
            return st.text_input("New value")
        elif config["type"] == "date":
            return st.date_input("New value")
        elif config["type"] == "time":
            return st.time_input("New value")
        elif config["type"] == "number":
            if field == "capacity" or field == "amount":
                return st.number_input("New value", step=1)
            else:
                return st.number_input("New value")

    # -----------------------------------------------------------------------------------------------

    """ Ticket office page """

    def valid_ticket_fields(self, other_amount, new_amount, price, ticket_type, event):
        """ Valida los campos de un ticket. """

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

    def edit_ticket_event_gui(self, event, ticket_type, new_value, field):
        """ Edita un ticket de un evento y actualiza la interfaz. """

        ticket = self.back_controller.get_event_ticket(ticket_type, event)
        other_amount = self.get_other_amount(event, ticket.type_ticket)

        new_amount = ticket.amount if field == 'price' else new_value
        price = ticket.price if field == 'amount' else new_value

        # Validar los datos del evento
        if not self.valid_ticket_fields(other_amount, new_amount, price, ticket.type_ticket, event):
            return
        else:
            self.back_controller.update_ticket(ticket, field, new_value)
            st.success("Ticket edit successfully")

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

    def ticket_sale(self, event, ticket_type, ticket_quantity, ticket_price, payment_method, buyer_name, buyer_id,
                    buyer_email, buyer_age, how_did_you_know):

        #  Verificaciones de la informacion obtenida del formulario de venta de boletas
        if (buyer_name.strip() == "" or buyer_id.strip() == "" or buyer_email.strip() == "" or buyer_age <= 0
                or ticket_quantity <= 0):
            st.warning("Please, complete all the fields")

        else:
            # Creamos el ticket vendido para guardarlo en los datos
            sold_tickets = self.back_controller.create_sold_tickets(event, ticket_type, buyer_name, buyer_id,
                                                                    buyer_email, buyer_age, ticket_quantity)

            # Verificamos si el ticket si se creo correctamente en el sistema
            if self.back_controller.verify_sold_tickets(event, sold_tickets):
                st.success("sale completed successfully")

                # Controlar los tickets disponibles tomando en cuenta los tickes que se pidieron comprar
                self.back_controller.control_tickets_available(event, ticket_type, ticket_quantity)

                # Verifica si las boletas disponibles son cero despues del control para actualizar el estado
                self.back_controller.update_state_event_to_sold_out(event)

                # Acualizar la variable para controlar que ya se incio la venta de boletas de ese tipo con almenos una
                event.bool_sold_ticket[ticket_type] = True

                # Manejar los datos del reporte del evento
                event.report_data.increment_sold_by_ticket_type(ticket_type, ticket_quantity)
                event.report_data.increment_income_by_ticket_type(ticket_type, (ticket_price * ticket_quantity))
                event.report_data.increment_income_by_payment_method(payment_method, (ticket_price * ticket_quantity))
                event.report_data.add_buyer_info(buyer_age, how_did_you_know, payment_method, buyer_email)
                event.report_data.increment_income_by_event_type(event.type, (ticket_price * ticket_quantity))

                print(event.report_data.tickets_sold_by_ticket_type)
                print(event.report_data.total_income_by_ticket_type)
                print(event.report_data.total_income_by_payment_method)
                print(event.report_data.buyers_demographic)
                print(event.report_data.income_by_event_type)

                print(f" estado del evento: {event.state}")

                # Generamos el PDF de la boleta
                self.back_controller.generate_ticket_pdf(event, sold_tickets, f"{buyer_id}.pdf")

                # Abrir el PDF en el navegador web
                webbrowser.open_new(f"{buyer_id}.pdf")

                # Actualizacion de las paginas despues de una venta
                st.session_state.sale_ticket_form = False
                st.session_state.confirm_sale = False
                st.rerun()

    def close_ticket_sale(self, event_to_sale_ticket, type_ticket):
        """ Cierra la venta de boletas de un evento.  """

        #  Obtenemos la boleta que se va a cerrar
        ticket = self.back_controller.get_event_ticket(type_ticket, event_to_sale_ticket)

        #  Actualizamos su disponibilidad a cero
        self.back_controller.update_ticket(ticket, "amount_available", 0)

        #  Actualizar que ya se vendio al menos una boleta de ese tipo
        event_to_sale_ticket.bool_sold_ticket[type_ticket] = True

        #  Actualizar el evento en caso de que se haya vendido todas las boletas
        self.back_controller.update_state_event_to_sold_out(event_to_sale_ticket)

        st.session_state.sale_ticket_form = False
        st.session_state.sale_ticket = False
        st.rerun()

    def verify_amount_tickets(self, event, ticket_type, ticket_quantity):
        """ Verifica si la cantidad de boletas solicitadas no excede la cantidad disponible. """
        amount_tickets_available = event.tickets[0].amount
        if ticket_type == "regular":
            amount_tickets_available = event.tickets[1].amount

        if ticket_quantity > amount_tickets_available:
            st.error(f"The amount of {ticket_type} tickets requested exceeds the available amount")
            return False
        else:
            return True

    # -----------------------------------------------------------------------------------------------

    """ Access management page """

    def verify_access(self, event, ticket_code):
        """ Verifica si el código de un ticket es válido. """
        sold_ticket = self.back_controller.get_sold_ticket_by_code(event, ticket_code)
        if sold_ticket is not None:
            st.success(f"Access granted, welcome {sold_ticket.buyer_name}")
            return True
        else:
            st.error(f"Access denied, {ticket_code} is not registered")
            return False
