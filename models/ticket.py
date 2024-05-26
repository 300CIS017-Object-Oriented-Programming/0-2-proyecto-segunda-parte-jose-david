class Ticket:
    """
    La clase ticket se utiliza para generar el ticket definido que tiene un evento.
    nos ayuda para tener el cada evento definido cual va a ser la boleta de preventa y cual
    sera la boleta de venta regular.
    """
    def __init__(self, price, type_ticket):
        self.price = price
        self.type_ticket = type_ticket
        self.amount = 0
        self.amount_available = 0  # sirve para manejar la cantidad de boletas disponibles
        # self.reason_purchase = " "
