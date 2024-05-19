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
            self.events[event_data['date']].type = 'bar'
        elif event_type == "theater":
            self.events[event_data['date']] = TheaterEvent(**event_data)
            self.events[event_data['date']].type = 'theater'
        elif event_type == "philanthropic":
            self.events[event_data['date']] = PhilanthropicEvent(**event_data)
            self.events[event_data['date']].type = 'philanthropic'

    def delete_event(self, event):
        del self.events[event.date]

    def get_event_by_date(self, date):
        return self.events.get(date, None)

    def get_events_by_type(self, event_type):
        events = [event for event in self.events.values() if event.type == event_type]
        return events if events else None
