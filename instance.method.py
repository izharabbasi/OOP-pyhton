class Person:
    def __init__(self, Name, Class, Age):
        self.Name = Name
        self.Class = Class
        self.Age = Age

    def name_class(self):
        return f"{self.Name} {self.Class}"


p1 = Person("izhar", 12, 24)
p2 = Person("shery", 14, 26)

print(p1.Name)
print(p2.name_class())
