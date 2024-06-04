import pandas as pd


class Report:
    def __init__(self):
        # Inicializa un DataFrame para cada tipo de informe con los tipos de boletos y métodos de pago como columnas.
        # Cada DataFrame comienza con valores iniciales de 0.
        self.tickets_sold_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0], 'complementary': [0]})
        self.total_income_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0]})
        self.total_income_by_payment_method = pd.DataFrame({"credit_card": [0], "debit_card": [0], "cash": [0]})
        self.income_by_event_type = pd.DataFrame({'bar': [0], 'philanthropic': [0], 'theater': [0]})

        # Inicializa un DataFrame para almacenar información demográfica de los compradores.
        self.buyers_demographic = pd.DataFrame(columns=['age', 'how_did_you_know', 'payment_method', 'emails'])

    def increment_sold_by_ticket_type(self, ticket_type, amount):
        # Incrementa la cantidad de boletos vendidos de un tipo específico.
        if ticket_type in self.tickets_sold_by_ticket_type.columns:
            self.tickets_sold_by_ticket_type.loc[0, ticket_type] += amount

    def increment_income_by_ticket_type(self, ticket_type, income):
        # Incrementa los ingresos totales de un tipo de boleto específico.
        if ticket_type in self.total_income_by_ticket_type.columns:
            self.total_income_by_ticket_type.loc[0, ticket_type] += income

    def increment_income_by_payment_method(self, payment_method, income):
        # Incrementa los ingresos totales de un método de pago específico.
        if payment_method in self.total_income_by_payment_method.columns:
            self.total_income_by_payment_method.loc[0, payment_method] += income

    def add_buyer_info(self, age, how_did_you_know, payment_method, email):
        # Agrega la información de un comprador al DataFrame de información demográfica.
        new_data = {'age': age, 'how_did_you_know': how_did_you_know, 'payment_method': payment_method, 'emails': email}
        new_index = len(self.buyers_demographic)
        self.buyers_demographic.loc[new_index] = new_data

    def increment_income_by_event_type(self, event_type, income):
        # Incrementa los ingresos totales de un tipo de evento específico.
        if event_type in self.income_by_event_type.columns:
            self.income_by_event_type.loc[0, event_type] += income