# Importando la biblioteca requerida
import streamlit as st
from settings import SEPARATOR


# Función para dibujar la interfaz para crear un evento
def draw_create_event_interface(gui_controller, event_type, close_button_col):
    event_fields = gui_controller.back_controller.choose_event_fields(event_type)
    # Creando un formulario para el evento
    with st.form(key=f'{event_type}_form'):
        # Creando dos columnas para el formulario
        col1, col2 = st.columns(2)
        # Dividiendo los campos del evento en dos mitades
        half = len(event_fields) // 2
        fields = list(event_fields.items())
        # Mostrando la primera mitad de los campos en la primera columna
        for i in range(half):
            field, config = fields[i]
            if field != "state":  # Omitir el campo de estado
                with col1:
                    draw_input_field(field, config)
        # Mostrando la segunda mitad de los campos en la segunda columna
        for i in range(half, len(fields)):
            field, config = fields[i]
            if field != "state":  # Omitir el campo de estado
                with col2:
                    draw_input_field(field, config)

        # Si el formulario es enviado, crear el evento con los datos ingresados
        if st.form_submit_button('Create event'):
            event_data = {field: st.session_state[field] for field, _ in event_fields.items() if
                          field != "state"}  # Omitir el campo de estado
            gui_controller.create_event(event_type, event_data)
    with close_button_col:
        st.write("")
        st.write("")
        if st.button('❌', key="close_create_event"):
            st.session_state.create_event = False
            st.rerun()


# Función para dibujar la interfaz para el evento buscado
def draw_searched_event_interface(gui_controller, event_date_consult, close_button_col):
    if "edit_event_interface" not in st.session_state:
        st.session_state.edit_event_interface = False
    if "delete_event_interface" not in st.session_state:
        st.session_state.delete_event_interface = False

    searched_event = gui_controller.back_controller.get_event_by_date(event_date_consult)
    if searched_event is not None:
        display_event(gui_controller, searched_event)

        empty, edit_event_button_col, delete_event_button_col, empty = st.columns([0.9, 1, 1, 1])

        with edit_event_button_col:
            if st.button("Edit event"):
                st.session_state.edit_event_interface = True
                st.session_state.delete_event_interface = False
        with delete_event_button_col:
            if st.button("Delete event"):
                st.session_state.delete_event_interface = True
                st.session_state.edit_event_interface = False

        if st.session_state.edit_event_interface:
            if searched_event.state == "realized":
                st.error("You cannot edit an event that has already been realized.")
            else:
                draw_edit_event_interface(gui_controller, searched_event)
        if st.session_state.delete_event_interface:
            st.session_state.edit_event_interface = False
            draw_delete_event_interface(gui_controller, searched_event)
    else:
        st.error("No event was found on the selected date.")
    with close_button_col:
        st.write("")  # por motivos esteticos
        st.write("")
        if st.button('❌', key="close_search_event"):  # FIXME: cambiar a un icono X
            st.session_state.search_event = False
            st.session_state.edit_event_interface = False  # Cierra la interfaz de edición
            st.session_state.delete_event_interface = False  # Cierra la interfaz de eliminación
            st.rerun()


# Función para dibujar el campo de entrada basado en su tipo
def draw_input_field(field, config):
    if config["type"] == "text":
        st.text_input(config["label"], key=field)
    elif config["type"] == "date":
        st.date_input(config["label"], key=field)
    elif config["type"] == "time":
        st.time_input(config["label"], key=field)
    elif config["type"] == "number":
        if field == "capacity":
            st.number_input(config["label"], step=1, key=field)
        else:
            st.number_input(config["label"], key=field)


# Función para mostrar un evento
def display_event(gui_controller, event):
    st.markdown("<br>", unsafe_allow_html=True)

    # Convirtiendo el objeto de evento en un diccionario de atributos
    event_dict = dict(vars(event))
    # Obteniendo el diccionario de campos correspondiente al tipo de evento
    event_fields = gui_controller.back_controller.choose_event_fields(event.type)
    # Creando tres columnas
    col1, col2, col3 = st.columns(3)


    # Dividiendo los campos en tres listas
    fields = list(event_fields.items())
    third = len(fields) // 3
    fields1 = fields[:third]
    fields2 = fields[third:2 * third]
    fields3 = fields[2 * third:]

    # Mostrando los campos en las tres columnas

    for field, config in fields1:
        with col1:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields2:
        with col2:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields3:
        with col3:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")

    st.markdown(SEPARATOR, unsafe_allow_html=True)


# Función para dibujar la biblioteca de eventos
def draw_events_library(gui_controller, close_button_col):
    # Creando un cuadro de selección para seleccionar el tipo de evento
    col0, col1 = st.columns([0.5, 2.5])
    with col0:
        event_type = st.selectbox("Filter by event type", ["Select...", "bar", "philanthropic", "theater"])

    # Si se ha seleccionado un tipo de evento
    if event_type != "Select...":
        # Obteniendo todos los eventos de este tipo
        events = gui_controller.back_controller.get_events_by_type(event_type)

        # Si no hay eventos de este tipo, mostrar un mensaje
        if events is None:
            with col0:
                st.info(f"there are still no events of type {event_type}.")

            # Para cada evento, mostrarlo en una nueva columna
        else:
            for event in events:
                with col1:
                    display_event(gui_controller, event)
    with close_button_col:
        if st.button("❌"):  # FIXME: cambiar a un icono X
            st.session_state.show_event_library = False
            st.rerun()


# Función para dibujar la interfaz para editar un evento
def draw_edit_event_interface(gui_controller, searched_event):
    # Obteniendo los campos del evento buscado
    select_field_col, input_col, apply_button_col = st.columns([1, 1.5, 1.5])
    event_fields = gui_controller.back_controller.choose_event_fields(searched_event.type)

    # Creando una lista de opciones para el cuadro de selección
    options = [field for field, _ in event_fields.items()]

    # Creando el cuadro de selección con las opciones
    with select_field_col:
        selected_field = st.selectbox("Select the field to edit", options)

    with input_col:
        # Si el campo seleccionado es "state", dibujar un cuadro de selección con los estados permitidos
        if selected_field == "state":
            new_value = st.selectbox("New value", event_fields[selected_field]["options"])
        else:
            # Creando un campo de entrada para el nuevo valor
            new_value = gui_controller.draw_input_field_edit(selected_field, event_fields[selected_field])
        st.info("Press search again to notice the changes")
    with apply_button_col:
        st.write("")
        st.write("")
        if st.button("Apply changes"):
            gui_controller.edit_event(searched_event, new_value, selected_field)


# Función para dibujar la interfaz para eliminar un evento
def draw_delete_event_interface(gui_controller, searched_event):
    st.warning("Are you sure you want to delete this event?")
    empty, yes_button_col, no_button_col, empty = st.columns([1.5, 0.7, 0.7, 2])
    with yes_button_col:
        if st.button("Confirm"):
            gui_controller.delete_event(searched_event)

    with no_button_col:
        if st.button("❌"):
            st.session_state.delete_event_interface = False
            st.experimental_rerun()

# Función para dibujar el campo de entrada para editar un evento basado en su tipo
