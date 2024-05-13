from models.bar_event import BarEvent
from models.philanthropic_event import PhilanthropicEvent
from models.theater_event import TheaterEvent


class BackController:
    def __init__(self):
        self.events = {}

    def event_exists(self, date):
        return date in self.events

    def create_bar_event(self, **event_data):
        if self.event_exists(event_data['date']):
            return False
        self.events[event_data['date']] = BarEvent(**event_data)
        return True

    def create_theater_event(self, **event_data):
        if self.event_exists(event_data['date']):
            return False
        self.events[event_data['date']] = TheaterEvent(**event_data)
        return True

    def create_philanthropic_event(self, **event_data):
        if self.event_exists(event_data['date']):
            return False
        self.events[event_data['date']] = PhilanthropicEvent(**event_data)
        return True

    def get_event_by_date(self, date):
        return self.events.get(date, None)