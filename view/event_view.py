import streamlit as st


def draw_create_event_interface(gui_controller, event_type, event_fields):
    print(f"event type create {event_type}")
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


def display_event(gui_controller, event):
    # Convertir el objeto de evento en un diccionario de atributos
    event_dict = vars(event)

    # Obtener el diccionario de campos correspondiente al tipo de evento
    event_fields = gui_controller.choose_event_fields(event.type)
    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Dividir los campos en tres listas
    fields = list(event_fields.items())
    third = len(fields) // 3
    fields1 = fields[:third]
    fields2 = fields[third:2 * third]
    fields3 = fields[2 * third:]

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


def draw_events_library(gui_controller):
    # Crear un select box para seleccionar el tipo de evento
    col0, col1 = st.columns([0.5, 2.5])
    with col0:

        event_type = st.selectbox("Filtrar por tipo de evento", ["Seleccione...", "bar", "philanthropic", "theater"])

    # Si se ha seleccionado un tipo de evento

    if event_type != "Seleccione...":
        # Obtener todos los eventos de este tipo
        events = gui_controller.back_controller.get_events_by_type(event_type)

        # Si no hay eventos de este tipo, mostrar un mensaje
        if events is None:
            with col0:
                st.info(f"aun no hay eventos de tipo {event_type}.")

            # Para cada evento, mostrarlo en una nueva columna
        else:
            for event in events:
                with col1:
                    display_event(gui_controller, event)


def draw_searched_event_interface(gui_controller, event_date_consult):
    searched_event = gui_controller.back_controller.get_event_by_date(event_date_consult)
    if searched_event is not None:
        display_event(gui_controller, searched_event)

        empty, edit_event_button_col, delete_event_button_col, empty = st.columns([0.9, 1, 1, 1])

        with edit_event_button_col:

            if st.button("Editar evento"):
                st.session_state.edit_event_interface = True
        with delete_event_button_col:
            if st.button("Eliminar evento"):
                st.session_state.delete_event_interface = True

        if st.session_state.edit_event_interface:
            draw_edit_event_interface(gui_controller, searched_event)
        if st.session_state.delete_event_interface:
            draw_delete_event_interface(gui_controller, searched_event)
    else:
        st.error("No se encontró ningún evento en la fecha seleccionada.")


def draw_edit_event_interface(gui_controller, searched_event):
    # Obtener los campos del evento buscado
    select_field_col, input_col, apply_button_col = st.columns([1, 1.5, 1.5])
    event_fields = gui_controller.choose_event_fields(searched_event.type)

    # Crear una lista de opciones para el selectbox
    options = [field for field, _ in event_fields.items()]

    # Crear el selectbox con las opciones
    with select_field_col:
        selected_field = st.selectbox("Seleccione el campo a editar", options)

    with input_col:
        with input_col:
            # Crear un campo de entrada para el nuevo valor
            new_value = draw_input_field_edit(selected_field, event_fields[selected_field])
            st.info("Oprima buscar de nuevo para notar los cambios")
        with apply_button_col:
            st.write("")
            st.write("")
            if st.button("Aplicar cambios"):
                if new_value is not None and new_value != "":
                    gui_controller.edit_event(searched_event, new_value, selected_field)
                else:
                    st.warning("Por favor ingrese un valor válido")


def draw_delete_event_interface(gui_controller, searched_event):
    st.warning("¿Está seguro que desea eliminar este evento?")
    empty, yes_button_col, no_button_col, empty = st.columns([1.5, 0.7, 0.7, 2])
    with yes_button_col:
        if st.button("Confirmar"):
            gui_controller.delete_event(searched_event)

    with no_button_col:
        if st.button("Cerrar"):
            st.session_state.delete_event_interface = False
            st.experimental_rerun()


def draw_input_field_edit(field, config):
    if config["type"] == "text":
        return st.text_input("Nuevo valor")
    elif config["type"] == "date":
        return st.date_input("Nuevo valor")
    elif config["type"] == "time":
        return st.time_input("Nuevo valor")
    elif config["type"] == "number":
        return st.number_input("Nuevo valor")
