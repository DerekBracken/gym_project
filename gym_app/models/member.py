class Member:

    def __init__(self, first_name, last_name, premium=False, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.premium = premium
        self.id = id

    def full_name(self):
        self.full_name = self.full_name + " " + self.last_name