[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# GestionBoletasComedia
# Documenten aqui su proyecto

# Diagrama de clases UML 

```mermaid
   classDiagram
    class BackController {
        - Events
        + event_exists( date)
        + create_event( event_type, **event_data)
        + get_event_by_date(date)
    }
    class GUIController {
        - back_controller 
        - run_page
        main()
        create_event(, event_type, event_data)
        choose_event_fields(, event_type)
        
    }
    class Event {
        -type = ''
        -name = name
        -date = date
        -opening_time = opening_time
        -show_time = show_time
        -location = location
        -address = address
        -city = city
        -artists = artists
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