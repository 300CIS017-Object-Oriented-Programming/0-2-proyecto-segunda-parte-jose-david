from models.bar_event import BarEvent
from models.philanthropic_event import PhilanthropicEvent
from models.theater_event import TheaterEvent


class BackController:
    def __init__(self):
        self.events = {}

    def event_exists(self, date):
        return date in self.events

    def create_event(self, event_type, **event_data):

        if event_type == "bar":
            self.events[event_data['date']] = BarEvent(**event_data)
            self.events[event_data['date']].type = 'Bar'
        elif event_type == "theater":
            self.events[event_data['date']] = TheaterEvent(**event_data)
            self.events[event_data['date']].type = 'Filantropico'
        elif event_type == "philanthropic":
            self.events[event_data['date']] = PhilanthropicEvent(**event_data)
            self.events[event_data['date']].type = 'Teatro'

    def get_event_by_date(self, date):
        return self.events.get(date, None)
