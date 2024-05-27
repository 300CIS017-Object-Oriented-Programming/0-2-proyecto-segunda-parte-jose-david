import streamlit as st
import pandas as pd
import plotly.express as px


def draw_dashboard(gui_controller, start_date, end_date):
    graph1, graph2 = st.columns([2, 2])
    st.title("Welcome to the event manager")
    st.write("This is the dashboard, here you can manage the events and the access to them")
    with graph1:
        # Cantidad de eventos creados por tipo
        event_types = gui_controller.back_controller.get_event_types_in_date_range(start_date, end_date)
        if event_types is None:
            st.error("No hay eventos disponibles.")
        else:
            # Aquí puedes continuar con el procesamiento de los tipos de eventos
            df = pd.DataFrame({
                'event_type': event_types,
            })

            # Contar la cantidad de cada tipo de evento
            df_count = df['event_type'].value_counts().reset_index()
            df_count.columns = ['event_type', 'count']

            # Crear el gráfico de barras con Plotly
            fig = px.bar(df_count, x='event_type', y='count', color='event_type', title='Number of events by type')

            # Mostrar el gráfico en Streamlit
            st.plotly_chart(fig, use_container_width=True)
    with graph2:
        pass


