[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# GestionBoletasComedia


## Descripción

Este proyecto es un sistema de gestión de eventos de comedia. El sistema permite la creación de eventos, la gestión 
de boletas y la generación de reportes.

Este proyecto fue desarrollado para el curso de Programación Orientada a Objetos de la Universidad Javeriana Cali
donde se buscaba aplicar los conceptos de POO en un proyecto de software real desarrollado con el framework stremlit.

## Tabla de Contenidos
- [Explicación](#explicación)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Código de Conducta](#código-de-conducta)
- [Licencia](#licencia)
- [Contacto](#contacto)
- [Agradecimientos](#agradecimientos)

## Explicación
### Humor hub
La solucion fue llamada Humor hub, un sistema de gestion de eventos de comedia. El sistema permite la creación de eventos, la gestión de boletas y la generación de reportes.

Los tipos de evento manejados son: BarEvent, PhilanthropicEvent y TheaterEvent. Cada uno de estos eventos tiene atributos y comportamientos específicos
sus campos se manejan en el archivo settings y se pueden modificar para adaptarse a las necesidades del usuario.

### Creación de eventos
El sistema permite la creación de eventos de comedia. Para crear un evento se debe ingresar la información requerida por el sistema.
El sistema valida que la información ingresada sea correcta y que no exista un evento con la misma fecha.
Tambien se pueden editar y eliminar eventos.

### Gestión de boletas
El sistema permite la creación de boletas para los eventos. Se pueden asignar precios a las boletas y se pueden vender boletas.
El sistema valida que la información ingresada sea correcta y que no se vendan boletas de más.
Tambien se pueden editar y eliminar boletas.

### Venta de boletas
El sistema permite la venta de boletas para los eventos. Se pueden vender boletas de diferentes tipos y se pueden vender varias boletas a la vez.
El sistema valida que la información ingresada sea correcta y que no se vendan boletas de más.
Tambien se pueden editar y eliminar boletas.

### Registro de acceso
El sistema permite el registro de acceso de los compradores a los eventos. Se puede registrar el acceso de un comprador a un evento.
El sistema valida que la información ingresada sea correcta y que no se registre el acceso de un comprador más de una vez.

### Reportes
El sistema permite la generación de reportes de los eventos. Se pueden generar reportes de los eventos vendidos, los ingresos por tipo de boleta, los ingresos por tipo de evento, los ingresos por método de pago y la demografía de los compradores.

### Diagrama de clases

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
## Instalación
* Instalar el proyecto en su computador local. Escriba desde la línea de comandos y ubicado en la carpeta raíz del
  proyecto `pip install -r requirements.txt`. Note que si no tiene un ambiente virtual primero debe configurarlo.
* Ejecutar el juego localmente. Escriba en consola `streamlit run app.py`. Su navegador debería abrir el juego

## Uso

En cuanto al uso puedes consultar este manuel de usuario [Manual de usuario](docs/Manual%20de%20usuario.pdf)


## Contacto

Si tienes alguna pregunta o comentario sobre este proyecto, no dudes en contactarme:

- **GitHub**: [Jdavidrb](https://github.com/Jdavidrb)
- **Correo Personal**: u.jdavidrb@gmail.com
- **Correo Institucional**: jdavidruanob@javerianacali.edu.co
- **Número de Contacto**: 3126498666


