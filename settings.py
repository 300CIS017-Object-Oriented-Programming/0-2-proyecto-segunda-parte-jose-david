TITLE_MAIN_PAGE = """
<style>
.title_main_page {
    text-align: center;
    font-size: 60px;
    font-family: 'Courier New', Courier, monospace;
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
    "artists": {"type": "text", "label": "Artists"},
    "bar_profit": {"type": "number", "label": "Bar Profit"},
    "artist_payment": {"type": "number", "label": "Artist Payment"},
}

THEATER_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Name"},
    "date": {"type": "date", "label": "Date"},
    "opening_time": {"type": "time", "label": "Opening Time"},
    "show_time": {"type": "time", "label": "Show Time"},
    "location": {"type": "text", "label": "Location"},
    "address": {"type": "text", "label": "Address"},
    "city": {"type": "text", "label": "City"},
    "artists": {"type": "text", "label": "Artists"},
    "rental_cost": {"type": "number", "label": "Rental Cost"},
}

PHILANTHROPIC_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Name"},
    "date": {"type": "date", "label": "Date"},
    "opening_time": {"type": "time", "label": "Opening Time"},
    "show_time": {"type": "time", "label": "Show Time"},
    "location": {"type": "text", "label": "Location"},
    "address": {"type": "text", "label": "Address"},
    "city": {"type": "text", "label": "City"},
    "artists": {"type": "text", "label": "Artists"},
    "sponsors": {"type": "text", "label": "Sponsors"},
    "sponsorship_amount": {"type": "number", "label": "Sponsorship Amount"},
}