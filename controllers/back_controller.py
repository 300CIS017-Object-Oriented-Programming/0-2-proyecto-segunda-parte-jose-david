from models.bar_event import BarEvent


class BackController:
    def __init__(self):
        self.events = {}

    def create_bar_event(self, name, date, opening_time, show_time, location, address, city, artists, tickets,
                         bar_profit, artist_payment):
        self.events[date] = BarEvent(name, date, opening_time, show_time, location, address, city, artists, tickets,
                                     bar_profit, artist_payment)
