import pandas as pd


class Report:
    def __init__(self):
        # boletos vendidos por tipo de evento
        self.tickets_sold_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0], 'complementary': [0]})
        # Ingresos totales por tipo de boleta
        self.total_income_by_ticket_type = pd.DataFrame({'presale': [0], 'regular': [0]})
        # Ingresos totales por metodo de pago
        self.total_income_by_payment_method = pd.DataFrame({"credit_card": [0], "debit_card": [0], "cash": [0]})
        # Informacion demografica de los compradores
        self.buyers_demographic = pd.DataFrame(columns=['age', 'how_did_you_know', 'payment_method', 'emails'])
        # Dinero por tipo de evento
        self.income_by_event_type = pd.DataFrame({'bar': [0], 'philanthropic': [0], 'theater': [0]})

    def increment_sold_by_ticket_type(self, ticket_type, amount):
        if ticket_type in self.tickets_sold_by_ticket_type.columns:
            self.tickets_sold_by_ticket_type.loc[0, ticket_type] += amount

    def increment_income_by_ticket_type(self, ticket_type, income):
        if ticket_type in self.total_income_by_ticket_type.columns:
            self.total_income_by_ticket_type.loc[0, ticket_type] += income

    def increment_income_by_payment_method(self, payment_method, income):
        if payment_method in self.total_income_by_payment_method.columns:
            self.total_income_by_payment_method.loc[0, payment_method] += income

    def add_buyer_info(self, age, how_did_you_know, payment_method, email):
        new_data = {'age': age, 'how_did_you_know': how_did_you_know, 'payment_method': payment_method, 'emails': email}
        new_index = len(self.buyers_demographic)
        self.buyers_demographic.loc[new_index] = new_data

    def increment_income_by_event_type(self, event_type, income):
        if event_type in self.income_by_event_type.columns:
            self.income_by_event_type.loc[0, event_type] += income
