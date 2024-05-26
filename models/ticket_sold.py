class TicketSold:

    """Clase para alamcenar los datos de una boleta vendidda y facilitarnos su manejo """

    def __init__(self, code, ticket_type, buyer_name, buyer_id, buyer_age, buyer_email):
        self.code = code
        self.ticket_type = ticket_type
        self.buyer_id = buyer_id
        self.buyer_name = buyer_name
        self.buyer_email = buyer_email
