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
    "name": {"type": "text", "label": "Nombre"},
    "date": {"type": "date", "label": "Fecha"},
    "opening_time": {"type": "time", "label": "Hora de apertura"},
    "show_time": {"type": "time", "label": "Hora del espectáculo"},
    "location": {"type": "text", "label": "Ubicación"},
    "address": {"type": "text", "label": "Dirección"},
    "city": {"type": "text", "label": "Ciudad"},
    "artists": {"type": "text", "label": "Artistas"},
    "bar_profit": {"type": "number", "label": "Ganancia del bar"},
    "artist_payment": {"type": "number", "label": "Pago al artista"},
}

THEATER_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Nombre"},
    "date": {"type": "date", "label": "Fecha"},
    "opening_time": {"type": "time", "label": "Hora de apertura"},
    "show_time": {"type": "time", "label": "Hora del espectáculo"},
    "location": {"type": "text", "label": "Ubicación"},
    "address": {"type": "text", "label": "Dirección"},
    "city": {"type": "text", "label": "Ciudad"},
    "artists": {"type": "text", "label": "Artistas"},
    "rental_cost": {"type": "number", "label": "Costo de alquiler"},
}

PHILANTHROPIC_EVENT_FIELDS = {
    "name": {"type": "text", "label": "Nombre"},
    "date": {"type": "date", "label": "Fecha"},
    "opening_time": {"type": "time", "label": "Hora de apertura"},
    "show_time": {"type": "time", "label": "Hora del espectáculo"},
    "location": {"type": "text", "label": "Ubicación"},
    "address": {"type": "text", "label": "Dirección"},
    "city": {"type": "text", "label": "Ciudad"},
    "artists": {"type": "text", "label": "Artistas"},
    "sponsors": {"type": "text", "label": "Patrocinadores"},
    "sponsorship_amount": {"type": "number", "label": "Monto del patrocinio"},
}
