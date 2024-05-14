from models.event import Event


class TheaterEvent(Event):
    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, rental_cost):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists)
        self.rental_cost = rental_cost

