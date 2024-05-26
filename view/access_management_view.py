import streamlit as st


def draw_register_access_interface(gui_controller, event_today, close_button):
    empy, info_col, code_input_col, verify_button_col, empty = st.columns([1, 1, 1, 1, 1])
    if not event_today.bool_sold_out["presale"] and not event_today.bool_sold_out["regular"]:
        st.error("The ticket office for the event is still active. Close the ticket sales to register the entry")
    elif len(event_today.sold_tickets) == 0:
        st.success("All event entries registered.")
    else:
        with info_col:
            st.write(f"Tickets per register: {len(event_today.sold_tickets)}")
        with code_input_col:
            code_input_to_access = st.text_input("Enter the ticket code")
        with verify_button_col:
            if st.button("verify"):
                if code_input_to_access:
                    if gui_controller.verify_access(event_today, code_input_to_access):
                        gui_controller.back_controller.register_access(event_today, code_input_to_access)

    with close_button:
        if st.button("Close", key="close_access_management"):
            st.session_state.access_management = False
            st.rerun()
