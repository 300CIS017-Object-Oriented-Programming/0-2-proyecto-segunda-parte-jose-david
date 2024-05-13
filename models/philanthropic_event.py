from models.event import Event


class PhilanthropicEvent(Event):
    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, tickets, sponsors,
                 sponsorship_amount):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists, tickets)
        self.sponsors = sponsors
        self.sponsorship_amount = sponsorship_amount
