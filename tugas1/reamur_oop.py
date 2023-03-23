class Suhu:
    def __init__(self, reamur):
        self.reamur = reamur

    def suhu(self):
        return (self.reamur + 32) * 9/4


SuhuA = Suhu(34)
print(f"Suhu fahrenheit: {SuhuA.suhu()}")
