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