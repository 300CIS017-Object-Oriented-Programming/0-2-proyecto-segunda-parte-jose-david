import streamlit as st


def draw_create_bar_event():

    st.title('Create a Bar Event')
    name = st.text_input('Name')
    date = st.date_input('Date')
    opening_time = st.time_input('Opening Time')
    show_time = st.time_input('Show Time')
    location = st.text_input('Location')
    address = st.text_input('Address')
    city = st.text_input('City')
    artists = st.text_input('Artists')
    tickets = st.number_input('Tickets')
    bar_profit = st.number_input('Bar Profit')
    artist_payment = st.number_input('Artist Payment')
    if st.button('Create'):
        st.write(f'Event {name} created')
        st.write(f'Date: {date}')
        st.write(f'Opening Time: {opening_time}')
        st.write(f'Show Time: {show_time}')
        st.write(f'Location: {location}')
        st.write(f'Address: {address}')
        st.write(f'City: {city}')
        st.write(f'Artists: {artists}')
        st.write(f'Tickets: {tickets}')
        st.write(f'Bar Profit: {bar_profit}')
        st.write(f'Artist Payment: {artist_payment}')


def draw_create_theater_event():

    st.title('Create a Theater Event')
    """name = st.text_input('Name')
    date = st.date_input('Date')
    opening_time = st.time_input('Opening Time')
    show_time = st.time_input('Show Time')
    location = st.text_input('Location')
    address = st.text_input('Address')
    city = st.text_input('City')
    artists = st.text_input('Artists')
    tickets = st.number_input('Tickets')
    rental_cost = st.number_input('Rental Cost')
    if st.button('Create'):
        st.write(f'Event {name} created')
        st.write(f'Date: {date}')
        st.write(f'Opening Time: {opening_time}')
        st.write(f'Show Time: {show_time}')
        st.write(f'Location: {location}')
        st.write(f'Address: {address}')
        st.write(f'City: {city}')
        st.write(f'Artists: {artists}')
        st.write(f'Tickets: {tickets}')
        st.write(f'Rental Cost: {rental_cost}')"""


def draw_create_philanthropic_event():
    st.empty()
    st.title('Create a Philantropic Event')
    """name = st.text_input('Name')
    date = st.date_input('Date')
    opening_time = st.time_input('Opening Time')
    show_time = st.time_input('Show Time')
    location = st.text_input('Location')
    address = st.text_input('Address')
    city = st.text_input('City')
    artists = st.text_input('Artists')
    tickets = st.number_input('Tickets')
    donation_target = st.number_input('Donation Target')
    if st.button('Create'):
        st.write(f'Event {name} created')
        st.write(f'Date: {date}')
        st.write(f'Opening Time: {opening_time}')
        st.write(f'Show Time: {show_time}')
        st.write(f'Location: {location}')
        st.write(f'Address: {address}')
        st.write(f'City: {city}')
        st.write(f'Artists: {artists}')
        st.write(f'Tickets: {tickets}')
        st.write(f'Donation Target: {donation_target}')"""
