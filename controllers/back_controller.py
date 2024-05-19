from models.bar_event import BarEvent
from models.philanthropic_event import PhilanthropicEvent
from models.theater_event import TheaterEvent


class BackController:
    """
    The BackController class is responsible for managing the business logic of the application.
    It interacts with the GUIController to handle user interface updates and manages the events in the application.
    """

    def __init__(self):
        """
        Initializes the BackController with an empty dictionary of events.
        """
        self.events = {}

    def event_exists(self, date):
        """
        Checks if an event exists on the specified date.
        Returns True if an event exists, False otherwise.
        """
        return date in self.events

    def create_event(self, event_type, **event_data):
        """
        Creates a new event of the specified type with the provided data.
        The event is stored in the events dictionary with the date as the key.
        """
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
        """
        Deletes the specified event from the event's dictionary.
        """
        del self.events[event.date]

    def get_event_by_date(self, date):
        """
        Retrieves an event by its date.
        Returns the event if it exists, None otherwise.
        """
        return self.events.get(date, None)

    def get_events_by_type(self, event_type):
        """
        Retrieves all events of a specified type.
        Returns a list of events if any exist, None otherwise.
        """
        events = [event for event in self.events.values() if event.type == event_type]
        return events if events else None
