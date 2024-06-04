import streamlit as st
import pandas as pd
import plotly.express as px


def draw_dashboard(gui_controller):
    """ Dibujar el dashboard de la aplicacion """

    st.markdown("## Dashboard 📊")
    st.write("put a date range")

    # Columnas
    empty, start_date_col, end_date_col, button_col, close_button_col, empty = st.columns([2, 1, 1, 1, 1, 1])

    # Recibir fechas
    with start_date_col:
        start_date = st.date_input("star_date")
    with end_date_col:
        end_date = st.date_input("end_date")
    with button_col:
        st.write("")
        st.write("")
        if st.button("show dashboard"):
            st.session_state.dashboard = True

    if st.session_state.dashboard:
        graph1, graph2 = st.columns([2, 2])
        st.title("Welcome to the event manager")
        st.write("This is the dashboard, here you can manage the events and the access to them")
        with graph1:
            # Cantidad de eventos creados por tipo
            event_types = gui_controller.back_controller.get_event_types_in_date_range(start_date, end_date)
            if event_types is None:
                st.error("No hay eventos disponibles.")
            else:
                # Crear un DataFrame con los tipos de eventos
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
            # Obtener los eventos en el rango de fechas
            events = gui_controller.back_controller.get_events_in_date_range(start_date, end_date)

            # Inicializar un DataFrame con ceros para cada tipo de evento
            total_income_by_event_type = pd.DataFrame({'bar': [0], 'philanthropic': [0], 'theater': [0]})

            # Para cada evento, obtener el objeto Report y sumar los ingresos por tipo de evento
            for event in events.values():
                report = event.report_data
                total_income_by_event_type.update(report.income_by_event_type)

            # Mostrar los ingresos totales por tipo de evento
            for event_type in total_income_by_event_type.columns:
                total_income = total_income_by_event_type.loc[0, event_type]
                if total_income == 0:
                    st.write(f"No hay ingresos para el tipo de evento {event_type}.")
                else:
                    st.write(f"Los ingresos totales para el tipo de evento {event_type} son: {total_income}")

        with close_button_col:
            st.write("")
            st.write("")
            if st.button("close", key="close_dashboard"):
                st.session_state.dashboard = False
                st.rerun()


def draw_sales_report_interface(gui_controller):
    # Obtener todos los eventos
    events = gui_controller.back_controller.get_all_events()

    # Verificar si hay eventos
    if not events:
        st.write("No hay eventos disponibles.")
        return

    # Inicializar DataFrames para almacenar los totales
    total_tickets_sold_by_type = pd.DataFrame({'presale': [0], 'regular': [0], 'complementary': [0]})
    total_income_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0]})

    # Sumar los datos de cada informe
    for event in events.values():
        report = event.report_data
        total_tickets_sold_by_type += report.tickets_sold_by_ticket_type
        total_income_by_ticket_type += report.total_income_by_ticket_type

    # Crear el primer gráfico: Cantidad de boletas vendidas por tipo
    total_tickets_sold_by_type = total_tickets_sold_by_type.melt(var_name='Ticket Type', value_name='Count')

    fig1 = px.bar(total_tickets_sold_by_type, x='Ticket Type', y='Count', title='Tickets Sold by Type')

    # Crear columnas para el gráfico y los ingresos totales
    graph_col, empty = st.columns([3, 1])

    with graph_col:
        #  Mostrar grafico de barras en Streamlit
        st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Total Income by Ticket Type")
    for ticket_type in total_income_by_ticket_type.columns:
        income = total_income_by_ticket_type.loc[0, ticket_type]
        st.write(f"{ticket_type.capitalize()}: {income} USD")


def draw_financial_reports_interface(gui_controller):
    """# Obtener todos los eventos
    events = gui_controller.back_controller.get_all_events()

    # Verificar si hay eventos
    if not events:
        st.write("No hay eventos disponibles.")
        return

    # Inicializar DataFrames para almacenar los totales
    total_income_by_payment_method = pd.DataFrame({"credit_card": [0], "debit_card": [0], "cash": [0]})
    total_income_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0]})

    # Sumar los datos de cada informe
    for event in events.values():
        report = event.report_data
        total_income_by_payment_method += report.total_income_by_payment_method
        total_income_by_ticket_type += report.total_income_by_ticket_type

    # Crear el primer gráfico: Ingresos por método de pago
    total_income_by_payment_method = total_income_by_payment_method.melt(var_name='Payment Method', value_name='Income')
    fig1 = px.pie(total_income_by_payment_method, names='Payment Method', values='Income', title='Income by Payment Method')
    st.plotly_chart(fig1, use_container_width=True)

    # Crear el segundo gráfico: Ingresos por tipo de boleto
    total_income_by_ticket_type = total_income_by_ticket_type.melt(var_name='Ticket Type', value_name='Income')
    fig2 = px.pie(total_income_by_ticket_type, names='Ticket Type', values='Income', title='Income by Ticket Type')
    st.plotly_chart(fig2, use_container_width=True)"""


def draw_demographic_reports_interface(gui_controller):
    """# Obtener todos los eventos
    events = gui_controller.back_controller.get_all_events()

    # Verificar si hay eventos
    if not events:
        st.write("No hay eventos disponibles.")
        return

    # Inicializar DataFrame para almacenar los datos demográficos
    total_buyers_demographic = pd.DataFrame(columns=['age', 'how_did_you_know', 'payment_method', 'emails'])

    # Sumar los datos de cada informe
    for event in events.values():
        report = event.report_data
        total_buyers_demographic = total_buyers_demographic.append(report.buyers_demographic, ignore_index=True)

    # Crear el primer gráfico: Distribución de edades
    fig1 = px.histogram(total_buyers_demographic, x='age', nbins=10, title='Age Distribution')
    st.plotly_chart(fig1, use_container_width=True)

    # Crear el segundo gráfico: Método de pago más utilizado
    fig2 = px.pie(total_buyers_demographic, names='payment_method', title='Payment Method Distribution')
    st.plotly_chart(fig2, use_container_width=True)

    # Botón para descargar el informe en formato Excel
    if st.button('Download Report in Excel Format'):
        total_buyers_demographic.to_excel('demographic_report.xlsx', index=False)
        st.success('Report has been downloaded successfully!')"""


def draw_artist_reports_interface(gui_controller):
    pass
