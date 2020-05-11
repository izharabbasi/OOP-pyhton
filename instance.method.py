class Person:
    def __init__(self, Name, Class, Age):
        self.Name = Name
        self.Class = Class
        self.Age = Age

    def name_class(self):
        return f"{self.Name} {self.Class}"

    def over_18(self):
        return self.Age > 18


p1 = Person("izhar", 12, 24)
p2 = Person("shery", 14, 10)

print(p1.Name)
print(p2.name_class())
print(p2.over_18())
