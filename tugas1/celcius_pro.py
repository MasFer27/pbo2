# NAMA  : FERLI
# NIM   : 210511140
# KELAS : R4/ D

class Suhu:
    def __init__(self, celcius):
        self.celcius = celcius
    def suhu(self):
        return self.celcius + 273.15
SuhuA = Suhu(20)
print(f"Suhu kelvin: {SuhuA.suhu()}")