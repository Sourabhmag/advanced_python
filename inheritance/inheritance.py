class Vehicle:
    def genral_usage(self):
        print("Genral Usage: Transportation")


class Bike(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.has_roof = False
        print("Bike constructor")

    def specific_usage(self):
        print("Specific Bike Usage: Road Trip")


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.has_roof = True
        print("Car constructor")

    def specific_usage(self):
        print("Specific Car Usage: Family Trip")


c = Car()
b = Bike()


print(c.specific_usage())
print(c.genral_usage())
print(b.specific_usage())
print(b.genral_usage())
print(isinstance(c, Car))
print(issubclass(Car, Vehicle))
