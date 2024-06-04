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
        + create_event()
        + edit_event( event, field, new_value)
        + delete_event(event)
        + create_ticket(self, event, ticket_type, price, amount)
        + update_ticket()
        + bool_valid_pric()
        + generate_ticket_pdf()
        + create_sold_tickets()
        + generate_ticket_code()
        + register_access()
        + Getters()
        
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
        - type 
        - name 
        - date 
        - opening_time 
        - show_time 
        - location 
        - address 
        - city 
        - artists 
        - capacity 
        - state
        - tickets  
        - sold_tickets 
        - report_data
        - bool_sold_ticket
        - bool_sold_out 
    }
    class BarEvent {
        - bar_profit = bar_profit
        - artist_payment 
        
    }
    class PhilanthropicEvent {
        - sponsors = sponsors
        - sponsorship_amount 
    }
    class TheaterEvent {
        - rental_cost 
    }
    class Ticket {
        - price 
        - type_ticket 
        - amount 
        - amount_available  
    }
    class SoldTicket {
        - code 
        - ticket_type 
        - buyer_id 
        - buyer_name 
        - buyer_email 
    }
    class Report {
        - tickets_sold_by_ticket_type 
        - total_income_by_ticket_type 
        - total_income_by_payment_method 
        - buyers_demographic 
        - income_by_event_type 

        + increment_sold_by_ticket_type(self, ticket_type, amount)
        + increment_income_by_ticket_type(self, ticket_type, income):
        + increment_income_by_payment_method(self, payment_method, income)
        + add_buyer_info(self, age, how_did_you_know, payment_method, email)
        + increment_income_by_event_type(self, event_type, income)
    }
    class Artist {
        - name
        - events_participated
    }
    class EventView {
        + draw_create_event_interface(gui_controller)
        + draw_input_field(field, config)
        + display_event(gui_controller)
    }
    class TicketView {
        + draw_ticket_management_interface(gui_controller)
        + draw_assign_ticket_price_interface(gui_controller)
        + draw_edit_ticket_interface(gui_controller)
        + draw_ticket_sales_management_interface(gui_controller)
        + draw_sale_ticket_interface(gui_controller)
        + draw_sale_ticket_form(gui_controller)
    }
    
    class AccessView {
        + draw_register_access_interface(gui_controller)
    }
    class MainView {
        + draw_option_menu(gui_controller)
        + draw_home_page(gui_controller)
        + draw_event_manager_page(gui_controller)
        + draw_ticket_office_page(gui_controller)
        + draw_access_management_page(gui_controller)
    }
    class App {
        + main()
    }
    App ..> GUIController: lauches
    GUIController <..> MainView : uses
    GUIController --> BackController: has
    MainView ..> EventView: uses
    MainView ..> TicketView: uses
    MainView ..> AccessView: uses
    BackController o-- Event: has
    BackController o-- Artist: has
    Event <|-- BarEvent 
    Event <|-- PhilanthropicEvent 
    Event <|-- TheaterEvent 
    Event o-- Ticket: has
    Event o-- SoldTicket: has
    Event --> Report: has
    
    
```