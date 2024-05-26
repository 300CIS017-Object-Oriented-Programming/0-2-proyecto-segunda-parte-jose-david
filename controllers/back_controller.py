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


class BackController:
    """
    The BackController class is responsible for managing the business logic of the application.
    It interacts with the GUIController to handle user interface updates and manages the events in the application.
    """

    def __init__(self):
        """
        Initializes the BackController with an empty dictionary of events.
        """
        self.events = {}
        self.artists = {}

    """ Event_manager_functions """

    def choose_event_fields(self, event_type):
        """
        Returns the appropriate fields for the specified event type.
        """
        fields = None
        if event_type == "bar":
            fields = BAR_EVENT_FIELDS
        elif event_type == "philanthropic":
            fields = PHILANTHROPIC_EVENT_FIELDS
        elif event_type == "theater":
            fields = THEATER_EVENT_FIELDS

        return fields

    def event_exists(self, date):
        """
        Checks if an event exists on the specified date.
        Returns True if an event exists, False otherwise.
        """
        return date in self.events

    def create_event(self, event_type, **event_data):
        """
        Creates a new event of the specified type with the provided data.
        The event is stored in the events dictionary with the date as the key.
        """
        if event_type == "bar":
            self.events[event_data['date']] = BarEvent(**event_data)
            self.events[event_data['date']].type = 'bar'
        elif event_type == "theater":
            self.events[event_data['date']] = TheaterEvent(**event_data)
            self.events[event_data['date']].type = 'theater'
        elif event_type == "philanthropic":
            self.events[event_data['date']] = PhilanthropicEvent(**event_data)
            self.events[event_data['date']].type = 'philanthropic'

        # Split the 'artists' string into a list of artist names
        artist_names = event_data['artists'].split(',')

        # For each artist name, if it exists in the artists dictionary, add the event to its list of events.
        # If it does not exist, create a new Artist and add the event to its list of events.
        for artist_name in artist_names:
            artist_name = artist_name.strip()  # Remove leading and trailing whitespace
            if artist_name in self.artists:
                self.artists[artist_name].events_participated[event_data['date']] = self.events[event_data['date']]
            else:
                new_artist = Artist(artist_name)
                new_artist.events_participated[event_data['date']] = self.events[event_data['date']]
                self.artists[artist_name] = new_artist

    def edit_event(self, event, field, new_value):
        """
        Edits the specified field of an existing event with a new value.
        """
        if field == 'artists':
            # Remove current artists from the event

            for artist_name in list(self.artists.keys()):
                if event.date in self.artists[artist_name].events_participated:
                    del self.artists[artist_name]

            # Split the 'artists' string into a list of artist names
            artist_names = new_value.split(',')

            # For each artist name, create a new Artist and add the event to its list of events

            for artist_name in artist_names:
                artist_name = artist_name.strip()  # Remove leading and trailing whitespace
                new_artist = Artist(artist_name)
                new_artist.events_participated[event.date] = event
                self.artists[artist_name] = new_artist

        setattr(event, field, new_value)

    def delete_event(self, event):
        """
        Deletes the specified event from the event's dictionary.
        """
        del self.events[event.date]

    def get_event_by_date(self, date):
        """
        Retrieves an event by its date.
        Returns the event if it exists, None otherwise.
        """
        return self.events.get(date, None)

    def get_events_by_type(self, event_type):
        """
        Retrieves all events of a specified type.
        Returns a list of events if any exist, None otherwise.
        """
        events = [event for event in self.events.values() if event.type == event_type]
        return events if events else None

    def get_all_event_dates(self):
        """
        Retrieves all dates of the existing events.
        Returns a list of dates.
        """
        return list(self.events.keys())

    """ Ticket_office_functions """

    """ Management tickets functions """

    def get_event_ticket(self, ticket_type, event):
        """
        Assigns a ticket type to an event.
        It communicates with the BackController to assign the ticket type to the event and displays a success message.
        """
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
        """
        Creates a new ticket for the specified event with the given price and amount.
        """
        if ticket_type == "presale":
            event.tickets[0] = Ticket(price, ticket_type)
            setattr(event.tickets[0], 'amount', amount)
            setattr(event.tickets[0], 'amount_available', amount)
        elif ticket_type == "regular":
            event.tickets[1] = Ticket(price, ticket_type)
            setattr(event.tickets[1], 'amount', amount)
            setattr(event.tickets[1], 'amount_available', amount)

    def update_ticket(self, ticket_to_edit, field_to_edit, new_value):
        """
        Updates the specified field of the ticket with the new value.
        """
        setattr(ticket_to_edit, field_to_edit, new_value)

    def bool_valid_price(self, event, new_price):
        """
        Updates the price of the specified ticket type for the given event with validation.
        """
        valid_price = True
        if event.type != 'philanthropic' and new_price == 0:
            valid_price = False

        return valid_price

    def bool_valid_amount(self, event, ticket_type, new_amount):
        """
        Updates the amount of the specified ticket type for the given event with validation.
        """
        # Cambiar.
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

            # Agregar la imagen
            # c.drawImage("ruta/a/la/imagen.jpg", x, y, ancho, alto)

            # Dibujar un segundo rectángulo como margen
            c.setStrokeColor(lightblue)
            c.rect(50, 50, 500, 400)

            c.setFont("Helvetica", 16)
            c.drawString(80, 380, "IMPORTANTE")
            c.showPage()
            # Aquí puedes agregar el texto importante

            # Finalizar y guardar el PDF
        c.save()

    def create_sold_tickets(self, event, ticket_type, buyer_name, buyer_id, buyer_email, buyer_age, ticket_quantity):
        """
        Creates a new sold ticket for the specified event and ticket type.
        """
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
        """
        Verifies if a ticket has been sold to the buyer with the specified ID.
        """
        verify = True
        for ticket in tickets_sold:
            if ticket.code not in event.sold_tickets:
                verify = False
        return verify

    def get_sold_ticket_by_code(self, event, code):
        """
        Retrieves a sold ticket by the buyer's ID.
        """
        return event.sold_tickets.get(code, None)

    def get_current_date(self):
        """
        Returns the current date in the format 'YYYY-MM-DD'.
        """
        return datetime.now().date()

    def control_tickets_available(self, event, ticket_type, ticket_sale_quantity):
        if ticket_type == "presale":
            event.tickets[0].amount_available -= ticket_sale_quantity
        elif ticket_type == "regular":
            event.tickets[1].amount_available -= ticket_sale_quantity

    def register_access(self, event, ticket_code):
        if ticket_code in event.sold_tickets:
            del event.sold_tickets[ticket_code]

