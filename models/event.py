from models.ticket import Ticket


class Event:
    """
    The Event class serves as a blueprint for creating Event objects in the application.
    It encapsulates the common attributes and behaviors of an event, such as its name, date,
    opening time, show time, location, address, city, and artists.
    """

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists):
        self.type = ''
        self.name = name
        self.date = date
        self.opening_time = opening_time
        self.show_time = show_time
        self.location = location
        self.address = address
        self.city = city
        self.artists = artists
        self.tickets = [None, None]  # The tickets associated with the event (presale,regular)
