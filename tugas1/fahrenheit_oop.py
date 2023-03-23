class Suhu:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def suhu(self):
        return (self.fahrenheit - 32) * 5/9


SuhuA = Suhu(45)
print(f"Suhu celcius: {SuhuA.suhu()}")
