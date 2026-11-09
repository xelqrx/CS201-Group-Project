import random


class Client:
    def __init__(self, name, balance, is_riding=False, id_created=False):
        self.name = name
        self.balance = balance
        self.is_riding = is_riding
        self.id_created = id_created
        self.client_ID = None
        self.bike_id = None
        self.client_ID = self.create_id()

    def create_id(self):
        if self.id_created:
            return self.client_ID
        self.client_ID = random.randint(1000, 9999)
        self.id_created = True
        return self.client_ID

    def check_balance(self) -> bool:
        return self.balance >= 2

    def assign_bike(self, bike_id):
        self.bike_id = bike_id
        self.is_riding = True
        return self.client_ID

    def balance_change(self, change):
        self.balance -= change
        return self.balance
