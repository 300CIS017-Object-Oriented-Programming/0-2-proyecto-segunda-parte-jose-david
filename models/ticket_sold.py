class TicketSold:

    """Clase para alamcenar los datos de una boleta vendidda y facilitarnos su manejo """

    def __init__(self, ticket_type, buyer_name, buyer_id):

        self.ticket_type = ticket_type
        self.buyer_id = buyer_id
        self.buyer_name = buyer_name
