import streamlit as st

TITLE_MAIN_PAGE = """
<style>
.title_main_page {
    text-align: center;
    font-size: 80px;
    font-family: 'Courier New', Courier, monospace;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
    background: -webkit-linear-gradient(left, #ffd803, #ff5733);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>

<script>
function set_title_color() {
    var bgColor = getComputedStyle(document.body).backgroundColor;
    var title = document.querySelector('.title');
    if (bgColor === 'rgb(255, 255, 255)') {  // Si el fondo es blanco (tema claro)
        title.style.color = 'black';
    } else {  // Si el fondo no es blanco (tema oscuro)
        title.style.color = 'white';
    }
}
document.addEventListener('DOMContentLoaded', set_title_color);
</script>
"""

TITLE_MAIN_FUNCTIONS = """
<style>
.title_main_functions {
    text-align: center;
    font-size: 40px;  # Cambia el tamaño de la fuente aquí
    font-family: 'Arial', sans-serif;  # Cambia la fuente aquí
    text-shadow: 2px 2px black;
    
}
</style>

<script>
function set_title_color() {
    var bgColor = getComputedStyle(document.body).backgroundColor;
    var title = document.querySelector('.title');
    if (bgColor === 'rgb(255, 255, 255)') {  // Si el fondo es blanco (tema claro)
        title.style.color = 'black';
    } else {  // Si el fondo no es blanco (tema oscuro)
        title.style.color = 'white';
    }
}
document.addEventListener('DOMContentLoaded', set_title_color);
</script>
"""

BAR_EVENT_FIELDS = {

    "name": {"type": "text", "label": "Name"},
    "date": {"type": "date", "label": "Date"},
    "opening_time": {"type": "time", "label": "Opening Time"},
    "show_time": {"type": "time", "label": "Show Time"},
    "location": {"type": "text", "label": "Location"},
    "address": {"type": "text", "label": "Address"},
    "city": {"type": "text", "label": "City"},
    "artists": {"type": "text", "label": "Artists(put a comma between artists)"},
    "capacity": {"type": "number", "label": "Capacity"},
    "state": {"type": "select", "label": "State", "options": ["Cancelled", "Postponed", "Closed"]},

}

THEATER_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Name"},
    "date": {"type": "date", "label": "Date"},
    "opening_time": {"type": "time", "label": "Opening Time"},
    "show_time": {"type": "time", "label": "Show Time"},
    "location": {"type": "text", "label": "Location"},
    "address": {"type": "text", "label": "Address"},
    "city": {"type": "text", "label": "City"},
    "artists": {"type": "text", "label": "Artists(put a comma between artists)"},
    "capacity": {"type": "number", "label": "Capacity"},
    "rental_cost": {"type": "number", "label": "Rental Cost"},
    "state": {"type": "select", "label": "State", "options": ["Cancelled", "Postponed", "Closed"]},
}

PHILANTHROPIC_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Name of event"},
    "date": {"type": "date", "label": "Date"},
    "opening_time": {"type": "time", "label": "Opening Time"},
    "show_time": {"type": "time", "label": "Show Time"},
    "location": {"type": "text", "label": "Location"},
    "address": {"type": "text", "label": "Address"},
    "city": {"type": "text", "label": "City"},
    "artists": {"type": "text", "label": "Artists(put a comma between artists)"},
    "capacity": {"type": "number", "label": "Capacity"},
    "sponsors": {"type": "text", "label": "Sponsors"},
    "sponsorship_amount": {"type": "number", "label": "Sponsorship Amount"},
    "state": {"type": "select", "label": "State", "options": ["Cancelled", "Postponed", "Closed"]},
}

TICKET_EVENT_FIELDS = {
    "price": {"type": "number", "label": "Price"},
    "amount": {"type": "number", "label": "Amount"},
}

OPTIONS_MARKETING = ["Social Media", "Friends/Family", "Advertisement", "Other"]
OPTIONS_METHOD = ["credit_card", "debit_card", "cash"]

bar_event_data = {
    'name': 'Test Bar Event',
    'date': '2022-12-31',
    'opening_time': '18:00',
    'show_time': '20:00',
    'location': 'Test Location',
    'address': '123 Test Street',
    'city': 'Test City',
    'artists': 'Artist 1',
    'capacity': 100,
    'bar_profit': 1000,
    'artist_payment': 500

}


theater_event_data = {
    'name': 'Test Theater Event',
    'date': '2022-12-31',
    'opening_time': '18:00',
    'show_time': '20:00',
    'location': 'Test Location',
    'address': '123 Test Street',
    'city': 'Test City',
    'artists': 'Artist 1',
    'capacity': 100,
    'rental_cost': 2000
}

philanthropic_event_data = {
    'name': 'Test Philanthropic Event',
    'date': '2022-12-31',
    'opening_time': '18:00',
    'show_time': '20:00',
    'location': 'Test Location',
    'address': '123 Test Street',
    'city': 'Test City',
    'artists': 'Artist 1',
    'capacity': 100,
    'sponsors': 'Sponsor 1',
    'sponsorship_amount': 3000
}
