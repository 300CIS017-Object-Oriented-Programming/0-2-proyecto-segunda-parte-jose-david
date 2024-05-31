[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# GestionBoletasComedia

# Diagrama de clases UML 

```mermaid
   classDiagram
    class BackController {
        - Events
        - Artists
        + event_exists( date)
        + create_event( event_type, **event_data)
        + get_event_by_date(date)
        + choose_event_fields()
        + event_exists()
        + create_event
        + edit_event( event, field, new_value)
        + delete_event(event)
        + create_ticket(self, event, ticket_type, price, amount)
        + update_ticket()
        + bool_valid_pric()
        + generate_ticket_pdf()
        + create_sold_tickets()
        + generate_ticket_code()
        + register_access()
        + Gettes
        
    }
    class GUIController {
        - back_controller 
        - run_page
        main()
        create_event(, event_type, event_data)
        choose_event_fields(, event_type)
        edit_event()
        delete_event()
        valid_ticket_fields()
        edit_ticket_event_gui()
        ticket_sale()
        verify_access()
        
    }
    class Event {
        self.type 
        self.name 
        self.date 
        self.opening_time 
        self.show_time 
        self.location 
        self.address 
        self.city 
        self.artists 
        self.capacity 
        self.state 

        self.tickets  
        self.sold_tickets 
        self.report_data
        self.bool_sold_ticket 

       
        self.bool_sold_out 
    }
    class BarEvent {
        -bar_profit = bar_profit
        -artist_payment = artist_payment
    }
    class PhilanthropicEvent {
        - sponsors = sponsors
        - sponsorship_amount = sponsorship_amount
    }
    class TheaterEvent {
        - rental_cost = rental_cos
    }
    class Ticket {
        +start()
    }
    class EventView {
        + draw_create_event_interface(gui_controller, event_type, event_fields)
        + draw_input_field(field, config)
        + display_event(gui_controller, event, event_type)
    }
    class TicketView {
        
    }
    class ReportView {
        
    }
    class AccessView {
        
    }
    class MainView {
        + draw_option_menu(gui_controller)
        + draw_home_page()
        + draw_event_manager_page(gui_controller)
        + draw_ticket_office_page()
        + draw_access_management_page()
        + draw_reports_page()
    }
    class App {
        + main()
    }
    App ..> GUIController: lauches
    GUIController <..> MainView : uses
    GUIController --> BackController: has
    MainView ..> EventView: uses
    MainView ..> TicketView: uses
    MainView ..> ReportView: uses
    MainView ..> AccessView: uses
    BackController o-- Event: has
    Event <|-- BarEvent 
    Event <|-- PhilanthropicEvent 
    Event <|-- TheaterEvent 
```