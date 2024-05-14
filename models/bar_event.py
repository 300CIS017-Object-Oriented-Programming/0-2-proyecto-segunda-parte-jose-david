from models.event import Event


class BarEvent(Event):

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, bar_profit,
                 artist_payment):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists)
        self.bar_profit = bar_profit
        self.artist_payment = artist_payment

