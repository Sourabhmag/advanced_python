class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Mother, Father):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Bike Racing")

c = Child()
c.skills()