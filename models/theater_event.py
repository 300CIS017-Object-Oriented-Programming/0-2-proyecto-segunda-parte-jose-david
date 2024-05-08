from models.event import Event


class Theater(Event):
    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, tickets, rental_cost):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists, tickets)
        self.rental_cost = rental_cost
