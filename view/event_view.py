# Importing the required library
import streamlit as st


# Function to draw the interface for creating an event
def draw_create_event_interface(gui_controller, event_type, event_fields):

    # Creating a form for the event
    with st.form(key=f'{event_type}_form'):
        # Creating two columns for the form
        col1, col2 = st.columns(2)
        # Splitting the event fields into two halves
        half = len(event_fields) // 2
        fields = list(event_fields.items())
        # Displaying the first half of the fields in the first column
        for i in range(half):
            field, config = fields[i]
            with col1:
                draw_input_field(field, config)
        # Displaying the second half of the fields in the second column
        for i in range(half, len(fields)):
            field, config = fields[i]
            with col2:
                draw_input_field(field, config)

        # If the form is submitted, create the event with the entered data
        if st.form_submit_button('Enviar'):
            event_data = {field: st.session_state[field] for field, _ in event_fields.items()}
            gui_controller.create_event(event_type, event_data)


# Function to draw the input field based on its type
def draw_input_field(field, config):
    if config["type"] == "text":
        st.text_input(config["label"], key=field)
    elif config["type"] == "date":
        st.date_input(config["label"], key=field)
    elif config["type"] == "time":
        st.time_input(config["label"], key=field)
    elif config["type"] == "number":
        st.number_input(config["label"], key=field)


# Function to display an event
def display_event(gui_controller, event):
    # Converting the event object into a dictionary of attributes
    event_dict = vars(event)

    # Getting the dictionary of fields corresponding to the event type
    event_fields = gui_controller.choose_event_fields(event.type)
    # Creating three columns
    col1, col2, col3 = st.columns(3)

    # Splitting the fields into three lists
    fields = list(event_fields.items())
    third = len(fields) // 3
    fields1 = fields[:third]
    fields2 = fields[third:2 * third]
    fields3 = fields[2 * third:]

    # Displaying the fields in the three columns
    for field, config in fields1:
        with col1:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields2:
        with col2:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")
    for field, config in fields3:
        with col3:
            st.write(f"{config['label']}: {event_dict.get(field, '')}")


# Function to draw the events library
def draw_events_library(gui_controller):
    # Creating a select box to select the event type
    col0, col1 = st.columns([0.5, 2.5])
    with col0:
        event_type = st.selectbox("Filtrar por tipo de evento", ["Seleccione...", "bar", "philanthropic", "theater"])

    # If an event type has been selected
    if event_type != "Seleccione...":
        # Getting all the events of this type
        events = gui_controller.back_controller.get_events_by_type(event_type)

        # If there are no events of this type, display a message
        if events is None:
            with col0:
                st.info(f"aun no hay eventos de tipo {event_type}.")

            # For each event, display it in a new column
        else:
            for event in events:
                with col1:
                    display_event(gui_controller, event)


# Function to draw the interface for the searched event
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


# Function to draw the interface for editing an event
def draw_edit_event_interface(gui_controller, searched_event):
    # Getting the fields of the searched event
    select_field_col, input_col, apply_button_col = st.columns([1, 1.5, 1.5])
    event_fields = gui_controller.choose_event_fields(searched_event.type)

    # Creating a list of options for the selectbox
    options = [field for field, _ in event_fields.items()]

    # Creating the selectbox with the options
    with select_field_col:
        selected_field = st.selectbox("Seleccione el campo a editar", options)

    with input_col:
        with input_col:
            # Creating an input field for the new value
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


# Function to draw the interface for deleting an event
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


# Function to draw the input field for editing an event based on its type
def draw_input_field_edit(field, config):
    if config["type"] == "text":
        return st.text_input("Nuevo valor")
    elif config["type"] == "date":
        return st.date_input("Nuevo valor")
    elif config["type"] == "time":
        return st.time_input("Nuevo valor")
    elif config["type"] == "number":
        return st.number_input("Nuevo valor")
