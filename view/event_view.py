import streamlit as st


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


def display_event(gui_controller, event, event_type):
    # Convertir el objeto de evento en un diccionario de atributos
    event_dict = vars(event)

    # Obtener el diccionario de campos correspondiente al tipo de evento
    event_fields = gui_controller.choose_event_fields(event_type)

    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Dividir los campos en tres listas
    fields = list(event_fields.items())
    third = len(fields) // 3
    fields1 = fields[:third]
    fields2 = fields[third:2*third]
    fields3 = fields[2*third:]

    # Mostrar los campos en las tres columnas
    for field, config in fields1:
        with col1:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields2:
        with col2:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields3:
        with col3:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")