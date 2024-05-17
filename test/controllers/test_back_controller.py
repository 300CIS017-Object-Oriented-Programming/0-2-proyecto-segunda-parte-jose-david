import unittest
from controllers.back_controller import BackController
from models.bar_event import BarEvent
from models.theater_event import TheaterEvent
from models.philanthropic_event import PhilanthropicEvent
from settings import bar_event_data, theater_event_data, philanthropic_event_data


class TestBackController(unittest.TestCase):
    def setUp(self):
        self.controller = BackController()

    def test_create_bar_event(self):
        self.controller.create_event('bar', **bar_event_data)
        self.assertIsInstance(self.controller.events[bar_event_data['date']], BarEvent)

    def test_create_theater_event(self):
        self.controller.create_event('theater', **theater_event_data)
        self.assertIsInstance(self.controller.events[theater_event_data['date']], TheaterEvent)

    def test_create_philanthropic_event(self):
        self.controller.create_event('philanthropic', **philanthropic_event_data)
        self.assertIsInstance(self.controller.events[philanthropic_event_data['date']], PhilanthropicEvent)

    def test_event_exists(self):
        self.controller.create_event('philanthropic', **philanthropic_event_data)
        self.assertTrue(self.controller.event_exists(philanthropic_event_data['date']))

    def test_event_does_not_exist(self):
        self.assertFalse(self.controller.event_exists('2022-12-31'))

    def test_create_event_with_missing_data(self):
        event_data = {
            'name': 'Test Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            # 'address' falta intencionalmente
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'sponsors': ['Sponsor 1', 'Sponsor 2'],
            'sponsorship_amount': 3000
        }
        with self.assertRaises(TypeError):
            self.controller.create_event('philanthropic', **event_data)

    """def test_get_events_by_type(self):
        events = self.controller.events
        print(f"Events: {events} {type(events)} {len(events)}")

        # Verificar que todos los eventos devueltos son de tipo 'bar'

        bar_events = self.controller.get_events_by_type('bar')
        for event in bar_events:
            self.assertIsInstance(event, BarEvent)

        # Repetir para los otros tipos de eventos
         theater_events = self.controller.get_events_by_type('theater')
        for event in theater_events:
            self.assertIsInstance(event, TheaterEvent)

        philanthropic_events = self.controller.get_events_by_type('philanthropic')
        for event in philanthropic_events:
            self.assertIsInstance(event, PhilanthropicEvent)""" # FIX ME


if __name__ == '__main__':
    unittest.main()

