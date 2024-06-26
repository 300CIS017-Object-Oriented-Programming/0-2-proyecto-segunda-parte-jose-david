import streamlit as st
from settings import TICKET_EVENT_FIELDS, OPTIONS_MARKETING, OPTIONS_METHOD

""" Ticket management interface """


def draw_ticket_management_interface(gui_controller, close_button_col):
    #  Inicializar las variables de estado de la sesión si no existen
    if "edit_ticket" not in st.session_state:
        st.session_state.edit_ticket = False

    search_event_col, type_ticket_col = st.columns([1, 1])
    # Obtener todas las fechas de los eventos para mostrar en el selectbox
    event_dates = gui_controller.back_controller.get_all_event_dates()

    with search_event_col:
        event_date_to_assign_ticket = st.selectbox("Enter the date of the event", options=event_dates,
                                                   key="event_date_to_edit_ticket")

    if event_date_to_assign_ticket is None:
        st.info("There are no events to edit")
    else:
        with type_ticket_col:
            # Select the type of ticket
            type_ticket = st.selectbox("Select the type of ticket", ["Select...", "presale", "regular"])

        # Obtener el evento por la fecha
        event_to_management_ticket = gui_controller.back_controller.get_event_by_date(event_date_to_assign_ticket)

        if type_ticket != "Select...":
            if event_to_management_ticket.bool_sold_ticket[type_ticket]:
                st.info("The tickets for this event have already been sold")
            else:
                draw_assign_ticket_price_interface(gui_controller, type_ticket, event_to_management_ticket,
                                                   search_event_col, type_ticket_col)  # view/ticket_office_view
    with close_button_col:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        if st.button("❌", key="close_ticket_management"):
            st.session_state.ticket_management = False
            st.session_state.edit_ticket = False
            st.rerun()


def draw_assign_ticket_price_interface(gui_controller, type_ticket, event_to_management_ticket,
                                       search_event_col, type_event_col):
    if "edit_ticket" not in st.session_state:
        st.session_state.edit_ticket = False

    # Obtener la cantidad de tickets asignados para presale y regular para mostrarle al usuario
    presale_amount = gui_controller.back_controller.get_amount_ticket_assigned("presale", event_to_management_ticket)
    regular_amount = gui_controller.back_controller.get_amount_ticket_assigned("regular", event_to_management_ticket)

    #  Obtener el ticket para el evento
    ticket = gui_controller.back_controller.get_event_ticket(type_ticket, event_to_management_ticket)

    """ Assign ticket """
    if ticket is None:
        with search_event_col:
            st.info(f"The {type_ticket} tickets has not been assigned yet, {int(event_to_management_ticket.capacity)} "
                    f"tickets available. {presale_amount} assigned for presale "
                    f" {regular_amount} assigned for regular")

        with type_event_col:
            price_col, amount_col = st.columns([1, 1])  # columns

            with price_col:
                price = st.number_input("Enter the price of the ticket")
            with amount_col:
                amount = st.number_input("Enter the amount of tickets", step=1)

            if st.button("Assign ticket"):
                #  Asignar el ticket al evento
                gui_controller.assign_ticket_to_event(event_to_management_ticket, type_ticket, price, amount)
                st.session_state.edit_ticket = False

    else:
        st.write(f"The {type_ticket} ticket has been assigned with a price of {ticket.price} and an amount "
                 f"of {ticket.amount} tickets")

        if st.button("Edit ticket"):
            st.session_state.edit_ticket = True

        if st.session_state.edit_ticket:
            # Dibujar la interfaz para editar el ticket
            draw_edit_ticket_interface(gui_controller, event_to_management_ticket, type_ticket)


def draw_edit_ticket_interface(gui_controller, event_to_edit_ticket, ticket_type):
    if "confirm_edit" not in st.session_state:
        st.session_state.confirm_edit = False

    select_field_col, input_col, apply_button_col = st.columns([1, 1.5, 1.5])  # Columnas
    #  Obtener los campos del ticket del la configuracion en settings.py
    options = [field for field, _ in TICKET_EVENT_FIELDS.items()]

    with select_field_col:
        selected_field = st.selectbox("Select the field to edit", options)
    with input_col:
        # Si el campo seleccionado es "state", dibujar un cuadro de selección con los estados permitidos
        new_value = gui_controller.draw_input_field_edit(selected_field, TICKET_EVENT_FIELDS[selected_field])

    with apply_button_col:
        st.write("")
        st.write("")
        confirm_edit = False
        if st.button("Apply changes"):
            confirm_edit = True
    if confirm_edit:
        # Editar el ticket
        gui_controller.edit_ticket_event_gui(event_to_edit_ticket, ticket_type, new_value, selected_field)


""" Sales management interface """


def draw_ticket_sales_management_interface(gui_controller, close_button_col):
    # Initialize session state variables if they don't exist
    if "sale_ticket" not in st.session_state:
        st.session_state.sale_ticket = False

    st.markdown("<br> <br>", unsafe_allow_html=True)
    empty, search_event_col, ticket_type_col, button_col = st.columns([0.6, 0.6, 0.5, 0.9])  # Columns
    event_dates = gui_controller.back_controller.get_all_event_dates()

    with search_event_col:
        event_date_to_sale_ticket = st.selectbox("Enter the date of event", options=event_dates,
                                                 key="event_date_to_sale_ticket")

    event_to_sale_ticket = gui_controller.back_controller.get_event_by_date(event_date_to_sale_ticket)

    if event_date_to_sale_ticket is None:
        st.info("There are no events to edit")
    else:
        with ticket_type_col:
            ticket_type = st.selectbox("Select the type of ticket", ["presale", "regular"])

            with button_col:
                st.write(" ")
                st.write(" ")
                if st.button("Select"):
                    st.session_state.sale_ticket = True

        if st.session_state.sale_ticket:
            if gui_controller.back_controller.get_event_ticket(ticket_type, event_to_sale_ticket) is None:
                st.info(f"The {ticket_type} ticket has not been assigned yet")
            else:
                draw_sale_ticket_interface(gui_controller, event_to_sale_ticket, ticket_type)
            # view/ticket_office_view
    with close_button_col:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        if st.button("❌", key="close_ticket_sales_management"):
            st.session_state.ticket_sale_management = False
            st.rerun()


def draw_sale_ticket_interface(gui_controller, event_to_sale_ticket, type_ticket):
    if "sale_ticket_form" not in st.session_state:
        st.session_state.sale_ticket_form = False

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1.2, 1, 1.5, 1])  # Columns
    # Obtener el ticket del evento
    ticket = gui_controller.back_controller.get_event_ticket(type_ticket, event_to_sale_ticket)

    if ticket.amount_available == 0:
        st.info(f"{type_ticket} tickets are sold out")
    else:
        with col2:
            st.write(f"Price ticket: {ticket.price} USD")
            st.write(f"Event capacity: {event_to_sale_ticket.capacity}")

        with col3:
            if type_ticket == "presale":
                st.write(f"presale tickets avaliable: {event_to_sale_ticket.tickets[0].amount_available}")
            elif type_ticket == "regular":
                st.write(f"regular tickets avaliable: {event_to_sale_ticket.tickets[1].amount_available}")
            st.write(f"Total tickets sold: {len(event_to_sale_ticket.sold_tickets)}")

        st.markdown("<br>", unsafe_allow_html=True)

        empty, button_sale_col, button_sold_out, close_button, empty = st.columns([1.3, 1, 1, 1, 0.2])  # Columns

        with button_sale_col:
            if st.button("Sale ticket"):
                st.session_state.sale_ticket_form = True
        with button_sold_out:
            if st.button(f"close {type_ticket}"):
                # Cerrar la venta de tickets
                gui_controller.close_ticket_sale(event_to_sale_ticket, type_ticket)
        if st.session_state.sale_ticket_form:
            # Dibujar el formulario de venta de tickets
            draw_sale_ticket_form(gui_controller, event_to_sale_ticket, type_ticket, close_button)


def draw_sale_ticket_form(gui_controller, event_to_sale_ticket, type_ticket, close_button):
    if "confirm_sale" not in st.session_state:
        st.session_state.confirm_sale = False

    empty, form_col, empty = st.columns([0.8, 2.5, 1])  # Columns
    # Asignar el valor del tickete correspondiente
    ticket = gui_controller.back_controller.get_event_ticket(type_ticket, event_to_sale_ticket)
    ticket_price = ticket.price

    with form_col:
        with st.form(key='sale_ticket_formefasfaef'):

            # Campos del formulario
            buyer_name = st.text_input("Enter name")
            buyer_id = st.text_input("Enter ID")
            buyer_email = st.text_input("Enter email")  # Email del comprador
            buyer_age = st.number_input("Enter age", step=1)
            ticket_quantity = st.number_input("Enter ticket quantity", step=1)  # Cantidad de boletos
            how_did_you_know = st.radio("How did you know about the event?", OPTIONS_MARKETING)
            payment_method = st.radio("Select the payment method", OPTIONS_METHOD)
            complimentary_ticket = st.radio("Complimentary ticket", ["Yes", "No"])

            submit_button = st.form_submit_button(label="Sale")

            if submit_button:
                st.session_state.confirm_sale = True

            if st.session_state.confirm_sale:
                #  Verificar si la cantidad de tickets es válida
                if gui_controller.verify_amount_tickets(event_to_sale_ticket, type_ticket, ticket_quantity):
                    if complimentary_ticket == "Yes":  # Si el ticket es cortesía
                        type_ticket = 'complementary'
                        ticket_price = 0
                    #  Vender el ticket
                    gui_controller.ticket_sale(event_to_sale_ticket, type_ticket, ticket_quantity, ticket_price
                                               , payment_method, buyer_name, buyer_id, buyer_email, buyer_age,
                                               how_did_you_know)
