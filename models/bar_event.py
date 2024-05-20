from models.event import Event


class BarEvent(Event):
    """
       The BarEvent class inherits from the Event class and represents a specific type of event: a bar event.
        A bar event is an event that takes place in a bar and has a bar profit and an artist payment.
    """

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, capacity, bar_profit,
                 artist_payment):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists, capacity)
        self.bar_profit = bar_profit
        self.artist_payment = artist_payment
