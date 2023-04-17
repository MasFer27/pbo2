class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Toyota", "Corolla", 2022)

try:
    print(car.color)
except AttributeError:
    print("Objek Car tidak memiliki atribut 'color'")
