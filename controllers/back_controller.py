# models
from models.bar_event import BarEvent
from models.philanthropic_event import PhilanthropicEvent
from models.theater_event import TheaterEvent
from models.ticket import Ticket
from models.artist import Artist
from models.ticket_sold import TicketSold
from models.report import Report

# settings
from settings import BAR_EVENT_FIELDS, PHILANTHROPIC_EVENT_FIELDS, THEATER_EVENT_FIELDS

# Librerias
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightblue
from datetime import datetime
import random
import string


class BackController:

    """ Clase que controla la lógica de negocio de la aplicación. """

    def __init__(self):
        self.events = {}  # Diccionario para almacenar los eventos
        self.artists = {}  # Diccionario para almacenar los artistas participantes en los eventos

    """ Event_manager_functions """

    def choose_event_fields(self, event_type):
        """Devuelve los campos específicos para un tipo de evento dado."""

        fields = None
        if event_type == "bar":
            fields = BAR_EVENT_FIELDS  # settings.py
        elif event_type == "philanthropic":
            fields = PHILANTHROPIC_EVENT_FIELDS  # settings.py
        elif event_type == "theater":
            fields = THEATER_EVENT_FIELDS  # settings.py

        return fields

    def event_exists(self, date):
        """Verifica si un evento ya existe en el diccionario de eventos."""
        return date in self.events

    def create_event(self, event_type, **event_data):
        """ Crea un evento y configura todo lo que lo rodea."""

        if event_type == "bar":
            self.events[event_data['date']] = BarEvent(**event_data)
            self.events[event_data['date']].type = 'bar'
        elif event_type == "theater":
            self.events[event_data['date']] = TheaterEvent(**event_data)
            self.events[event_data['date']].type = 'theater'
        elif event_type == "philanthropic":
            self.events[event_data['date']] = PhilanthropicEvent(**event_data)
            self.events[event_data['date']].type = 'philanthropic'

        # Crear un artista si no existe y agregarlo al diccionario de artistas
        artist_names = event_data['artists'].split(',')
        for artist_name in artist_names:
            artist_name = artist_name.strip()
            if artist_name in self.artists:  # Si el artista ya existe
                self.artists[artist_name].events_participated[event_data['date']] = self.events[event_data['date']]
            else:
                new_artist = Artist(artist_name)  # Crear un nuevo artista

                new_artist.events_participated[event_data['date']] = self.events[event_data['date']]
                self.artists[artist_name] = new_artist  # Agregar el artista al diccionario de artistas

    def edit_event(self, event, field, new_value):
        """ Edita un campo específico de un evento dado."""

        if field == 'artists':
            # Eliminar los artisas de ese eventos para remplazarlos
            for artist_name in list(self.artists.keys()):  # Cada nombre del artista es una key
                if event.date in self.artists[artist_name].events_participated:
                    del self.artists[artist_name]
            # Agregar los nuevos artistas
            artist_names = new_value.split(',')  # Separar el string que se recibe para crear los artistas
            for artist_name in artist_names:
                artist_name = artist_name.strip()
                new_artist = Artist(artist_name)
                new_artist.events_participated[event.date] = event
                self.artists[artist_name] = new_artist

        # Actualizar el campo del evento
        setattr(event, field, new_value)

    def delete_event(self, event):
        """ Elimina un evento del diccionario de eventos. """
        del self.events[event.date]

    #  --------------------------------------------------------------------------------------------------------------

    """ Ticket_office_functions """
    """ Ticket manegement"""

    def create_ticket(self, event, ticket_type, price, amount):
        """ Crea un ticket y lo asigna a un evento. """
        if ticket_type == "presale":
            event.tickets[0] = Ticket(price, ticket_type)

            setattr(event.tickets[0], 'amount', amount)
            setattr(event.tickets[0], 'amount_available', amount)

        elif ticket_type == "regular":
            event.tickets[1] = Ticket(price, ticket_type)

            setattr(event.tickets[1], 'amount', amount)
            setattr(event.tickets[1], 'amount_available', amount)

    def update_state_event_to_sale(self, event):
        """ Actualiza el estado de un evento a 'to sale tickets' si los tickets del evento ya se crearon."""
        if event.tickets[0] is not None and event.tickets[1] is not None:
            event.state = "to sale tickets"

    def update_state_event_to_sold_out(self, event):
        """ Actualiza el estado de un evento a 'sold out' si los tickets del evento se agotaron."""
        if event.tickets[0].amount_available == 0 and event.tickets[1].amount_available == 0:
            event.state = "sold out"

    def update_ticket(self, ticket_to_edit, field_to_edit, new_value):
        """ Edita un campo específico de un ticket dado."""
        setattr(ticket_to_edit, field_to_edit, new_value)

    def bool_valid_price(self, event, new_price):
        """ Verifica si el precio de un ticket es válido."""
        valid_price = True
        if event.type != 'philanthropic' and new_price == 0:
            valid_price = False

        return valid_price

    def bool_valid_amount(self, event, ticket_type, new_amount):
        """ Verifica si la cantidad de tickets es válida."""
        valid_amount = True
        if ticket_type == "presale" and new_amount > event.tickets[0].amount:
            valid_amount = False

        elif ticket_type == "regular" and new_amount > event.tickets[1].amount:
            valid_amount = False

        return valid_amount

    """ Ticket_sales_functions """

    def generate_ticket_pdf(self, event, sold_tickets, filename):
        """ Genera un PDF con los tickets vendidos. """

        c = canvas.Canvas(filename, pagesize=letter)
        for i in range(len(sold_tickets)):
            # Dibujar un rectángulo como margen
            # Los parámetros son: x, y, ancho, alto
            c.setStrokeColor(lightblue)
            c.rect(50, 50, 500, 670)

            # Añadir texto al PDF
            c.setFont("Courier", 30)
            c.drawString(150, 750, "Humor Hub Tickets")

            c.setFont("Times-Roman", 8)
            c.drawString(120, 680, "Comprador: ")
            c.drawString(120, 660, "ID: ")
            c.drawString(120, 640, "Evento: ")
            c.drawString(120, 620, "Fecha: ")
            c.drawString(220, 620, "Artistas: ")
            c.drawString(120, 600, "Hora de apertura\nde puertas: ")
            c.drawString(120, 595, "de puertas: ")
            c.drawString(220, 600, "Hora del show: ")
            c.drawString(120, 560, "Ubicación: ")
            c.drawString(220, 560, "Ciudad: ")
            c.drawString(320, 560, "Dirección: ")
            c.drawString(420, 560, "codigo: ")

            c.setFont("Times-Bold", 8)
            c.drawString(180, 680, f"{sold_tickets[i].buyer_name}")
            c.drawString(180, 660, f"{sold_tickets[i].buyer_id}")
            c.drawString(180, 640, f" {event.name}")
            c.drawString(180, 620, f" {event.date}")
            c.drawString(280, 620, f" {event.opening_time}")
            c.drawString(180, 600, f" {event.show_time}")
            c.drawString(280, 600, f" {event.location}")
            c.drawString(180, 560, f" {event.city}")
            c.drawString(280, 560, f" {event.address}")
            c.drawString(380, 560, f" {event.artists}")
            c.drawString(480, 560, f" {sold_tickets[i].code}")

            c.setStrokeColor(lightblue)
            c.rect(50, 50, 500, 400)

            c.setFont("Helvetica", 16)
            c.drawString(80, 380, "IMPORTANTE")
            c.showPage()

        c.save()

    def create_sold_tickets(self, event, ticket_type, buyer_name, buyer_id, buyer_email, buyer_age, ticket_quantity):
        """ Crea tickets vendidos y los asigna a un evento. """
        sold_tickets = []
        for _ in range(ticket_quantity):
            code = self.generate_ticket_code()  # Generar un código de ticket
            sold_ticket = TicketSold(code, ticket_type, buyer_name, buyer_id, buyer_email, buyer_age)
            event.sold_tickets[sold_ticket.code] = sold_ticket
            sold_tickets.append(sold_ticket)

        return sold_tickets

    def generate_ticket_code(self):
        """ Genera un código de ticket. """
        code = None
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))  # Generar 3 letras aleatorias
        numbers = ''.join(random.choice(string.digits) for _ in range(3))  # Generar 3 números aleatorios
        code = letters + numbers
        return code

    def verify_sold_tickets(self, event, tickets_sold):
        """ Verifica si los tickets vendidos están en la lista de tickets vendidos del evento. """
        verify = True
        for ticket in tickets_sold:
            if ticket.code not in event.sold_tickets:
                verify = False
        return verify

    def control_tickets_available(self, event, ticket_type, ticket_sale_quantity):
        """ Controla la cantidad de tickets disponibles."""
        if ticket_type == "presale" or ticket_type == "complementary":
            event.tickets[0].amount_available -= ticket_sale_quantity

        elif ticket_type == "regular" or ticket_type == "complementary":
            event.tickets[1].amount_available -= ticket_sale_quantity

    # -------------------------------------------------------------------------------------------------

    """ Ticket_access_functions """

    def register_access(self, event, ticket_code):
        """ Registra el acceso de un ticket a un evento. """
        if ticket_code in event.sold_tickets:
            del event.sold_tickets[ticket_code]

    # -------------------------------------------------------------------------------------------------

    """ getters """
    """ get evetns """

    def get_all_events(self):
        # Devuelve una copia del diccionario de eventos para evitar la manipulación directa
        return self.events.copy()

    def get_event_by_date(self, date):
        """ Devuelve un evento por su fecha. """
        return self.events.get(date, None)

    def get_events_in_date_range(self, start_date, end_date):
        # Filtrar el diccionario de eventos para incluir solo aquellos eventos cuya fecha cae dentro del rango
        # especificado
        filtered_events = {date: event for date, event in self.events.items() if start_date <= date <= end_date}
        return filtered_events

    def get_event_types_in_date_range(self, start_date, end_date):
        """ Devuelve los tipos de eventos que se llevaron a cabo en un rango de fechas dado. """
        if not self.events:  # Si el diccionario de eventos está vacío
            return None

        event_types = [event.type for event in self.events.values() if start_date <= event.date <= end_date]
        return event_types

    def get_events_by_type(self, event_type):
        """ Devuelve una lista de eventos de un tipo específico. """
        events = [event for event in self.events.values() if event.type == event_type]
        return events if events else None

    """ get dates"""

    def get_all_event_dates(self):
        """ Devuelve una lista de todas las fechas de los eventos. """
        return list(self.events.keys())

    def get_current_date(self):
        """ Devuelve la fecha actual. """
        return datetime.now().date()

    """ others """

    def get_event_ticket(self, ticket_type, event):
        """ Devuelve un ticket de un evento dado. """

        ans_ticket = None
        if ticket_type == "presale":
            if event.tickets[0] is not None:
                ans_ticket = event.tickets[0]

        elif ticket_type == "regular":
            if event.tickets[1] is not None:
                ans_ticket = event.tickets[1]

        return ans_ticket

    def get_amount_ticket_assigned(self, ticket_type, event):
        """ Devuelve la cantidad de tickets asignados a un evento dado. """
        ticket = self.get_event_ticket(ticket_type, event)
        if ticket is None:
            amount = 0
        else:
            amount = ticket.amount
        return amount

    def get_sold_ticket_by_code(self, event, code):
        """ Devuelve un ticket vendido por su código. """
        return event.sold_tickets.get(code, None)
