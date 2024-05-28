from models.bar_event import BarEvent
from models.philanthropic_event import PhilanthropicEvent
from models.theater_event import TheaterEvent
from models.ticket import Ticket
from models.ticket_sold import TicketSold
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightblue
from datetime import datetime
from settings import BAR_EVENT_FIELDS, PHILANTHROPIC_EVENT_FIELDS, THEATER_EVENT_FIELDS
from models.artist import Artist
import random
import string
from models.report import Report


class BackController:

    def __init__(self):
        self.events = {}
        self.artists = {}

    """ Event_manager_functions """

    def choose_event_fields(self, event_type):
        fields = None
        if event_type == "bar":
            fields = BAR_EVENT_FIELDS
        elif event_type == "philanthropic":
            fields = PHILANTHROPIC_EVENT_FIELDS
        elif event_type == "theater":
            fields = THEATER_EVENT_FIELDS

        return fields

    def event_exists(self, date):
        return date in self.events

    def create_event(self, event_type, **event_data):

        if event_type == "bar":
            self.events[event_data['date']] = BarEvent(**event_data)
            self.events[event_data['date']].type = 'bar'
        elif event_type == "theater":
            self.events[event_data['date']] = TheaterEvent(**event_data)
            self.events[event_data['date']].type = 'theater'
        elif event_type == "philanthropic":
            self.events[event_data['date']] = PhilanthropicEvent(**event_data)
            self.events[event_data['date']].type = 'philanthropic'

        artist_names = event_data['artists'].split(',')
        for artist_name in artist_names:
            artist_name = artist_name.strip()
            if artist_name in self.artists:
                self.artists[artist_name].events_participated[event_data['date']] = self.events[event_data['date']]
            else:
                new_artist = Artist(artist_name)
                new_artist.events_participated[event_data['date']] = self.events[event_data['date']]
                self.artists[artist_name] = new_artist

    def edit_event(self, event, field, new_value):
        if field == 'artists':
            for artist_name in list(self.artists.keys()):
                if event.date in self.artists[artist_name].events_participated:
                    del self.artists[artist_name]
            artist_names = new_value.split(',')
            for artist_name in artist_names:
                artist_name = artist_name.strip()
                new_artist = Artist(artist_name)
                new_artist.events_participated[event.date] = event
                self.artists[artist_name] = new_artist

        setattr(event, field, new_value)

    def delete_event(self, event):
        del self.events[event.date]

    def get_event_by_date(self, date):
        return self.events.get(date, None)

    def get_events_by_type(self, event_type):
        events = [event for event in self.events.values() if event.type == event_type]
        return events if events else None

    def get_all_event_dates(self):
        return list(self.events.keys())

    """ Ticket_office_functions """

    """ Management tickets functions """

    def get_event_ticket(self, ticket_type, event):
        ans_ticket = None
        if ticket_type == "presale":
            if event.tickets[0] is not None:
                ans_ticket = event.tickets[0]
        elif ticket_type == "regular":
            if event.tickets[1] is not None:
                ans_ticket = event.tickets[1]
        return ans_ticket

    def get_amount_ticket_assigned(self, ticket_type, event):
        ticket = self.get_event_ticket(ticket_type, event)
        if ticket is None:
            amount = 0
        else:
            amount = ticket.amount
        return amount

    def create_ticket(self, event, ticket_type, price, amount):

        if ticket_type == "presale":
            event.tickets[0] = Ticket(price, ticket_type)
            setattr(event.tickets[0], 'amount', amount)
            setattr(event.tickets[0], 'amount_available', amount)
        elif ticket_type == "regular":
            event.tickets[1] = Ticket(price, ticket_type)
            setattr(event.tickets[1], 'amount', amount)
            setattr(event.tickets[1], 'amount_available', amount)

    def update_state_event_to_sale(self, event):
        if event.tickets[0] is not None and event.tickets[1] is not None:
            event.state = "to sale tickets"

    def update_state_event_to_sold_out(self, event):
        if event.tickets[0].amount_available == 0 and event.tickets[1].amount_available == 0:
            event.state = "sold out"

    def update_ticket(self, ticket_to_edit, field_to_edit, new_value):

        setattr(ticket_to_edit, field_to_edit, new_value)

    def bool_valid_price(self, event, new_price):
        valid_price = True
        if event.type != 'philanthropic' and new_price == 0:
            valid_price = False

        return valid_price

    def bool_valid_amount(self, event, ticket_type, new_amount):

        valid_amount = True
        if ticket_type == "presale" and new_amount > event.tickets[0].amount:
            valid_amount = False
        elif ticket_type == "regular" and new_amount > event.tickets[1].amount:
            valid_amount = False

        return valid_amount

    """ Ticket_sales_functions """

    def generate_ticket_pdf(self, event, sold_tickets, filename):
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
        sold_tickets = []
        for _ in range(ticket_quantity):
            code = self.generate_ticket_code()
            sold_ticket = TicketSold(code, ticket_type, buyer_name, buyer_id, buyer_email, buyer_age)
            event.sold_tickets[sold_ticket.code] = sold_ticket
            sold_tickets.append(sold_ticket)

        return sold_tickets

    def generate_ticket_code(self):
        code = None
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        numbers = ''.join(random.choice(string.digits) for _ in range(3))
        code = letters + numbers
        return code

    def verify_sold_tickets(self, event, tickets_sold):
        verify = True
        for ticket in tickets_sold:
            if ticket.code not in event.sold_tickets:
                verify = False
        return verify

    def get_sold_ticket_by_code(self, event, code):
        return event.sold_tickets.get(code, None)

    def get_current_date(self):
        return datetime.now().date()

    def control_tickets_available(self, event, ticket_type, ticket_sale_quantity):
        if ticket_type == "presale" or ticket_type == "complementary":
            event.tickets[0].amount_available -= ticket_sale_quantity
        elif ticket_type == "regular" or ticket_type == "complementary":
            event.tickets[1].amount_available -= ticket_sale_quantity

    def register_access(self, event, ticket_code):
        if ticket_code in event.sold_tickets:
            del event.sold_tickets[ticket_code]

    # -------------------------------------------------------------------------------------------------
    def get_event_types_in_date_range(self, start_date, end_date):
        if not self.events:  # Si el diccionario de eventos está vacío
            return None

        event_types = [event.type for event in self.events.values() if start_date <= event.date <= end_date]
        return event_types

    def get_events_in_date_range(self, start_date, end_date):
        # Filtrar el diccionario de eventos para incluir solo aquellos eventos cuya fecha cae dentro del rango
        # especificado
        filtered_events = {date: event for date, event in self.events.items() if start_date <= date <= end_date}
        return filtered_events
    def get_all_events(self):
        # Devuelve una copia del diccionario de eventos para evitar la manipulación directa
        return self.events.copy()


    # --------------------------------------------------------------------------------------------------------------

    # Controlar las boletas vendidas por tipo de evento









