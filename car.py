# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
car1 = Vehicle()
car2 = Vehicle()
car1.name = "namjoo's"
car1.color = "black"
car2.name = "namhoom's"
car2.color = "white"
car1.value = 2500
car2.kind = "truck"



# test code
print(car1.description())
print(car2.description())
