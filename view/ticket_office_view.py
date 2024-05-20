import streamlit as st

""" Ticket management interface """


def draw_ticket_management_interface(gui_controller):
    # Initialize session state variables if they don't exist
    if "edit_ticket" not in st.session_state:
        st.session_state.edit_ticket = False

    search_event_col, type_event_col = st.columns([1, 1])
    event_dates = gui_controller.back_controller.get_all_event_dates()

    with search_event_col:
        event_date_to_edit_ticket = st.selectbox("Enter the date of the event", options=event_dates)

    if event_date_to_edit_ticket is None:
        st.info("There are no events to edit")
    else:
        with type_event_col:
            # Select the type of ticket
            type_ticket = st.selectbox("Select the type of ticket", ["Select...", "presale", "regular"])

        event_to_edit_ticket = gui_controller.back_controller.get_event_by_date(event_date_to_edit_ticket)

        if type_ticket != "Select...":
            draw_assign_ticket_price_interface(gui_controller, type_ticket, event_to_edit_ticket,
                                               search_event_col, type_event_col)  # view/ticket_office_view

    if st.button("Close"):
        st.session_state.ticket_management = False
        st.session_state.edit_ticket = False
        st.rerun()


def draw_assign_ticket_price_interface(gui_controller, type_ticket, event_to_edit_ticket,
                                       search_event_col, type_event_col):
    ticket = gui_controller.back_controller.get_event_ticket(type_ticket, event_to_edit_ticket)

    if ticket is not None:
        st.write(f"The actual {type_ticket} price of the event {event_to_edit_ticket.name} ticket"
                 f" is: {ticket.price} USD")

        """ Edit ticket price """

        if st.button("Edit ticket"):
            st.session_state.edit_ticket = True
        if st.session_state.edit_ticket:
            draw_edit_price_ticket_interface(gui_controller, event_to_edit_ticket, type_ticket)
            # view/ticket_office_view

    else:  # If the ticket has not been assigned yet

        """ Assign ticket price """

        with search_event_col:
            st.info(f"The {type_ticket} price has not been assigned yet")
        with type_event_col:
            price = st.number_input("Enter the price of the ticket")
            if st.button("Assign ticket"):
                valid_price = gui_controller.back_controller.bool_valid_price(event_to_edit_ticket, type_ticket, price)
                if valid_price:
                    gui_controller.back_controller.update_ticket_price(event_to_edit_ticket, type_ticket, price)
                    st.rerun()
                else:
                    st.warning("The price for non-philanthropic events should not be zero. Please consider setting a "
                               "price.")


def draw_edit_price_ticket_interface(gui_controller, event_to_edit_ticket, ticket_type):
    empty, price_input_col, empty = st.columns([0.9, 2.5, 1])
    with price_input_col:
        new_price = st.number_input("Enter the new price of the ticket")
    empty, edit_price_button_col, cancel_edit_col, empty = st.columns([0.9, 0.5, 0.5, 1])
    with edit_price_button_col:

        if st.button("Edit"):
            # Validate the price
            valid_price = gui_controller.back_controller.bool_valid_price(event_to_edit_ticket, ticket_type,
                                                                          new_price)
            if valid_price:
                gui_controller.back_controller.update_ticket_price(event_to_edit_ticket, ticket_type, new_price)
                st.session_state.edit_ticket = False
                st.rerun()
            else:
                st.warning("invalid price")

    with cancel_edit_col:

        if st.button("Cancel"):
            st.session_state.edit_ticket = False
            st.rerun()


""" Sales management interface """


def draw_sales_tickets_manager_interface(gui_controller):
    pass