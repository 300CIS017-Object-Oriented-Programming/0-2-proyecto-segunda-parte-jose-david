from models.report import Report


class Event:
    """ Clase modelo para manejar de un evento para manejar su informacion en la aplicacion """

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, capacity):
        self.type = ''  # Se agrega despues con fines mas pracicos

        # Informacion basica del evento
        self.name = name
        self.date = date
        self.opening_time = opening_time
        self.show_time = show_time
        self.location = location
        self.address = address
        self.city = city
        self.artists = artists
        self.capacity = capacity
        self.state = 'to realize'

        self.tickets = [None, None]  # Boletas de configuradas de cada evento (presale,regular)
        self.sold_tickets = {}  # Boletas vendidas en cada evento
        self.report_data = Report()  # Instance de la clase reporte para manejar el analisis de datos de cada evento

        # Boleano para saber si ya se vendio al menos una boleta
        self.bool_sold_ticket = {"presale": False, "regular": False}

        # Boleano para saber si ya se agotaron todas las boletas
        self.bool_sold_out = {"presale": False, "regular": False}

