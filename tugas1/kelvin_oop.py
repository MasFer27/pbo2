class Suhu:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def suhu(self):
        return (self.kelvin - 273) * 4/5


SuhuA = Suhu(20)
print(f"Suhu reamur: {SuhuA.suhu()}")
