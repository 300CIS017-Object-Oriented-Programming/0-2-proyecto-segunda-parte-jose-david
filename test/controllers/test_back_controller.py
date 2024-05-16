import unittest
from controllers.back_controller import BackController
from models.bar_event import BarEvent
from models.theater_event import TheaterEvent
from models.philanthropic_event import PhilanthropicEvent


class TestBackController(unittest.TestCase):
    def setUp(self):
        self.controller = BackController()

    def test_create_bar_event(self):
        event_data = {
            'name': 'Test Bar Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            'address': '123 Test Street',
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'bar_profit': 1000,
            'artist_payment': 500
        }
        self.controller.create_event('bar', **event_data)
        self.assertIsInstance(self.controller.events[event_data['date']], BarEvent)

    def test_create_theater_event(self):
        event_data = {
            'name': 'Test Theater Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            'address': '123 Test Street',
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'rental_cost': 2000
        }
        self.controller.create_event('theater', **event_data)
        self.assertIsInstance(self.controller.events[event_data['date']], TheaterEvent)

    def test_create_philanthropic_event(self):
        event_data = {
            'name': 'Test Philanthropic Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            'address': '123 Test Street',
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'sponsors': ['Sponsor 1', 'Sponsor 2'],
            'sponsorship_amount': 3000
        }
        self.controller.create_event('philanthropic', **event_data)
        self.assertIsInstance(self.controller.events[event_data['date']], PhilanthropicEvent)

    def test_event_exists(self):
        event_data = {
            'name': 'Test Philanthropic Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            'address': '123 Test Street',
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'sponsors': ['Sponsor 1', 'Sponsor 2'],
            'sponsorship_amount': 3000
        }
        self.controller.create_event('philanthropic', **event_data)
        self.assertTrue(self.controller.event_exists(event_data['date']))

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


if __name__ == '__main__':
    unittest.main()

"""    def test_create_event_with_existing_date(self):
        event_data = {
            'name': 'Test Event',
            'date': '2022-12-31',
            'opening_time': '18:00',
            'show_time': '20:00',
            'location': 'Test Location',
            'address': '123 Test Street',
            'city': 'Test City',
            'artists': ['Artist 1', 'Artist 2'],
            'sponsors': ['Sponsor 1', 'Sponsor 2'],
            'sponsorship_amount': 3000
        }
        self.controller.create_event('philanthropic', **event_data)
        with self.assertRaises(KeyError):
            self.controller.create_event('philanthropic', **event_data)"""

"""def test_create_event_with_unknown_type(self):
    event_data = {
        'name': 'Test Event',
        'date': '2022-12-31',
        'opening_time': '18:00',
        'show_time': '20:00',
        'location': 'Test Location',
        'address': '123 Test Street',
        'city': 'Test City',
        'artists': ['Artist 1', 'Artist 2'],
        'sponsors': ['Sponsor 1', 'Sponsor 2'],
        'sponsorship_amount': 3000
    }
    with self.assertRaises(KeyError):
        self.controller.create_event('unknown', **event_data)"""
