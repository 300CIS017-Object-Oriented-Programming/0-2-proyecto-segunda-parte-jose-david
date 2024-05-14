import streamlit as st
from settings import BAR_EVENT_FIELDS, THEATER_EVENT_FIELDS, PHILANTHROPIC_EVENT_FIELDS


def draw_create_event_interface(gui_controller, event_type, event_fields):
    with st.form(key=f'{event_type}_form'):
        col1, col2 = st.columns(2)
        half = len(event_fields) // 2
        fields = list(event_fields.items())
        for i in range(half):
            field, config = fields[i]
            with col1:
                draw_input_field(field, config)
        for i in range(half, len(fields)):
            field, config = fields[i]
            with col2:
                draw_input_field(field, config)

        if st.form_submit_button('Enviar'):
            event_data = {field: st.session_state[field] for field, _ in event_fields.items()}
            gui_controller.create_event(event_type, event_data)


def draw_input_field(field, config):
    if config["type"] == "text":
        st.text_input(config["label"], key=field)
    elif config["type"] == "date":
        st.date_input(config["label"], key=field)
    elif config["type"] == "time":
        st.time_input(config["label"], key=field)
    elif config["type"] == "number":
        st.number_input(config["label"], key=field)


def choose_event_fields(event_type):
    event_fields = None
    if event_type == "bar":
        event_fields = BAR_EVENT_FIELDS
    elif event_type == "philanthropic":
        event_fields = PHILANTHROPIC_EVENT_FIELDS
    elif event_type == "theater":
        event_fields = THEATER_EVENT_FIELDS
    return event_fields
