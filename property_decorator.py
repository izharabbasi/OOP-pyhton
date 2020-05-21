class Phone:
    def __init__(self, make, model, _price):
        self.make = make
        self.model = model
        self._price = max(_price, 0)
        # self.complete_specs = f"{self.make} {self.model} and price is {self._price}"

    @property
    def complete_specs(self):
        return f"{self.make} {self.model} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def calling(self, Phone_number):
        print(f"Calling {Phone_number}")

    def full_name(self):
        return f"{self.make} and  {self.model}"


phone1 = Phone("Iphone", "7Plus", -6500)
phone1._price = -1000
print(phone1.model)
print(phone1._price)
print(phone1.complete_specs)
