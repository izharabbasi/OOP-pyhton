class Phone:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self.complete_specs = f"{self.make} {self.model} and price is {self.price}"

    def calling(self, Phone_number):
        print(f"Calling {Phone_number}")

    def full_name(self):
        return f"{self.make} and  {self.model}"


phone1 = Phone("Iphone", "7Plus", 6500)

print(phone1.model)
