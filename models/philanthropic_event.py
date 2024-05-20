from models.event import Event


class PhilanthropicEvent(Event):

    """
        The PhilanthropicEvent class extends the Event class, adding specific attributes related to philanthropic events.
        It is used to create PhilanthropicEvent objects in the application, which include additional information
        like sponsors and sponsorship amount.
    """

    def __init__(self, name, date, opening_time, show_time, location, address, city, artists, capacity, sponsors,
                 sponsorship_amount):
        super().__init__(name, date, opening_time, show_time, location, address, city, artists, capacity)
        self.sponsors = sponsors
        self.sponsorship_amount = sponsorship_amount


