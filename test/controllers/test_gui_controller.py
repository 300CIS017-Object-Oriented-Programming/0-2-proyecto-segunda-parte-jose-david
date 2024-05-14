import unittest
from unittest.mock import Mock, call
from controllers.gui_controller import GUIController


class TestGUIController(unittest.TestCase):
    # ... tus pruebas existentes ...

    def test_create_event_with_existing_date(self):
        # Crear un mock del BackController
        mock_back_controller = Mock()

        # Crear una instancia del GUIController con el mock del BackController
        gui_controller = GUIController()
        gui_controller.back_controller = mock_back_controller

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

        # Crear un evento
        gui_controller.create_event('philanthropic', event_data)

        # Intentar crear otro evento con la misma fecha
        gui_controller.create_event('philanthropic', event_data)

        # Verificar que el método event_exists del BackController se llamó dos veces con la misma fecha
        mock_back_controller.event_exists.assert_has_calls([call(event_data['date']), call(event_data['date'])])
        self.assertEqual(mock_back_controller.event_exists.call_count, 2)