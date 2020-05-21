class Phone:
    def __init__(self, make, model, _price):
        self.make = make
        self.model = model
        self._price = _price

    def make_call(self, number):
        print(f"Calling {number}")

    def full_name(self):
        return f"{self.make} {self.model} and price is {self._price}"
