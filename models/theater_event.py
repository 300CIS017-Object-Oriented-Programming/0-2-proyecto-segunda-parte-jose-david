from models.event import Event


class TheaterEvent(Event):

    """
        The TheaterEvent class extends the Event class, adding specific attributes related to theater events.
        It is used to create TheaterEvent objects in the application, which include additional information
        like rental cost of the theater.
    """

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, rental_cost):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists)
        self.rental_cost = rental_cost

