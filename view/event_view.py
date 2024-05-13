import streamlit as st


def draw_create_event_interface(gui_controller, event_type, event_fields):
    with st.form(key=f'{event_type}_form'):
        for field, config in event_fields.items():
            if config["type"] == "text":
                st.text_input(config["label"], key=field)
            elif config["type"] == "date":
                st.date_input(config["label"], key=field)
            elif config["type"] == "time":
                st.time_input(config["label"], key=field)
            elif config["type"] == "number":
                st.number_input(config["label"], key=field)

        if st.form_submit_button('Create'):
            event_data = {field: st.session_state[field] for field in event_fields}
            success = gui_controller.create_event(event_type, event_data)
            if success:
                st.success("El evento ha sido creado y guardado exitosamente.")
            else:
                st.error("Ya existe un evento en la fecha seleccionada.")
