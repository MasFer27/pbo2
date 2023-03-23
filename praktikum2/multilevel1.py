class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} speaks")
class Snake(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def fly(self):
        print(f"{self.name} is eating {self.wingspan} chicken")
class python(Snake):
    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)
        self.color = color
    def speak(self):
        print(f"{self.name} is a {self.color} python that walks")

pythn = python("Python", 3, "Black")
pythn.speak() 
pythn.fly() 